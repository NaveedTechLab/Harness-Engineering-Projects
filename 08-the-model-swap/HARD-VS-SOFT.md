# HARD vs SOFT — What a Model Swap Should (and Shouldn't) Break

**The whole thesis of Harness Engineering, tested for real:** "a
guardrail lives in the harness, never in the prompt." If that's true,
swapping the model underneath should never break a guardrail — only
things that were always dependent on the model's judgment should shift.

Before you run anything, predict for each project: is its core guarantee
**HARD** (enforced by code — settings.json, a hook, a validator script —
and therefore should hold no matter which model is running) or **SOFT**
(depends on the model actually reasoning well — and therefore might
genuinely get worse with a weaker or different model)?

| Project | The guarantee being tested | HARD or SOFT? | Why |
|---|---|---|---|
| 1 — The First Wall | Secrets can't be read | **HARD** | Enforced by `deny` rules at the permission layer — the model never gets a vote |
| 2 — The Lint Hook | Bad code can't be written | **HARD** | `PreToolUse` exit 2 blocks the tool call regardless of which model requested it |
| 3 — The Error Audit | The agent self-heals from a bad call | **SOFT** | Self-healing requires the model to actually read and reason about the error message |
| 4 — The Tool Diet | Fewer tools → better tool choice | **SOFT** | Tool selection is a judgment call the model makes every time |
| 5 — The Typed Reviewer | Verdicts are valid, consistent JSON | **MIXED** | The *validator* is HARD (it'll catch bad JSON from any model) — but *producing* well-formed JSON in the first place is SOFT, and this is the single most likely thing to break |
| 6 — The Ratchet Week | Rules prevent repeat mistakes | **MIXED** | A hook-based fix is HARD; a `CLAUDE.md`-rule fix is SOFT — this project's own lesson was to notice which is which |
| 7 — The Fenced Night | The injection can't leak secrets | **HARD** (the block) / **SOFT** (whether the model even tries) | The hook stops the action either way — but a different model might be *more* or *less* likely to fall for the injection in the first place |

**The prediction worth making out loud before you test:** everything
marked HARD should hold with zero changes needed. Everything marked SOFT
or MIXED is fair game to break, and if it does, that's not a failure of
the drill — it's the data point this project exists to produce.
