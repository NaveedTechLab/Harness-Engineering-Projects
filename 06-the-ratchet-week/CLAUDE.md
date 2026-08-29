# CLAUDE.md — this file grows over the ratchet week

Every rule below was added because a REAL mistake happened once, was
classified by verb, and got turned into a permanent fix — never because
it "seemed like good practice" in the abstract. That's the ratchet: it
only ever moves forward, one caught mistake at a time.

## Rules

## Rule: run tests after any deletion
Added: 2026-08-20, after an agent deleted a function used only via
getattr() and broke the code without noticing.
Verb: Verify
Before reporting any task involving deleted code as complete, run the
project's test suite and show the output. A deletion is not "done" until
the tests have been shown to still pass.

<!--
Format for each NEW rule you add:

## Rule: <short name>
Added: <date>, after <one-line description of the mistake>
Verb: <Constrain | Inform | Verify | Correct | Escalate>
<the actual rule text an agent would read>
-->
