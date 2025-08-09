#!/usr/bin/env bash
set -euo pipefail
# Resolve pandoc provided by pypandoc-binary inside venv; fallback to system pandoc
HERE="$(cd "$(dirname "$0")" && pwd)"
VENV_PY="$HERE/../.venv/bin/python"
PANDOC_BIN=""
if [ -x "$VENV_PY" ]; then
  PANDOC_BIN="$($VENV_PY - <<'PY'
import pypandoc
print(pypandoc.get_pandoc_path())
PY
)"
fi
if [ -z "$PANDOC_BIN" ] || [ ! -x "$PANDOC_BIN" ]; then
  PANDOC_BIN="pandoc"
fi
exec "$PANDOC_BIN" "$@"