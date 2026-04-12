#!/usr/bin/env bash
# step.sh – Switch src/code.py AND docs/*.rst to a specific workshop step.
#
# Usage:  ./step.sh <start|2|3|4|5|bonus|unbonus>
#
#   start   – Start state    (display only, no buzzer, no strip)
#   2       – Step 2 result  (docs done, buzzer to be added)
#   3       – Step 3 result  (buzzer done, LED strip to be added)
#   4       – Step 4 result  (LED strip done, zone logic to be added)
#   5       – Step 5 result  (complete implementation)
#   bonus   – Install Pharaoh Copilot agents into .github/
#   unbonus – Remove Pharaoh Copilot agents from .github/
#
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$SCRIPT_DIR/src"
WORKSHOP="$SCRIPT_DIR/.workshop"

case "${1:-}" in
  start) FROM="$WORKSHOP/step_start" ; LABEL="Start state (display only)" ;;
  2)     FROM="$WORKSHOP/step_2"     ; LABEL="Step 2 result (add buzzer)" ;;
  3)     FROM="$WORKSHOP/step_3"     ; LABEL="Step 3 result (add LED strip)" ;;
  4)     FROM="$WORKSHOP/step_4"     ; LABEL="Step 4 result (add zone logic)" ;;
  5)     FROM="$WORKSHOP/step_5"     ; LABEL="Step 5 result (complete)" ;;
  bonus)
    echo "==> Bonus: installing Pharaoh Copilot agents"
    BONUS="$WORKSHOP/step_bonus"
    mkdir -p "$SCRIPT_DIR/.github/agents" "$SCRIPT_DIR/.github/prompts"
    cp "$BONUS"/.github/agents/pharaoh.*.agent.md   "$SCRIPT_DIR/.github/agents/"
    cp "$BONUS"/.github/prompts/pharaoh.*.prompt.md "$SCRIPT_DIR/.github/prompts/"
    cp "$BONUS"/.github/copilot-instructions.md     "$SCRIPT_DIR/.github/copilot-instructions.md"
    if ! grep -q '\.pharaoh/' "$SCRIPT_DIR/.gitignore" 2>/dev/null; then
        printf '\n# Pharaoh session state (ephemeral, do not commit)\n.pharaoh/\n' >> "$SCRIPT_DIR/.gitignore"
        echo "    .gitignore: .pharaoh/ added"
    fi
    echo "    .github/agents/  – pharaoh agents installed"
    echo "    .github/prompts/ – pharaoh prompts installed"
    echo "    .github/copilot-instructions.md installed"
    echo ""
    echo "    Next: run @pharaoh.setup to generate pharaoh.toml"
    echo ""
    echo "    Available: @pharaoh.setup  @pharaoh.change  @pharaoh.trace"
    echo "               @pharaoh.mece  @pharaoh.author"
    exit 0
    ;;
  unbonus)
    echo "==> Bonus: removing Pharaoh Copilot agents"
    rm -f "$SCRIPT_DIR"/.github/agents/pharaoh.*.agent.md
    rm -f "$SCRIPT_DIR"/.github/prompts/pharaoh.*.prompt.md
    rm -f "$SCRIPT_DIR/.github/copilot-instructions.md"
    echo "    Pharaoh agents removed."
    exit 0
    ;;
  *)
    echo "Usage: $0 <start|2|3|4|5|bonus|unbonus>"
    echo "  start   – Start state    (display only)"
    echo "  2       – Step 2 result  (add buzzer)"
    echo "  3       – Step 3 result  (add LED strip)"
    echo "  4       – Step 4 result  (add zone logic)"
    echo "  5       – Step 5 result  (complete)"
    echo "  bonus   – Install Pharaoh Copilot agents"
    echo "  unbonus – Remove Pharaoh Copilot agents"
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
    if [ -f "$FROM/docs/schemas.json" ]; then
        cp "$FROM/docs/schemas.json" "$SCRIPT_DIR/docs/schemas.json"
    fi
    echo "    docs/ updated from $FROM/docs/"
fi

if [ -d "$FROM/tests" ]; then
    rm -f "$SCRIPT_DIR/tests/test_"*.py
    cp "$FROM/tests/test_"*.py "$SCRIPT_DIR/tests/"
    echo "    tests/ updated from $FROM/tests/"
fi
