# Harness Project 3 — The Error Audit

**Harness Engineering — rewriting errors so the agent can self-heal.**

This project has two connectors that do the **exact same job** — a tiny
fake item-catalog API. The only difference: `api_client.py` returns raw,
cryptic errors, and `api_client_actionable.py` returns the same failures
rewritten to say what's wrong and exactly what to do about it.

This is Loop Engineering's connector rule (Concept 10), taken further:
**"the error message is the input to the next beat."** In a loop, nobody
is watching to translate a cryptic error into the right fix. The error
message itself has to do that job.

## Round 1 — Give the agent the raw connector

```bash
claude
```
Ask it to do a small task using the raw connector, without giving it any
extra hints about what's wrong:
```
Use connector/api_client.py to fetch item 999, then create a new item
called "Widget". Don't set any environment variables unless a command
tells you to.
```

**Watch what happens.** With `API_KEY` unset, the first call fails with
just `Error: 401`. Notice how the agent reacts:
- Does it guess wildly (retry the same broken command, or invent an
  unrelated fix)?
- Does it eventually figure out an environment variable is needed, or
  does it get stuck and ask you?

Then it'll hit `Error: 404` for item 999 (which doesn't exist) — watch
whether it understands *why*, or just reports the raw code back to you.

## Round 2 — Same task, the actionable connector

```
Use connector/api_client_actionable.py to fetch item 999, then create a
new item called "Widget". Don't set any environment variables unless a
command tells you to.
```

**Watch the difference.** The 401 error now says exactly what
environment variable to set and what value to use — a well-behaved agent
should self-correct immediately, without you saying anything else. The
404 error explains the valid range, so if asked to recover, the agent
knows to pick a real id instead of guessing blindly.

## What actually changed — line by line

| Failure | Raw | Actionable |
|---|---|---|
| Missing key | `Error: 401` | Names the exact env var, the exact value, and says "retry the same command" |
| Bad id type | `Error: 400` | Names which argument was wrong and shows a valid example |
| Id out of range | `Error: 404` | States the valid range (1–100) instead of just failing |
| Transient failure | `Error: 500` | Explicitly says "this is transient, retry unchanged" — vs. a plain 500, which looks identical to a permanent failure |
| Missing required field | `Error: 400` | Names the missing field and shows the exact fixed command |

## The transient-vs-permanent trap

Notice `Error: 500` and `Error: 404` look exactly the same in the raw
version — just a bare code. But they call for **opposite** responses: a
404 means "stop, this input is wrong, don't retry the same thing." A 500
means "this might just be transient, retrying the same request could
work." **A raw error code often can't tell an agent which one it's
looking at** — the rewrite has to say so explicitly, or a loop will
either retry something that can never succeed, or give up on something
that would have worked a second later.

## What ships in this folder

| File | Job |
|---|---|
| `connector/api_client.py` | Round 1 — the raw, cryptic connector |
| `connector/api_client_actionable.py` | Round 2 — identical logic, rewritten errors |

## The interview-ready idea

> "I compared an agent's behavior against two versions of the same fake
> API — one returning bare error codes, one returning the same failures
> rewritten to name the exact fix. With the raw version, the agent either
> got stuck or guessed. With the rewritten version, it self-corrected
> immediately, because the error message itself carried the next step.
> That's the difference between an error a human has to translate and
> one a loop can act on directly — and it matters most for the codes that
> look identical but mean opposite things, like a 404 that means 'stop'
> versus a 500 that means 'try again.'"
