# Harness Project 2 — The Lint Hook

**Harness Engineering — Hooks: feedback vs gate.**

Two hooks can watch for the exact same problem and behave completely
differently, depending on **which event** they attach to:

- **`PostToolUse`** fires *after* a tool call finishes. It can inspect
  what happened and complain — but it **cannot undo it**. The file is
  already on disk.
- **`PreToolUse`** fires *before* a tool call runs. If it exits with
  code `2`, the tool call **never happens at all**.

Same bad pattern, same detection logic. Completely different outcome.
This project makes you feel that difference directly.

## The bad pattern we're watching for

A bare `except:` clause — it silently swallows every error, including
ones you almost never want to catch (`KeyboardInterrupt`, `SystemExit`).
Both hooks in this project detect exactly this one thing, so the only
variable in the drill is **when** the hook fires.

## Round 1 — Feedback hook (starts active)

The starter `.claude/settings.json` wires up `lint_feedback.py` on
`PostToolUse`. Start Claude Code:

```bash
claude
```

Ask it:
```
Add error handling to process_item in src/processor.py using a bare
except: clause that just passes silently.
```

**Watch what happens:**
1. The edit **succeeds** — the bare `except:` lands in the file.
2. *After* that, a warning appears (from the hook), pointing out the
   problem.
3. **The bad code is already there.** The warning is a suggestion for a
   follow-up fix, not a prevention.

Confirm it yourself:
```bash
cat src/processor.py
```
You'll see the bare `except:` sitting right there in the file, warning
or no warning.

## Round 2 — Switch to the gate hook

```bash
cp .claude/settings.gate.json .claude/settings.json
```
Restart Claude Code, reset the file first:
```bash
git checkout src/processor.py   # or manually restore the clean version
```

Ask the **exact same thing** again:
```
Add error handling to process_item in src/processor.py using a bare
except: clause that just passes silently.
```

**Watch what happens this time:**
1. The tool call is **blocked before it runs**. Claude sees the block
   message and typically tries a different approach (like
   `except Exception:`) on its own.
2. Check the file — the bare `except:` **never made it to disk** at all.

## Why this distinction matters

| | `PostToolUse` (feedback) | `PreToolUse` (gate) |
|---|---|---|
| When it fires | After the action | Before the action |
| Can it undo the action? | No | N/A — it prevents it |
| Good for | Formatting, running tests, logging, suggestions | Security rules, destructive commands, hard constraints |
| Cost | Cheap — the action already happened either way | Must be fast (ideally <100ms) — it's in the critical path of every matched tool call |

**The rule of thumb this project teaches:** if something must **never**
happen — a secret leaking, a destructive command, a broken invariant —
it belongs in a `PreToolUse` gate, not a `PostToolUse` warning. A
warning after the fact is fine for style nits. It is not a guardrail.

## What ships in this folder

| File | Job |
|---|---|
| `.claude/hooks/lint_feedback.py` | PostToolUse — warns, always exits 0 |
| `.claude/hooks/lint_gate.py` | PreToolUse — exits 2 to block before the write |
| `.claude/settings.json` | Starts wired to the feedback hook |
| `.claude/settings.gate.json` | Swap in for round 2 — wires the gate hook instead |
| `src/processor.py` | The file both hooks watch |

## The interview-ready idea

> "I built the same lint check as two different hooks — a PostToolUse
> version that only warns after the bad code is already written, and a
> PreToolUse version that inspects the proposed content and blocks the
> write with exit code 2 before it ever touches disk. It's a concrete
> reminder that a guardrail's timing matters as much as its logic: a
> check that fires too late is feedback, not a wall."
