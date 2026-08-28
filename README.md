# /ENDGAME

**/ENDGAME** is a high-rigor orchestration skill for AI agents. It is designed for substantial tasks where incomplete work, silent scope reduction, weak verification, or premature completion are unacceptable.

It does **not** force every task through a giant checklist. Instead, it routes only the reasoning and specialist modules that the task actually needs.

## Core pipeline

`INTENT → CONTEXT → DECOMPOSE → RESEARCH → ARCHITECT → ASSUMPTIONS → ACCEPTANCE GATES → BUILD → TEST → SPEC-CHECK → ATTACK → AUTOPSY/FAILHOW → GROUND → UNLAZY → COMPLETE`

## What /ENDGAME is for

Use it for:

- software builds and refactors
- research and technical analysis
- complex document or artifact creation
- architecture and implementation planning
- security reviews
- multi-step workflows
- high-stakes deliverables that must be checked against a specification

Do **not** use it to inflate trivial tasks with unnecessary process.

## Design principles

1. **Understand before acting.** Determine the real deliverable, constraints, and definition of done.
2. **Retrieve before reinventing.** Use available files, code, prior decisions, specifications, and evidence when relevant.
3. **Define acceptance gates before substantial execution.** Completion criteria must be explicit and testable.
4. **Prefer the simplest design that satisfies the requirements.** Avoid complexity for its own sake.
5. **Make surgical changes when possible.** Preserve working behavior unless change is required.
6. **Test the actual output.** Do not equate implementation intent with successful execution.
7. **Check the result against the original request.** Avoid drift.
8. **Attack your own result.** Look for weaknesses, omissions, contradictions, security issues, and edge cases.
9. **Fix root causes, not symptoms.** Trace failures backward when necessary.
10. **Ground material claims.** Separate verified facts from inference, uncertainty, and unsupported assertions.
11. **Do not declare completion early.** If gates fail, report what remains.

## Install / use

### Generic prompt/agent systems

Copy [`SKILL.md`](./SKILL.md) into your agent's skill, rules, or system-prompt directory and expose it as `/ENDGAME` (or any command name you prefer).

### Claude-style skill directories

Place this repository (or just `SKILL.md`) in your skills folder. If your runtime supports slash commands, map `/ENDGAME` to the skill.

### OpenAI / Codex / custom agents

Use the contents of `SKILL.md` as a reusable developer/system instruction, or load it conditionally when a user invokes `/ENDGAME`.

## Minimal invocation

```text
/ENDGAME
Build a production-ready API for ...
```

Or in a system that does not support slash commands:

```text
Apply the ENDGAME workflow to this task: ...
```

## Routing

ENDGAME can call specialist behaviors only when useful, such as:

- deep research
- context retrieval
- evidence grounding
- software architecture
- test-driven development
- QA
- threat modeling / security review
- supply-chain review
- database review
- forensic review
- adversarial critique
- committee/rubric review

These are **capabilities**, not mandatory steps. An implementation may map them to its own tools or subagents.

## Acceptance behavior

A compliant ENDGAME run should never claim success merely because code was written or a document was generated. It should compare the result against the requested specification and acceptance gates, then either:

- report completion because the gates passed, or
- explicitly identify the unresolved blockers/failed gates.

## Repository contents

- `SKILL.md` — portable skill definition
- `agents/openai.yaml` — Codex display metadata and invocation policy
- `templates/acceptance-gates.md` — reusable completion-gate template
- `examples/usage.md` — example invocations
- `scripts/validate_skill.py` — repository validation
- `LICENSE` — GNU General Public License v3.0
- `CHANGELOG.md` — release history

## License

Copyright © 2026 Skylar Lyons.

ENDGAME is licensed under the **GNU General Public License v3.0 or later** (`GPL-3.0-or-later`). You may use, study, modify, and redistribute it under the terms of that license. See [`LICENSE`](./LICENSE).
