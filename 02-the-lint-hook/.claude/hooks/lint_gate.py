#!/usr/bin/env python3
"""
lint_gate.py — a GATE hook (meant for PreToolUse).

This fires BEFORE a Write or Edit happens. It inspects the PROPOSED
content — nothing has touched disk yet — and if it finds the bad
pattern, it exits 2, which blocks the tool call entirely. Claude never
gets to write the bad code in the first place.
"""

import json
import sys

BAD_PATTERN = "except:"


def main() -> None:
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    if tool_name not in ("Write", "Edit"):
        sys.exit(0)

    # Write uses "content"; Edit uses "new_string". Check whichever is present.
    proposed_content = tool_input.get("content") or tool_input.get("new_string") or ""

    if BAD_PATTERN in proposed_content:
        print(
            "BLOCKED: this edit introduces a bare 'except:' clause, which "
            "silently swallows all errors including KeyboardInterrupt and "
            "SystemExit. Use 'except Exception:' or catch a specific "
            "exception type instead.",
            file=sys.stderr,
        )
        sys.exit(2)  # exit 2 = block the tool call before it runs

    sys.exit(0)


if __name__ == "__main__":
    main()
