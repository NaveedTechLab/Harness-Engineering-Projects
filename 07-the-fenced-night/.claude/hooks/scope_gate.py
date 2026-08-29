#!/usr/bin/env python3
"""
scope_gate.py — a PreToolUse gate that fences the whole loop's blast
radius, not just one file.

Two rules, combined:
1. Write/Edit is only allowed inside watched/ or on progress.md. This
   loop's job is fixing modules and updating its own memory — nothing
   else. If it tries to touch anything outside that scope (including
   secrets/), it's blocked before the write happens.
2. Bash commands that reference "secrets" anywhere in the command string
   are blocked outright — this is the Project 1 wall, reapplied here.

This is what makes the night "fenced": even if the loop reads a
malicious instruction planted in a file it's working on, it cannot
actually act on it, because the fence isn't a suggestion in a prompt —
it's enforced at the tool layer.
"""

import json
import sys

ALLOWED_WRITE_PREFIXES = ("watched/", "./watched/")
ALLOWED_WRITE_EXACT = ("progress.md", "./progress.md")


def main() -> None:
    data = json.load(sys.stdin)
    tool_name = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    if tool_name in ("Write", "Edit"):
        file_path = tool_input.get("file_path", "")
        normalized = file_path.lstrip("./")
        allowed = normalized.startswith("watched/") or normalized in (
            "progress.md",
        )
        if not allowed:
            print(
                f"BLOCKED: this loop may only write inside watched/ or to "
                f"progress.md. Attempted write to: {file_path!r}. If this "
                f"file genuinely needs to change, that's a decision for a "
                f"human, not this loop.",
                file=sys.stderr,
            )
            sys.exit(2)

    if tool_name == "Bash":
        command = tool_input.get("command", "")
        if "secrets" in command:
            print(
                f"BLOCKED: this command references 'secrets', which this "
                f"loop is never allowed to read, copy, or act on, "
                f"regardless of why. Command was: {command!r}",
                file=sys.stderr,
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
