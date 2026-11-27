#!/bin/sh

# Create NeXus files for each subdirectory in publish_spm_images

set -e

scpt_dir=$(dirname "$0")

for dir in "$scpt_dir"/*/; do
    [ -d "$dir" ] || continue

    dir_name=$(basename "$dir")
    output_file="${dir_name}.nxs"

    echo "Converting: $dir_name"
    find "$dir" -type f ! -name '*.nxs' | xargs dataconverter --nxdl NXstm --reader spm --output "$output_file"
    mv "$output_file" "$dir"
done

echo "Done."
