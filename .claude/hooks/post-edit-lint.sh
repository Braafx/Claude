#!/bin/bash
# PostToolUse hook: auto-run ruff on Python files after Claude writes or edits them

input=$(cat)

tool_name=$(echo "$input" | jq -r '.tool_name // empty')
file_path=$(echo "$input" | jq -r '.tool_input.file_path // empty')

# Only act on Write or Edit tool calls
if [[ "$tool_name" != "Write" && "$tool_name" != "Edit" ]]; then
  exit 0
fi

# Only act on Python files
if [[ "$file_path" != *.py ]]; then
  exit 0
fi

# Only act if the file actually exists
if [[ ! -f "$file_path" ]]; then
  exit 0
fi

RUFF="/root/.local/bin/ruff"

if [[ ! -x "$RUFF" ]]; then
  exit 0
fi

"$RUFF" check --fix --quiet "$file_path" 2>/dev/null || true

exit 0
