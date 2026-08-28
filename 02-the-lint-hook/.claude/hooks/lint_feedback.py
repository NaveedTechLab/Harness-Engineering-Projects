#!/usr/bin/env python3
"""
lint_feedback.py — a FEEDBACK hook (meant for PostToolUse).

This fires AFTER a Write or Edit has already happened. It can complain,
but it cannot undo the edit — the bad code is already on disk by the time
this runs. This is the whole lesson of "feedback" hooks: they inform,
they don't gate.
"""

import json
import sys

BAD_PATTERN = "except:"


def main() -> None:
    data = json.load(sys.stdin)
    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path.endswith(".py"):
        sys.exit(0)

    try:
        with open(file_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        sys.exit(0)

    if BAD_PATTERN in content:
        print(
            f"⚠️  LINT WARNING: {file_path} contains a bare 'except:' clause. "
            "This was already written to disk — this hook can only warn, "
            "not prevent it. Consider fixing it in a follow-up edit.",
            file=sys.stderr,
        )

    # Always exit 0: this hook is feedback-only. Even if we found a
    # problem, a PostToolUse hook can't stop something that already
    # happened, so there's no reason to signal a block here.
    sys.exit(0)


if __name__ == "__main__":
    main()
