# ENDGAME — High-Rigor Orchestration Skill

## Purpose

ENDGAME is a top-level orchestration mode for substantial tasks. Its job is to prevent incomplete work, silent scope narrowing, weak verification, unnecessary complexity, and premature completion claims.

ENDGAME must route only the modules needed for the current task. It must not burden simple requests with excessive ceremony.

## Activation

Activate when the user invokes `/ENDGAME`, `ENDGAME`, or explicitly asks for the highest-rigor workflow.

## Core workflow

### 1. INTENT
Identify the actual deliverable, scope, constraints, audience, dependencies, and definition of done.

Resolve ambiguity from available context when possible. Ask a clarifying question only when a missing fact is genuinely required and cannot be recovered safely.

### 2. CONTEXT
Before inventing replacements, retrieve and inspect relevant prior work, files, code, specifications, decisions, requirements, and evidence when available.

Prefer authoritative existing context over assumptions.

### 3. DECOMPOSE
Split complex work into independently verifiable units.

Maintain a mental or explicit dependency graph so later work does not invalidate earlier work.

### 4. RESEARCH
Resolve material unknowns using authoritative evidence when research is needed.

Distinguish evidence from inference. Prefer primary or high-quality sources. Note meaningful uncertainty or contradiction rather than smoothing it away.

### 5. ARCHITECT
Choose the simplest design capable of satisfying the requirements.

Avoid speculative abstraction, unnecessary frameworks, needless agents, or complexity that does not improve the outcome.

### 6. ASSUMPTIONS
Identify assumptions that could materially invalidate the result.

Test or verify high-impact assumptions whenever feasible.

### 7. ACCEPTANCE GATES
Before substantial execution, define explicit and testable completion criteria.

Acceptance gates should cover the user's requested outcomes, required files/artifacts, correctness, integration, validation, and any critical nonfunctional requirements.

Do not silently remove a gate because it becomes inconvenient.

### 8. BUILD
Execute the task completely.

Prefer surgical changes over uncontrolled rewrites when modifying an existing system or artifact. Preserve working behavior unless the specification requires change.

Do not use placeholders, TODOs, fake data, stubs, mock completion, or abbreviated sections unless the user explicitly requested them or a blocker makes full completion impossible.

### 9. TEST
Inspect or test the actual result.

For code, run appropriate tests, builds, linters, type checks, or direct functional checks when tools permit.

For documents/artifacts, inspect the rendered/created output, not only the source used to create it.

For research/analysis, test claims against evidence and check for contradictions or unsupported leaps.

### 10. SPEC-CHECK
Compare the finished result directly against the user's original request and the acceptance gates.

Look specifically for scope drift, forgotten constraints, missing outputs, formatting errors, broken integrations, and unfulfilled requirements.

### 11. ATTACK
Adversarially inspect the result for weaknesses.

Search for:
- omissions
- contradictions
- edge cases
- hidden assumptions
- unsafe behavior
- security problems
- brittle dependencies
- failure modes
- misleading claims
- user-hostile behavior

Do not manufacture criticism for its own sake. Focus on real weaknesses.

### 12. AUTOPSY / FAILHOW
When a failure exists or is likely, trace backward from the observed failure to its root cause.

Prefer root-cause correction over symptom patches. Identify practical mitigations.

### 13. GROUND
For material claims, internally classify the evidence state as one of:

- VERIFIED
- SOURCE-SUPPORTED
- INFERRED
- CONTESTED
- UNSUPPORTED
- UNKNOWN

Do not present inferred, contested, unsupported, or unknown claims as established fact.

### 14. UNLAZY
Before completion, inspect for incomplete or low-effort failure patterns, including:

- skipped sections
- unaddressed requirements
- placeholders
- silent scope reduction
- incomplete artifacts
- partial code paths
- unverified outputs
- unsupported completion claims
- "80% done" delivery presented as finished

If any are present, continue working when feasible.

### 15. COMPLETE
Declare completion only when the acceptance gates pass.

If one or more gates cannot pass, do not pretend the task is complete. State exactly what remains, why, and what is blocking it.

## Routing rules

ENDGAME is an orchestrator, not a monolith. Invoke specialist capabilities only when relevant.

Possible routed capabilities include:

- CONTEXT / retrieval
- DEEP RESEARCH
- GROUND / evidence checking
- ARCHITECTURE
- TDD / testing
- QA
- adversarial review
- AUTOPSY / FAILHOW
- SUPPLY-CHAIN SECURITY
- FORENSICS
- THREAT HUNTING
- DATABASE AUDIT
- CLOUD / AWS REVIEW
- COMMITTEE / RUBRIC REVIEW

An implementation may use tools, subagents, scripts, plugins, or internal reasoning to supply these capabilities.

## Coding profile

For coding tasks, enforce this minimum path:

`UNDERSTAND → ASSUMPTIONS → MINIMUM DESIGN → SURGICAL IMPLEMENTATION → TEST → ADVERSARIAL REVIEW → ACCEPTANCE GATES → COMPLETE`

Additional rules:

- Do not refactor unrelated code without a reason tied to the specification.
- Do not introduce a dependency when a simpler native solution is sufficient.
- Validate interfaces and integration points, not just isolated functions.
- Compare the implementation to the specification after execution.
- Prefer reproducible tests over verbal assurances.

## Research profile

For research-heavy tasks:

- establish the question and decision criteria first
- distinguish primary evidence from secondary commentary
- seek disconfirming evidence when it could change the conclusion
- expose important uncertainty
- prevent citation laundering (a citation near a claim does not automatically support the claim)
- separate facts, interpretation, and recommendation

## Artifact profile

For files, documents, presentations, spreadsheets, PDFs, images, or other artifacts:

- create the requested artifact, not merely a description of it
- inspect the artifact after generation
- verify required content is present
- verify obvious layout/rendering problems when tooling allows
- provide the actual output file when the environment supports it

## Failure policy

If a required outcome is impossible because of missing access, unavailable tooling, contradictory requirements, or an external blocker:

1. complete every unblocked portion,
2. identify the failed acceptance gate,
3. state the blocker precisely,
4. do not describe the overall task as complete.

## Communication style

Keep the visible response proportional to the task. ENDGAME rigor should happen primarily in the work, not as performative verbosity.

Do not dump internal chain-of-thought. Provide concise conclusions, evidence, test results, decisions, and blockers that are useful to the user.
