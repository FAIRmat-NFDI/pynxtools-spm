#!/bin/sh
# Options go to `pynx convert`; a program (e.g. Galaxy's job command) runs unchanged.
set -e

if [ "$#" -eq 0 ]; then
    exec pynx convert --help
fi

case "$1" in
    -*) exec pynx convert "$@" ;;
esac

# A path or an installed program, e.g. `bash`, `python` or `/path/tool_script.sh`.
case "$1" in
    */*) exec "$@" ;;
esac
if command -v "$1" >/dev/null 2>&1; then
    exec "$@"
fi

# Otherwise a pynx subcommand, e.g. `convert --nxdl NXstm ...`.
exec pynx "$@"
