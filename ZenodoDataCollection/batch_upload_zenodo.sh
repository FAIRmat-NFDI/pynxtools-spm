#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# Batch-download Zenodo SPM records, unzip, and upload to S3.
#
# Usage:
#   ./batch_upload_zenodo.sh [--profile PROFILE] [--bucket BUCKET] [--dry-run]
#
# Pipeline for each record:
#   1. Skip if the record prefix already exists in S3.
#   2. Fetch the file list from the Zenodo API.
#   3. For each file (excluding .mp4):
#        - If the file is a .zip → download, unzip into WORKDIR/<record_id>/,
#          then delete the local zip.
#        - Otherwise → download directly into WORKDIR/<record_id>/.
#   4. aws s3 sync WORKDIR/<record_id>/ → s3://BUCKET/zenodo/<record_id>/
#   5. Delete WORKDIR/<record_id>/.
#
# S3 key layout: zenodo/<record_id>/<extracted-path-within-zip>
# (zip files that contain a root directory, e.g. AFM_dataset.zip → AFM_dataset/,
#  produce keys like zenodo/<id>/AFM_dataset/<file>; loose files inside a zip
#  land directly under zenodo/<id>/<file>.)
# ---------------------------------------------------------------------------

set -euo pipefail

# ---- defaults -------------------------------------------------------------
BUCKET="spm-zenodo-data-897035677417" # TODO: Collect account ID using aws comment or local profile
AWS_PROFILE="RubDev" # TODO: collect local profile from user input or env var
REGION="eu-central-1"
WORKDIR="/tmp/zenodo_spm_batch"
DRY_RUN=false
LOG_FILE="$(dirname "$0")/batch_upload.log"

# ---- records to process ---------------------------------------------------
# "Datasets of Interest" — record 20439519 re-queued because original upload
# used zips instead of extracted files; the S3 skip-check will guard duplicates.
INTEREST_RECORDS=(
    20439519
    19254504 15326266 14271622 14245518 10443995
    19087372 19086147 18847316 18847016 17831280
    14537302 14780459 11234725 6487575 19707666
    17533355 17360113 17202182 14196316 13595509
)

# "Unknown/Unsupported Format" records
UNKNOWN_RECORDS=(
    18060234 17350453 17423992 7664070 13744336
    10886977 17121837 11043571 7371527 18803936
    17733854 15148049 15995751 15533400 15520157
    14222590 14179239 14196376
)

ALL_RECORDS=("${INTEREST_RECORDS[@]}" "${UNKNOWN_RECORDS[@]}")

# ---- argument parsing -----------------------------------------------------
while [[ $# -gt 0 ]]; do
    case "$1" in
        --profile)  AWS_PROFILE="$2"; shift 2 ;;
        --bucket)   BUCKET="$2";      shift 2 ;;
        --dry-run)  DRY_RUN=true;     shift   ;;
        *)          echo "Unknown option: $1" >&2; exit 1 ;;
    esac
done

AWS_CMD="aws --profile $AWS_PROFILE"

# ---- helpers --------------------------------------------------------------
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

s3_prefix_exists() {
    local record_id="$1"
    $AWS_CMD s3 ls "s3://${BUCKET}/zenodo/${record_id}/" --region "$REGION" \
        2>/dev/null | grep -q . && return 0 || return 1
}

# ---- main upload logic ----------------------------------------------------
upload_record() {
    local record_id="$1"
    log "===== Processing record $record_id ====="

    if s3_prefix_exists "$record_id"; then
        log "SKIP: s3://${BUCKET}/zenodo/${record_id}/ already exists."
        return 0
    fi

    local api_json
    api_json=$(curl -fsSL "https://zenodo.org/api/records/${record_id}") \
        || { log "ERROR: Zenodo API failed for $record_id — skipping."; return 1; }

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
        log "WARNING: no files found for record $record_id."
        return 1
    fi

    local workdir="${WORKDIR}/${record_id}"
    mkdir -p "$workdir"

    local i
    for i in "${!keys[@]}"; do
        local filename="${keys[$i]}"
        local url="${urls[$i]}"
        local ext="${filename##*.}"

        # Skip video files
        if [[ "$ext" == "mp4" ]]; then
            log "  [$(( i + 1 ))/${#keys[@]}] SKIP video: $filename"
            continue
        fi

        log "  [$(( i + 1 ))/${#keys[@]}] Download: $filename"
        if [[ "$DRY_RUN" == true ]]; then
            if [[ "$ext" == "zip" ]]; then
                log "  [dry-run] Would unzip $filename → s3://${BUCKET}/zenodo/${record_id}/<contents>"
            else
                log "  [dry-run] Would upload $filename → s3://${BUCKET}/zenodo/${record_id}/${filename}"
            fi
            continue
        fi

        local local_path="${workdir}/${filename}"
        if ! curl -fL --retry 3 --retry-delay 10 -o "$local_path" "$url"; then
            log "  ERROR: download failed for $filename — skipping."
            rm -f "$local_path"
            continue
        fi

        if [[ "$ext" == "zip" ]]; then
            log "  Unzipping $filename ..."
            if ! unzip -q "$local_path" -d "$workdir"; then
                log "  ERROR: unzip failed for $filename."
            fi
            rm -f "$local_path"
            log "  Zip deleted, contents extracted to ${workdir}/"
        fi
        # Non-zip files stay at $workdir/$filename and are picked up by the sync below
    done

    if [[ "$DRY_RUN" == true ]]; then
        rm -rf "$workdir"
        log "===== Record $record_id dry-run complete ====="
        return 0
    fi

    # Upload each file into its own subfolder so metadata can be added alongside it.
    # S3 key layout: zenodo/<id>/<relative-dir>/<filename>/<filename>
    log "  Uploading extracted files with per-file subfolder layout ..."
    local uploaded=0 skipped=0
    while IFS= read -r -d '' filepath; do
        local relative="${filepath#${workdir}/}"
        local dirpart filename
        dirpart="$(dirname "$relative")"
        filename="$(basename "$relative")"

        # Build S3 key
        local s3_key
        if [[ "$dirpart" == "." ]]; then
            s3_key="zenodo/${record_id}/${filename}/${filename}"
        else
            s3_key="zenodo/${record_id}/${dirpart}/${filename}/${filename}"
        fi

        if $AWS_CMD s3 cp "$filepath" "s3://${BUCKET}/${s3_key}" \
                --region "$REGION" --quiet; then
            uploaded=$((uploaded + 1))
        else
            log "  ERROR: upload failed for $relative"
        fi
    done < <(find "$workdir" -type f \
        ! -path "*/__MACOSX/*" \
        ! -name ".DS_Store" \
        -print0)

    log "  Uploaded ${uploaded} file(s) (${skipped} skipped)."
    rm -rf "$workdir"
    log "  Local copy deleted."
    log "===== Record $record_id upload complete ====="
}

# ---- entry point ----------------------------------------------------------
mkdir -p "$WORKDIR"
log "Starting batch upload  bucket=${BUCKET}  profile=${AWS_PROFILE}  dry-run=${DRY_RUN}"
log "Total records: ${#ALL_RECORDS[@]}"

for record_id in "${ALL_RECORDS[@]}"; do
    upload_record "$record_id" || log "ERROR: record $record_id failed overall."
done

log "All records processed."
