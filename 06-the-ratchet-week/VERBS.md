# The 5 Verbs — Classification Guide

**Harness Engineering's core idea: every guardrail is one of five verbs.**
When you catch a mistake, the first question is not "how do I fix this
one instance" — it's **"which verb would have prevented this, and where
does that verb's fix permanently live?"**

| Verb | What it means | Where the fix lives | Example from this repo |
|---|---|---|---|
| **Constrain** | Remove the capability entirely, so the mistake becomes impossible | `.claude/settings.json` deny rules, sandboxing | Project 1 — denying `Read` (and later `Bash`) access to `secrets/` |
| **Inform** | Give the agent the right context/knowledge upfront, before it acts | `CLAUDE.md` / `AGENTS.md`, a skill | A rule like "always check `progress.md` before starting work" |
| **Verify** | Add a check that catches the mistake, before or after it happens | A hook, a test, a reviewer subagent | Project 2 — the lint gate hook; Project 5 — the typed reviewer |
| **Correct** | Give feedback specific enough that the agent fixes itself | Rewritten error messages, actionable failures | Project 3 — the error audit |
| **Escalate** | The decision genuinely needs a human — route it, don't guess | A human gate, a "needs a human" log entry | Loop Engineering Project 8/11 — flagging risky work instead of shipping it |

## How to pick the right verb for a real mistake

Ask these in order:

1. **Could this have been made literally impossible?** → Constrain.
   (Example: an agent that deleted a file it wasn't asked to touch —
   remove `rm` from its toolset or deny it on that path.)
2. **Did the agent lack information it needed to get this right?** →
   Inform. (Example: it didn't know your project uses `pytest`, not
   `unittest` — add one line to `CLAUDE.md`.)
3. **Could a check have caught this before/after it shipped?** → Verify.
   (Example: it introduced a lint violation — a hook would catch it.)
4. **Did it get an unhelpful error and then guess wrong?** → Correct.
   (Example: a cryptic `Error: 500` led to a bad retry — rewrite the
   error.)
5. **Was this a judgment call a person should have made?** → Escalate.
   (Example: it merged a PR when the change was genuinely ambiguous —
   that should have gone to a human gate instead.)

**A mistake often fits more than one verb.** Pick the one that removes
the *most* risk for the *least* cost — usually Constrain first if it's
available, since it's the only one that makes the mistake structurally
impossible rather than just less likely.
