# Loop Engineering Projects

Hands-on implementations of loop engineering patterns, built while completing the [GIAIC Final Marathon](https://agentfactory.panaversity.org/docs/loop-engineering-crash-course) Loop Engineering practice track. Each project is a working, self-built example of a different concept from the course — heartbeats, the spine, maker-checker verification, and codified workflows.

## What's a Loop?

A loop is a system that starts itself, checks its own work, records progress, and repeats — without a human driving each step. The four layers that make this possible:

- **Prompt** — a single message to the model
- **Context** — what the model can see in that moment
- **Harness** — one complete beat: instruction → tool use → self-verification → stop
- **Loop** — the system that starts, judges, and remembers multiple beats over time

## Projects

| # | Project | Concept | What It Demonstrates |
|---|---------|---------|----------------------|
| [01](./01-a-watch-loop) | **A Watch Loop** | In-session heartbeat | Watches the live USD → PKR exchange rate every minute. Closing the terminal kills the loop — the definition of an in-session heartbeat. |
| [02](./02-make-the-tests-pass-then-stop) | **Make the Tests Pass, Then Stop** | Conditional (`/goal`) heartbeat | Fixes 8 real bugs in a text-processing library until `pytest` genuinely passes — the checker is a proof, not an opinion. |
| [03](./03-the-morning-brief-with-a-memory) | **The Morning Brief With a Memory** | Scheduled heartbeat + the spine | A daily Hacker News brief that only reports stories not already shown, using a `seen-stories.txt` spine. Proved "no spine, no loop" by deleting that file. |
| [04](./04-a-fix-loop-with-a-real-checker) | **A Fix Loop With a Real Checker** | Maker-checker (subagents) | A pricing calculator fix, verified by a reviewer subagent against **both** the visible tests and a hidden checker with different numbers — catching fixes that only pretend to work. |
| [05](./05-codify-the-body) | **Codify the Body** | Dynamic workflows | Three independent buggy modules, fixed and verified in isolation by a single reusable `/fix-all-modules` command instead of a hand-typed prompt every time. |
| [06](./06-the-doorbell-loop) | **The Doorbell Loop** | Event-driven heartbeat | A GitHub Action that flags any **new** TODO/FIXME comment a pull request introduces — zero cost until a PR opens, and it automatically runs against every PR in this repo. |
| [07](./07-break-it-on-purpose) | **Break It On Purpose** | The Four Layers, diagnostic practice | Starts from a fully working loop and deliberately breaks each of the four layers (Prompt, Context, Harness, Loop) one at a time, to practice recognizing the symptom before reaching for a fix. |
| [08](./08-your-own-daily-loop) | **Your Own Daily Loop** | The full capstone | Combines every part of a loop — heartbeat, spine, isolated branches, maker-checker, human gate, and PR connector — into one daily maintenance loop that found real bugs, fixed them independently, and opened real pull requests. |

## Core Concepts Covered

- **Heartbeats** — in-session (`/loop`), conditional (`/goal`), scheduled (`/schedule`), and event-driven (GitHub Actions), each suited to a different shape of task
- **The spine** — persistent state between beats, without which a loop can't tell what it already did (Projects 3, 8)
- **Maker-checker** — the agent that does the work is never the one that approves it (Projects 2, 4, 5, 8)
- **A real checker** — a checker should test cases the maker never saw, not just replay the same tests (Project 4)
- **Human gate** — when a decision is genuinely ambiguous (a risky fix, two conflicting PRs), the loop escalates to a person instead of guessing (Project 8)
- **The Four Layers** — Prompt, Context, Harness, Loop — diagnosing which layer broke before reaching for a fix (Project 7)

## Stack

- [Claude Code](https://code.claude.com) — `/loop`, `/goal`, `/schedule`, Routines, subagents, and skills
- GitHub Actions — event-driven triggers (Project 06, and Project 08's PRs)
- Public, key-free APIs: [open.er-api.com](https://open.er-api.com) (exchange rates), [Hacker News API](https://github.com/HackerNews/API)
- `pytest` as the checker throughout — a passing test is a proof, not a claim

## Real Bugs Fixed Along the Way

Not just the projects' own intentional bugs — a few genuine issues came up building this repo, each a small lesson in its own right:

- A path-resolution bug in Project 3's spine (state file was writing to a nested folder instead of project root) — fixed by correcting `Path.resolve().parents[n]`.
- A missing `id-token: write` permission in Project 6's GitHub Actions workflow, needed for OIDC authentication.
- The Claude GitHub App not being installed on this repo (`/web-setup` only grants clone access, it doesn't install the app).
- Two PRs from Project 8's daily loop that would have conflicted on shared scaffold files, since the project directory had never been committed before — the loop correctly flagged this in `progress.md` under "needs a human" instead of guessing.

## Author

Muhammad — AI Automation Engineer, [NaveedTechLab](https://github.com/NaveedTechLab)
