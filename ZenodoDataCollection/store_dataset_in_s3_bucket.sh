#!/usr/bin/env bash

# Apply strict mode only when executed directly, not when sourced.
# Sourcing with set -e active would exit the caller's shell on any error.
if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    set -euo pipefail
fi

# ---------------------------------------------------------------------------
# Usage (standalone):
#   ./store_dataset_in_s3_bucket.sh [--region REGION] [--profile PROFILE] [FUNCTION] [ARGS...]
#
# Usage (source into another script):
#   source ./store_dataset_in_s3_bucket.sh --region eu-central-1 --profile RubDev
#   create_s3_bucket "my-bucket"
# ---------------------------------------------------------------------------

DEFAULT_REGION="eu-central-1"

# --- Argument parsing -------------------------------------------------------
# Two-pass parse: flags (--region, --profile) and positional args (function
# name + its own args) can appear in any order.
REGION="${REGION:-$DEFAULT_REGION}"
AWS_PROFILE="${AWS_PROFILE:-}"

_positional_args=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --region)   REGION="$2";      shift 2 ;;
        --profile)  AWS_PROFILE="$2"; shift 2 ;;
        --)         shift; _positional_args+=("$@"); break ;;
        -*)         echo "Unknown option: $1" >&2; [[ "${BASH_SOURCE[0]}" == "$0" ]] && exit 1 || return 1 ;;
        *)          _positional_args+=("$1"); shift ;;  # collect positional args
    esac
done

set -- "${_positional_args[@]+"${_positional_args[@]}"}"  # restore positionals

# Build a reusable aws-cli prefix so every function picks up profile + region
AWS_CMD="aws"
[[ -n "$AWS_PROFILE" ]] && AWS_CMD="$AWS_CMD --profile $AWS_PROFILE"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

# Returns the AWS account ID of the active credentials (cached after first call)
_AWS_ACCOUNT_ID=""
get_account_id() {
    if [[ -z "$_AWS_ACCOUNT_ID" ]]; then
        _AWS_ACCOUNT_ID=$($AWS_CMD sts get-caller-identity --query Account --output text) \
            || { echo "ERROR: could not retrieve AWS account ID — check credentials." >&2; return 1; }
    fi
    echo "$_AWS_ACCOUNT_ID"
}

# Appends the account ID to a bucket name if it does not already end with it.
#   Usage: unique_bucket_name "my-bucket"  →  "my-bucket-123456789012"
unique_bucket_name() {
    local name="$1"
    local account_id
    account_id=$(get_account_id)
    if [[ "$name" != *"-$account_id" ]]; then
        echo "${name}-${account_id}"
    else
        echo "$name"
    fi
}

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

create_s3_bucket() {
    local raw_name="$1"
    local bucket
    bucket=$(unique_bucket_name "$raw_name")
    echo "Creating bucket '$bucket' in region '$REGION'..."
    $AWS_CMD s3api create-bucket \
        --bucket "$bucket" \
        --region "$REGION" \
        --create-bucket-configuration LocationConstraint="$REGION"
}

# ---------------------------------------------------------------------------
# Upload a Zenodo record's files to S3
#
# Usage: upload_zenodo_record <record_id> <bucket>
#
# For each file in the record (excluding .mp4):
#   - .zip files  → downloaded, unzipped into WORKDIR/<record_id>/, zip deleted.
#   - other files → downloaded directly into WORKDIR/<record_id>/.
# After all downloads, aws s3 sync WORKDIR/<record_id>/ → s3://bucket/zenodo/<record_id>/
#
# S3 key layout: zenodo/<record_id>/<extracted-path-within-zip>
# (zips with an internal root dir, e.g. AFM_dataset.zip → AFM_dataset/,
#  produce keys like zenodo/<id>/AFM_dataset/<file>.)
# ---------------------------------------------------------------------------

WORKDIR="${WORKDIR:-/tmp/zenodo_spm_download}"

upload_zenodo_record() {
    local record_id="$1"
    local bucket="$2"

    if [[ -z "$record_id" || -z "$bucket" ]]; then
        echo "Usage: upload_zenodo_record <record_id> <bucket>" >&2
        return 1
    fi

    echo "Fetching file list for Zenodo record $record_id ..."
    local api_json
    api_json=$(curl -fsSL "https://zenodo.org/api/records/${record_id}") \
        || { echo "ERROR: could not reach Zenodo API." >&2; return 1; }

    local keys urls
    mapfile -t keys < <(echo "$api_json" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for f in data.get('files', []):
    print(f['key'])
")
    mapfile -t urls < <(echo "$api_json" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for f in data.get('files', []):
    print(f['links']['self'])
")

    if [[ ${#keys[@]} -eq 0 ]]; then
        echo "WARNING: no files found for record $record_id" >&2
        return 1
    fi

    local workdir="${WORKDIR}/${record_id}"
    mkdir -p "$workdir"

    local i
    for i in "${!keys[@]}"; do
        local filename="${keys[$i]}"
        local url="${urls[$i]}"
        local ext="${filename##*.}"

        # Skip video files — they dominate dataset size and are not SPM data.
        if [[ "$ext" == "mp4" ]]; then
            echo "[$(( i + 1 ))/${#keys[@]}] Skipping video: $filename"
            continue
        fi

        echo ""
        echo "[$(( i + 1 ))/${#keys[@]}] Downloading: $filename"
        local local_path="${workdir}/${filename}"
        curl -fL --retry 3 --retry-delay 5 -o "$local_path" "$url" \
            || { echo "ERROR: download failed for $filename — skipping." >&2; rm -f "$local_path"; continue; }

        if [[ "$ext" == "zip" ]]; then
            echo "    Unzipping $filename ..."
            unzip -q "$local_path" -d "$workdir" \
                || echo "    WARNING: unzip reported errors for $filename."
            rm -f "$local_path"
            echo "    Zip deleted, contents extracted."
        fi
    done

    echo ""
    # Upload each file into its own subfolder so metadata can be added alongside it.
    # S3 key layout: zenodo/<id>/<relative-dir>/<filename>/<filename>
    echo "Uploading extracted files with per-file subfolder layout ..."
    local uploaded=0
    while IFS= read -r -d '' filepath; do
        local relative="${filepath#${workdir}/}"
        local dirpart filename
        dirpart="$(dirname "$relative")"
        filename="$(basename "$relative")"

        local s3_key
        if [[ "$dirpart" == "." ]]; then
            s3_key="zenodo/${record_id}/${filename}/${filename}"
        else
            s3_key="zenodo/${record_id}/${dirpart}/${filename}/${filename}"
        fi

        if $AWS_CMD s3 cp "$filepath" "s3://${bucket}/${s3_key}" --quiet; then
            uploaded=$((uploaded + 1))
        else
            echo "  ERROR: upload failed for $relative" >&2
        fi
    done < <(find "$workdir" -type f \
        ! -path "*/__MACOSX/*" \
        ! -name ".DS_Store" \
        -print0)

    echo "Uploaded ${uploaded} file(s)."
    rm -rf "$workdir"
    echo "Local copy deleted."
    echo "Record $record_id upload complete."
}

# add more functions here ...

# ---------------------------------------------------------------------------
# Entry point
#
# When sourced:  BASH_SOURCE[0] != $0  →  skip this block entirely,
#                functions are available in the caller's shell.
# When executed: first positional arg selects the function to run;
#                no arg runs main().
# ---------------------------------------------------------------------------

main() {
    create_s3_bucket "my-zenodo-dataset-bucket"
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    if [[ $# -gt 0 ]]; then
        # Call the named function with remaining args: ./script.sh create_s3_bucket my-bucket
        "$@"
    else
        main
    fi
fi
