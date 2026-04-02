#!/usr/bin/env bash
# step.sh – Switch src/code.py AND docs/*.rst to a specific workshop step.
#
# Usage:  ./step.sh <1-5>
#
#   1 – Start state    (display only, no buzzer, no strip)
#   2 – Step 3 start   (buzzer to be added)
#   3 – Step 4 start   (LED strip to be added)
#   4 – Step 5 start   (zone logic to be added)
#   5 – Final state    (complete implementation)
#
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$SCRIPT_DIR/src"
WORKSHOP="$SCRIPT_DIR/.workshop"

case "${1:-}" in
  1) FROM="$WORKSHOP/start"             ; LABEL="Start state (display only)" ;;
  2) FROM="$WORKSHOP/step_3"            ; LABEL="Step 3 start (add buzzer)" ;;
  3) FROM="$WORKSHOP/step_4"            ; LABEL="Step 4 start (add LED strip)" ;;
  4) FROM="$WORKSHOP/step_5"            ; LABEL="Step 5 start (add zone logic)" ;;
  5) FROM="$WORKSHOP/step_5/solutions"  ; LABEL="Final state (complete)" ;;
  *)
    echo "Usage: $0 <1-5>"
    echo "  1 – Start state    (display only)"
    echo "  2 – Step 3 start   (add buzzer)"
    echo "  3 – Step 4 start   (add LED strip)"
    echo "  4 – Step 5 start   (add zone logic)"
    echo "  5 – Final state    (complete)"
    exit 1
    ;;
esac

cp "$FROM/code.py" "$SRC/code.py"
echo "==> $LABEL"
echo "    src/code.py updated from $FROM/code.py"

if [ -d "$FROM/docs" ]; then
    cp "$FROM/docs/user_stories.rst" "$SCRIPT_DIR/docs/user_stories.rst"
    cp "$FROM/docs/architecture.rst"  "$SCRIPT_DIR/docs/architecture.rst"
    cp "$FROM/docs/test_cases.rst"    "$SCRIPT_DIR/docs/test_cases.rst"
    echo "    docs/ updated from $FROM/docs/"
fi

if [ -d "$FROM/tests" ]; then
    rm -f "$SCRIPT_DIR/tests/test_"*.py
    cp "$FROM/tests/test_"*.py "$SCRIPT_DIR/tests/"
    echo "    tests/ updated from $FROM/tests/"
fi
