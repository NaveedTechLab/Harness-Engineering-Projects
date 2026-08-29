# Harness Project 6 — The Ratchet Week

**Harness Engineering — turning every caught mistake into a permanent fix.**

This is the habit that ties every other Harness project together. A
"ratchet" only ever moves one direction — once tightened, it doesn't
slip back. Applied here: **once you catch a mistake and turn it into a
guardrail, that class of mistake should never cost you again**, because
the fix lives in the harness (a rule, a hook, a check), not in your
memory of "be more careful next time."

This project runs for **7 days, about 15 minutes a day** — it's the one
project in this track that can't be compressed into a single sitting,
because the whole point is noticing mistakes during real work, not a
synthetic bug someone planted for you.

## Before you start

Read `VERBS.md`. Every mistake this week gets classified into one of
five verbs: **Constrain, Inform, Verify, Correct, Escalate**. You've
already built one working example of each, without necessarily naming it
that way:

| Verb | You already built this in... |
|---|---|
| Constrain | Harness Project 1 (deny rules) |
| Verify | Harness Project 2 (the lint gate hook), Project 5 (typed reviewer) |
| Correct | Harness Project 3 (rewriting connector errors) |
| Escalate | Loop Engineering Project 8/11 (human gates) |
| Inform | Every `CLAUDE.md` / `AGENTS.md` rule you've written so far |

This week, you're not learning the verbs — you're practicing catching a
mistake **as it happens** and immediately picking the right one.

## The daily loop (do this once a day)

1. **Work normally** with Claude Code — on this project, a real project,
   or anything else you're doing this week.
2. **Notice one real mistake.** Not a bug in someone else's planted demo
   — an actual moment where the agent did something wrong, sloppy, or
   not what you meant.
3. **Open `VERBS.md`** and walk through the 5 questions to pick a verb.
4. **Make the smallest permanent fix** for that verb — add a line to
   `CLAUDE.md`, write a quick hook, add a test, or note where a human
   gate belongs.
5. **Log it** in `ratchet-log.md` under that day.

Read Day 1's worked example in `ratchet-log.md` before you do your own —
it shows the whole cycle end to end, including the reasoning for why one
verb was chosen over another.

## What "permanent" means here

A fix that lives only in your head, or that you'll "remember to mention
next time," is not permanent — it's a hope. A fix counts as permanent if
a **fresh Claude Code session, with no memory of today, would still
benefit from it.** That's why `CLAUDE.md` rules and hooks are the two
most common landing spots: both get read by every future session
automatically.

## Common mistake when doing this drill

**Defaulting to "Inform" for everything.** Writing a `CLAUDE.md` rule
feels easy, so it's tempting to write one for every mistake, even when
the mistake really called for Constrain (remove the capability) or
Verify (add an actual check). A rule only works if the agent reads it
*and* chooses to follow it in the moment — it's the weakest of the five
verbs precisely because it depends on the model's judgment at exactly
the moment judgment failed once already. If the same category of mistake
shows up twice despite an "Inform" fix, that's a strong signal it needed
a stronger verb.

## What ships in this folder

| File | Job |
|---|---|
| `VERBS.md` | The 5-verb classification guide, with a decision order |
| `CLAUDE.md` | **The file that grows** — already has one real-shaped rule as an example |
| `ratchet-log.md` | Daily tracker, Day 1 fully worked as a template |

## The interview-ready idea

> "For a week, I made it a rule to catch at least one real agent mistake
> per day, classify it against five verbs — constrain, inform, verify,
> correct, escalate — and turn it into a permanent fix rather than just
> a one-off correction. The habit that mattered most wasn't any single
> fix, it was noticing when I'd used a weak verb: if a mistake I'd
> 'fixed' with a CLAUDE.md rule happened again, that was a signal the
> fix needed to be a hook or a deny rule instead — something enforced,
> not just remembered."
