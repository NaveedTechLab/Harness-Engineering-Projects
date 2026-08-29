# Harness Engineering Projects

Hands-on implementations of Harness Engineering patterns, built while completing the [GIAIC Final Marathon](https://agentfactory.panaversity.org/docs/harness-engineering-crash-course) Harness Engineering practice track — all 8 practice projects, self-built and self-tested, covering the five verbs that make an agent trustworthy to run unattended.

Builds directly on [Loop-Engineering-Projects](https://github.com/NaveedTechLab/Loop-Engineering-Projects) — a loop decides *when* work happens; a harness decides *what an agent is allowed to do while it happens*.

## The Five Verbs

Every guardrail in this repo is one of five verbs:

- **Constrain** — remove a capability entirely, so a mistake becomes structurally impossible
- **Inform** — give the agent the right context/knowledge before it acts
- **Verify** — add a check (a hook, a test, a reviewer) that catches a problem before or after it happens
- **Correct** — rewrite feedback so specific that the agent fixes itself
- **Escalate** — route a genuinely ambiguous decision to a human instead of guessing

The one rule that ties them all together: **a guardrail lives in the harness, never in the prompt.**

## Projects

| # | Project | Verb(s) | What It Demonstrates |
|---|---------|---------|----------------------|
| [01](./01-the-first-wall) | **The First Wall** | Constrain | Wrote a deny rule blocking the `Read` tool from a secrets folder, then attacked my own wall — got the contents out through `Bash`'s `cat`, a Python script, a file copy, and base64 obfuscation. A blacklist only closes doors you specifically named; the reliable fix is removing the capability, not listing forbidden phrasings. |
| [02](./02-the-lint-hook) | **The Lint Hook** | Verify | The same lint check as two different hooks: a `PostToolUse` version that only warns after bad code is already written, and a `PreToolUse` version that blocks the write with exit code 2 before it ever touches disk. A check that fires too late is feedback, not a wall. |
| [03](./03-the-error-audit) | **The Error Audit** | Correct | Compared an agent's behavior against two versions of the same fake API — one returning bare error codes, one rewritten to name the exact fix. The rewritten version let the agent self-correct immediately, especially for codes that look identical but mean opposite things, like a 404 ("stop") versus a 500 ("try again"). |
| [04](./04-the-tool-diet) | **The Tool Diet** | Inform / Verify | Gave two subagents an identical bug-fixing task — one with eight overlapping tools, one with exactly three scoped tools — and tracked tool-call counts and decoy-file detours across trials. Fewer, focused tools measurably reduce wasted turns. |
| [05](./05-the-typed-reviewer) | **The Typed Reviewer** | Verify | Moved a reviewer subagent from free-text PASS/FAIL to a strict JSON verdict, then wrote a validator checking both schema shape and cross-field consistency — catching a verdict of `PASS` with `tests_passed: false`, which schema validation alone would never flag. |
| [06](./06-the-ratchet-week) | **The Ratchet Week** | All five | A week-long habit: catch one real agent mistake a day, classify it against the five verbs, and turn it into a permanent fix rather than a one-off correction — noticing when a weak verb (a `CLAUDE.md` rule) needed to be a strong one (a hook) instead. |
| [07](./07-the-fenced-night) | **The Fenced Night** | Constrain + Verify + Escalate | Planted a real prompt injection inside a file a working loop would naturally read while fixing a genuine bug — an instruction asking it to leak a fake secret into its own memory file. A `PreToolUse` hook blocked the write and the shell command regardless of why the model wanted to run them. |
| [08](./08-the-model-swap) | **The Model Swap** | Capstone | Re-ran the deny rules, hooks, and JSON validator under a different, smaller model. Every guardrail enforced by code held identically; the one place behavior shifted was raw JSON formatting from the model itself — confirming which guarantees were truly hard versus which only ever depended on one model's habits. |

## Core Concepts Covered

- **Blacklists vs. removing capability** — a `deny` list only closes doors you named; sandboxing removes the door entirely (Project 01)
- **Hook timing** — `PreToolUse` can prevent; `PostToolUse` can only report after the fact (Project 02)
- **Actionable errors** — an error message is the input to an agent's next move, and must say what to do, not just what failed (Project 03)
- **Tool surface area** — every extra tool is a decision point that can go wrong, especially unattended (Project 04)
- **Structural vs. consistency validation** — a model can produce well-typed JSON that still contradicts itself; only checking field relationships catches that (Project 05)
- **The ratchet** — a caught mistake that isn't turned into a permanent, enforced fix will happen again (Project 06)
- **Defense in depth** — no single guardrail is enough; a fence is the combination of several (Project 07)
- **Hard vs. soft guarantees** — a real guardrail should hold across models; if it doesn't, it was never actually enforced (Project 08)

## Stack

- [Claude Code](https://code.claude.com) — `settings.json` permissions, hooks (`PreToolUse`/`PostToolUse`), subagents
- Python — hook scripts, validators, and test fixtures throughout
- `pytest` as the ground-truth checker for every bug-and-fix scenario

## Real Findings Along the Way

- Confirmed a naive `Read`-only deny rule is trivially bypassed via `Bash` (`cat`, a script, a copy, base64) — the actual fix is removing filesystem access, not enumerating denied commands.
- Verified a `PreToolUse` exit-2 hook genuinely prevents a write, where a `PostToolUse` hook on the identical check could only warn after the fact.
- Confirmed a validator's consistency checks (not just schema checks) are what catch a self-contradictory but well-typed verdict.
- Confirmed a `PreToolUse` hook blocks a planted prompt-injection payload's actual action (reading/leaking a secret) regardless of whether the model was tempted to comply with the injected instruction first.

## Author

Muhammad — AI Automation Engineer, [NaveedTechLab](https://github.com/NaveedTechLab)
