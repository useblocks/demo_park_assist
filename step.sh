#!/usr/bin/env bash
# step.sh – Switch src/code.py AND docs/*.rst to a specific workshop step.
#
# Usage:  ./step.sh <start|2|3|4|5>
#
#   start – Start state    (display only, no buzzer, no strip)
#   2     – Step 2 result  (docs done, buzzer to be added)
#   3     – Step 3 result  (buzzer done, LED strip to be added)
#   4     – Step 4 result  (LED strip done, zone logic to be added)
#   5     – Step 5 result  (complete implementation)
#
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SRC="$SCRIPT_DIR/src"
WORKSHOP="$SCRIPT_DIR/.workshop"

case "${1:-}" in
  start) FROM="$WORKSHOP/step_start" ; LABEL="Start state (display only)" ;;
  2)     FROM="$WORKSHOP/step_2"     ; LABEL="Step 2 result (add buzzer)" ;;
  3)     FROM="$WORKSHOP/step_3"     ; LABEL="Step 3 result (add LED strip)" ;;
  4)     FROM="$WORKSHOP/step_4"     ; LABEL="Step 4 result (add zone logic)" ;;
  5)     FROM="$WORKSHOP/step_5"     ; LABEL="Step 5 result (complete)" ;;
  *)
    echo "Usage: $0 <start|2|3|4|5>"
    echo "  start – Start state    (display only)"
    echo "  2     – Step 2 result  (add buzzer)"
    echo "  3     – Step 3 result  (add LED strip)"
    echo "  4     – Step 4 result  (add zone logic)"
    echo "  5     – Step 5 result  (complete)"
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
