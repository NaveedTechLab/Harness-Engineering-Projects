# ratchet-log.md — 7 days, ~15 minutes each

**The rule:** every day this week, during your normal work with Claude
Code (on any project — this one or a real one), catch ONE real mistake
the agent made. Classify it by verb (see `VERBS.md`), turn it into a
permanent fix, and log it here. If you genuinely catch zero mistakes on
a day, log that too — it's a valid, if rare, outcome.

---

## Day 1 — WORKED EXAMPLE (read this before starting your own)

**Date:** 2026-08-20

**What happened:** Asked the agent to "clean up unused imports" in a
file. It went further than asked and deleted an entire function it
decided looked unused — the function was actually called dynamically via
`getattr()`, so this broke the code.

**Classify:** Could this have been made impossible? Not easily — "delete
unused code" is genuinely useful most of the time. Could a check have
caught it before it shipped? Yes — running the test suite after any
deletion would have caught the break immediately.

**Verb chosen:** Verify.

**Permanent fix:** Added a rule to `CLAUDE.md` requiring the test suite
to run after any deletion, before reporting the task done. Also
considered whether a PostToolUse hook (like Harness Project 2's lint
hook) running `pytest` after any `Edit`/`Write` would enforce this more
reliably than a rule the agent has to remember. Chose the `CLAUDE.md`
rule for now since it's faster to add; flagged the hook as a stronger
Round 2 version if the mistake repeats.

**Rule added to `CLAUDE.md`:**
```
## Rule: run tests after any deletion
Added: 2026-08-20, after an agent deleted a function used only via
getattr() and broke the code without noticing.
Verb: Verify
Before reporting any task involving deleted code as complete, run the
project's test suite and show the output. A deletion is not "done" until
the tests have been shown to still pass.
```

---

## Day 2

**Date:**

**What happened:**

**Classify (walk through the 5 questions in VERBS.md):**

**Verb chosen:**

**Permanent fix:**

**Rule/hook/check added (paste it, or note where it lives):**

---

## Day 3

**Date:**

**What happened:**

**Classify:**

**Verb chosen:**

**Permanent fix:**

**Rule/hook/check added:**

---

## Day 4

**Date:**

**What happened:**

**Classify:**

**Verb chosen:**

**Permanent fix:**

**Rule/hook/check added:**

---

## Day 5

**Date:**

**What happened:**

**Classify:**

**Verb chosen:**

**Permanent fix:**

**Rule/hook/check added:**

---

## Day 6

**Date:**

**What happened:**

**Classify:**

**Verb chosen:**

**Permanent fix:**

**Rule/hook/check added:**

---

## Day 7

**Date:**

**What happened:**

**Classify:**

**Verb chosen:**

**Permanent fix:**

**Rule/hook/check added:**

---

## End-of-week review

- How many of the 7 days had a real mistake to log?
- Which verb came up most often for you?
- Pick your single best permanent fix from the week. Would it have
  prevented the mistake if it had existed BEFORE that mistake happened?
- Did any single mistake happen more than once during the week, even
  after you "fixed" it the first time? (If so, the first fix probably
  used too weak a verb — e.g. Inform when the mistake needed Constrain.)
