# Harness Project 4 — The Tool Diet

**Harness Engineering — fewer, focused tools beat many overlapping ones.**

Loop Engineering's Concept 10 said it as a rule of thumb: *"cutting an
agent's available tools raises its success rate... if a human engineer
cannot say for certain which tool fits the job, neither can the agent."*
This project turns that rule into something you actually measure, not
just believe.

## The setup

`codebase/` is a small shopping cart with a real, findable bug:
`calculate_order_total()` in `cart.py` forgets to multiply price by
quantity. There are also two **decoys**:
- `notifications.py` — plausible-looking, completely irrelevant
- `legacy/old_cart.py` — has a similarly-named function
  (`calculate_total`, not `calculate_order_total`) that could confuse a
  careless search

Confirm the bug is live:
```bash
cd codebase
python3 -m pytest test_cart.py -v
```
Should show **2 failed**.

## Two agents, same job, different toolbox

- **`wide-toolset`** — `Read, Grep, Glob, Bash, Edit, Write, WebSearch, WebFetch`.
  Overlapping and mostly irrelevant to this task (why would a bug fix
  need `WebSearch`?).
- **`narrow-toolset`** — `Read, Grep, Edit`. Exactly what's needed and
  nothing more.

## Round 1 — Run the wide-toolset agent

```bash
claude
```
```
Use the wide-toolset subagent to find and fix the bug: calculate_order_total
in codebase/cart.py is returning the wrong total. Have it report which
files it opened, in what order, and how many tool calls it took.
```

Record the result in `tool-diet-log.md` under Wide-toolset, Trial 1.

**Reset the bug before the next trial:**
```bash
cd codebase && python3 -m pytest test_cart.py   # confirm it's failing again
```
(If a previous trial fixed it, manually revert `cart.py`'s
`calculate_order_total` back to the buggy line before re-running.)

## Round 2 — Run the narrow-toolset agent

```
Use the narrow-toolset subagent to find and fix the bug: calculate_order_total
in codebase/cart.py is returning the wrong total. Have it report which
files it opened, in what order, and how many tool calls it took.
```

Record the result under Narrow-toolset, Trial 1.

## Do this ~5 times each, ideally across different sessions/days

One trial proves nothing — a lucky or unlucky run either way is noise.
The course's real version of this project runs over about a week. Repeat
both rounds a few times (resetting the bug each time), fill in
`tool-diet-log.md`, and look at the averages, not any single run.

## What to look for

- **Tool call count** — does the wide-toolset agent take more calls to
  reach the same fix, because it has more options to consider at each
  step?
- **Decoy detours** — does it ever open `notifications.py` "just in
  case," or get confused by `legacy/old_cart.py`'s similarly-named
  function?
- **First-try correctness** — does the narrow-toolset agent, with less to
  choose from, converge on the right fix more reliably?

## Why this matters for a loop specifically

In a chat session, a wasted tool call costs you a few seconds of
patience. **In an unattended loop, every wrong tool pick costs a full
beat — forever, every time that pattern repeats**, because nobody is
there to redirect it. A tool list you'd trim for a human's sake matters
even more for a loop's sake.

## What ships in this folder

| File | Job |
|---|---|
| `codebase/` | The buggy cart, plus two decoys |
| `.claude/agents/wide-toolset.md` | Round 1 — many overlapping tools |
| `.claude/agents/narrow-toolset.md` | Round 2 — only what's needed |
| `tool-diet-log.md` | Trial tracker across multiple runs |

## The interview-ready idea

> "I gave two subagents the identical bug-fixing task — one with eight
> overlapping tools including things like WebSearch that had nothing to
> do with the job, one with exactly three tools scoped to the task. I
> tracked tool-call counts and decoy-file detours across several trials.
> The wide-toolset agent was more likely to waste calls opening irrelevant
> files. In a chat session that costs a few seconds; in an unattended
> loop, every wrong tool pick costs a full wasted beat, every time that
> pattern repeats — which is why trimming the toolbox is a real
> reliability lever, not just tidiness."
