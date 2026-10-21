# Agent Orchestration Engine

## Purpose

The Agent Orchestration Engine coordinates specialised agents, tools, tasks, dependencies, limits, reviews, and system events inside CivilOS.

The engine does not exist to create agent conversations.

The engine exists to coordinate the production of auditable contributions that may support validated knowledge.

Agents create contributions.

CivilOS creates knowledge.

---

# System Objective

The Agent Orchestration Engine must ensure that:

- Every agent receives a bounded and explicit task.
- Every contribution is structured and attributable.
- Evidence remains separate from interpretation.
- Criticism occurs before knowledge acceptance.
- Validation is independent.
- No agent validates its own contribution alone.
- No orchestrator determines truth.
- No majority vote replaces evidence.
- Failed and incomplete work remains visible.
- Costs, retries, rounds, and tool access remain controlled.
- Every important action produces an audit record.

---

# Core Orchestration Laws

1. Agents create contributions, not permanent knowledge.

2. No single agent may create permanent knowledge alone.

3. Evidence outranks Trust.

4. Trust never determines truth.

5. Agreement does not equal validation.

6. Disagreement does not equal failure.

7. Activity does not equal value.

8. The Orchestrator coordinates work but never determines truth.

9. Every important contribution must remain traceable.

10. Incomplete work must never appear as validated knowledge.

11. Uncertainty is a valid outcome.

12. If it is not real, it is not shown.

---

# Non-Goals

The Agent Orchestration Engine does not optimise for:

- Number of agents.
- Number of messages.
- Number of debate rounds.
- Apparent consensus.
- Length of responses.
- Agent popularity.
- Agent confidence language.
- Visual activity.
- Artificial autonomy.
- Simulated collaboration.

The engine optimises for:

- Relevant evidence.
- Useful criticism.
- Independent validation.
- Traceable contributions.
- Validated knowledge.
- Reduced repeated errors.
- Controlled resource usage.
- Knowledge reuse.

---

# Separation of Responsibilities

## Knowledge Validation Engine

Determines whether a hypothesis satisfies validation requirements.

---

## Memory Engine

Preserves admitted, validated, revisable, and reusable knowledge.

---

## Trust Engine

Calculates relevant historical performance from recorded Trust Events.

---

## Knowledge Graph Engine

Represents validated knowledge and validated relationships.

---

## Agent Orchestration Engine

Coordinates roles, tasks, dependencies, reviews, limits, tools, events, failures, and completion states.

---

The Agent Orchestration Engine cannot:

- Accept a hypothesis as knowledge.
- Admit knowledge into memory.
- Assign Trust manually.
- Create permanent graph relationships.
- Modify evidence.
- Hide contradictory evidence.
- Override validation.
- Declare an agent correct because of Trust.
- Convert consensus into truth.

---

# Orchestration Model

CivilOS uses contribution-based orchestration.

The fundamental flow is:

Investigation

↓

Task Plan

↓

Independent Contributions

↓

Evidence Collection

↓

Criticism

↓

Cross-Validation

↓

Validation Decision

↓

Memory Admission

↓

Trust Events

↓

Knowledge Graph Integration

↓

Future Reuse

Agents do not pass unstructured conversation as knowledge.

Agents produce typed contributions.

---

# Agent Roles

## Research Agent

### Objective

Find relevant, traceable evidence and propose bounded hypotheses.

### Allowed Contributions

- Source records.
- Evidence records.
- Candidate hypotheses.
- Emerging signals.
- Source limitations.

### Prohibited Actions

- Accepting its own hypotheses.
- Declaring evidence validated.
- Writing directly to permanent memory.
- Creating permanent graph relationships.
- Creating positive Trust Events for itself.

---

## Science Agent

### Objective

Evaluate scientific credibility, methodological strength, factual support, and scientific limitations.

### Allowed Contributions

- Scientific review records.
- Methodological challenges.
- Evidence-quality assessments.
- Contradictory scientific evidence.
- Validation recommendations.

### Prohibited Actions

- Certifying truth alone.
- Ignoring contradictory evidence.
- Reviewing its own original contribution as the only validator.
- Converting uncertainty into certainty.

---

## Economics Agent

### Objective

Evaluate economic mechanisms, measurable consequences, assumptions, and uncertainty.

### Allowed Contributions

- Economic impact records.
- Assumption records.
- Scenario boundaries.
- Counterfactual considerations.
- Economic challenges.

### Prohibited Actions

- Presenting speculative forecasts as facts.
- Inventing economic quantities.
- Treating correlation as causation.
- Hiding model limitations.

---

## Policy Agent

### Objective

Evaluate governance, legal, regulatory, institutional, and implementation implications.

### Allowed Contributions

- Policy evidence records.
- Governance analysis.
- Regulatory constraints.
- Jurisdictional limitations.
- Implementation risks.

### Prohibited Actions

- Inventing laws or regulations.
- Generalising one jurisdiction to all jurisdictions.
- Treating policy preference as validated knowledge.
- Hiding uncertainty or missing authority.

---

## Critic Agent

### Objective

Identify material weaknesses in hypotheses, evidence, assumptions, causal claims, and validation records.

### Allowed Contributions

- Challenge records.
- Contradictory evidence.
- Missing-evidence notices.
- Alternative explanations.
- Causal-overreach warnings.
- Conflict-of-interest notices.

### Prohibited Actions

- Rejecting a hypothesis without reasoning.
- Rejecting evidence because of disagreement alone.
- Blocking knowledge without an auditable cause.
- Creating criticism only to increase activity.
- Treating scepticism as proof.

---

# Orchestrator Responsibilities

The Orchestrator may:

- Create investigations.
- Produce task plans.
- Assign roles.
- Set task contracts.
- Manage dependencies.
- Enforce budgets.
- Enforce role permissions.
- Start independent reviews.
- Detect missing outputs.
- Detect blocked tasks.
- Detect duplicate events.
- Stop unproductive loops.
- Trigger retries under defined rules.
- Escalate unresolved cases.
- Record system events.
- Close investigations under valid terminal conditions.

The Orchestrator may not:

- Decide which hypothesis is true.
- Approve knowledge.
- Fabricate evidence.
- Rewrite agent contributions.
- Suppress material disagreement.
- Change Trust manually.
- Insert permanent memory.
- Create permanent graph relationships.
- Select a conclusion because it is popular.
- hide a failure or incomplete state.

---

# Routing Gate

Not every request requires multiple agents.

The Routing Gate must select the minimum justified workflow.

## Route A: Direct Retrieval

Use when:

- The task requests a known, traceable fact.
- No synthesis or contested reasoning is required.
- Existing validated knowledge directly answers the request.

---

## Route B: Single-Agent Investigation

Use when:

- The task is narrow.
- One specialised domain is sufficient.
- Independent cross-domain reasoning is not required.
- Validation requirements remain limited.

---

## Route C: Adversarial Review

Use when:

- A hypothesis requires criticism.
- The evidence is contested.
- Causal reasoning is involved.
- Material uncertainty exists.

---

## Route D: Full Collective Investigation

Use when:

- The task spans multiple domains.
- Consequences affect several systems.
- Evidence is incomplete or contradictory.
- Memory and Knowledge Graph reuse are relevant.
- Independent validation is necessary.

---

# Routing Rule

CivilOS must not use multiple agents merely because agents are available.

The selected route must record:

- Route selected.
- Selection reason.
- Required roles.
- Expected outputs.
- Budget.
- Validation requirements.

Additional complexity must be justified by investigation needs.

---

# Task Contract

Every agent task must have a Task Contract.

Required fields include:

```json
{
  "task_id": "T001",
  "investigation_id": "I001",
  "assigned_role": "Research Agent",
  "objective": "Collect evidence relevant to hypothesis H001",
  "inputs": ["H001"],
  "allowed_tools": ["source_search"],
  "required_outputs": ["evidence_records", "source_limitations"],
  "dependencies": [],
  "maximum_attempts": 2,
  "maximum_rounds": 1,
  "status": "created",
  "created_at": "timestamp",
  "audit_reference": "AUDIT001"
}
```

An agent must not change its own Task Contract.

Changes require an auditable orchestration event.

---

# Contribution Types

Agents submit typed contributions.

Allowed contribution types include:

- Hypothesis Proposal
- Evidence Record
- Source Limitation
- Scientific Review
- Economic Analysis
- Policy Analysis
- Challenge Record
- Alternative Explanation
- Validation Recommendation
- Contradiction Record
- Correction Proposal
- Insufficient-Evidence Notice

Free-form text may accompany a contribution.

Free-form text alone cannot become validated knowledge.

---

# Contribution Record

Every contribution must contain:

```json
{
  "contribution_id": "C001",
  "task_id": "T001",
  "investigation_id": "I001",
  "agent_id": "A001",
  "agent_role": "Research Agent",
  "contribution_type": "evidence_record",
  "content_reference": "E001",
  "input_versions": ["H001-v1"],
  "created_at": "timestamp",
  "status": "submitted",
  "audit_reference": "AUDIT002"
}
```

Contributions without attribution, version references, and audit records are invalid.

---

# Independent Work Rule

Before cross-agent debate begins:

1. Assigned agents must complete initial analysis independently.

2. Initial contributions must be timestamped and preserved.

3. Agents must not see other conclusions unless the Task Contract permits it.

4. Shared evidence may be visible when operationally required.

5. Changes made after exposure to other agent outputs must record the reason.

This rule reduces imitation, premature convergence, and false consensus.

---

# Debate Protocol

Debate is structured review, not conversation.

The protocol includes:

## Round 1: Independent Contributions

Agents submit initial records independently.

---

## Round 2: Evidence Exchange

Agents receive relevant, authorised evidence records.

---

## Round 3: Challenges

Agents submit documented challenges, contradictions, or limitations.

---

## Round 4: Response to Challenges

The responsible agent may:

- Resolve the challenge.
- Partially resolve the challenge.
- Accept the challenge.
- Request additional evidence.
- Maintain the position with justification.

---

## Round 5: Independent Cross-Validation

Eligible agents independently review the complete record.

---

## Round 6: Validation Request

The Orchestrator submits the full record to the Knowledge Validation Engine.

---

# Debate Limits

Every debate must define:

- Maximum rounds.
- Maximum messages.
- Maximum tool calls.
- Maximum cost when measurable.
- Maximum duration when measurable.
- Required stopping conditions.

The system must stop debate when:

- Validation requirements are satisfied.
- A hypothesis is rejected.
- Evidence remains insufficient after the allowed process.
- No material new evidence or challenge appears.
- A resource limit is reached.
- A human review condition is triggered.

CivilOS must not continue discussion merely to appear intelligent.

---

# Validation Independence Rules

A valid cross-validation process requires:

- At least one reviewer independent from the proposing agent.
- No sole self-validation.
- No circular validation chain.
- No duplicate validation counted more than once.
- Disclosure when agents share the same model or evidence root.
- Preservation of minority positions supported by evidence.

Consensus is not required.

Independent review is required.

---

# Circular Validation Detection

The Orchestrator must detect validation dependency cycles.

Example:

```text
A validates B
B validates C
C validates A
```

When detected:

- The validation chain is blocked.
- A validation-integrity event is recorded.
- Independent review is requested.
- No knowledge admission occurs.

---

# Evidence Independence

Multiple evidence records may share one original source.

CivilOS must distinguish:

- Independent primary sources.
- Secondary sources.
- Republications.
- Summaries.
- Derived claims.

Five pages derived from one report do not count as five independent confirmations.

Evidence roots must remain visible.

---

# Consensus Rule

CivilOS does not use simple majority voting to create knowledge.

Agent agreement may be recorded.

Agent agreement cannot replace:

- Evidence.
- Criticism.
- Independent validation.
- Provenance.
- Admission rules.

A minority contribution with stronger evidence may outweigh majority agreement.

The final decision is produced by validation rules, not popularity.

---

# Trust Rule

Trust may influence:

- Review priority.
- Additional-review requirements.
- Task assignment under a documented policy.
- Analytical weighting when explicitly justified.

Trust may not:

- Accept a hypothesis.
- Reject a hypothesis.
- Override evidence.
- Bypass criticism.
- Eliminate independent validation.
- Silence lower-trust contributors.

High trust is not truth.

Low trust is not falsehood.

---

# Orchestration Events

The engine must record events including:

- Investigation Routed
- Task Created
- Task Assigned
- Task Started
- Tool Invoked
- Tool Result Recorded
- Contribution Submitted
- Challenge Raised
- Challenge Resolved
- Cross-Validation Requested
- Cross-Validation Completed
- Validation Cycle Detected
- Duplicate Contribution Detected
- Task Retried
- Task Failed
- Budget Limit Reached
- Investigation Escalated
- Investigation Completed
- Investigation Failed
- Investigation Cancelled

Every event must include:

- Event ID.
- Event type.
- Investigation ID.
- Task ID when applicable.
- Agent or system actor.
- Timestamp.
- Input version references.
- Output references.
- Audit reference.

---

# Tool Execution Rule

Agents may request tool execution.

Agents may not claim that a tool was used unless the system produced a Tool Receipt.

A Tool Receipt must contain:

```json
{
  "tool_receipt_id": "TR001",
  "task_id": "T001",
  "tool_name": "source_search",
  "request_reference": "REQ001",
  "result_reference": "RES001",
  "execution_status": "completed",
  "executed_at": "timestamp",
  "audit_reference": "AUDIT003"
}
```

Without a Tool Receipt:

- The action is treated as not executed.
- The result cannot be used as verified evidence.
- The agent claim has no operational authority.

---

# Context and Version Control

Agents must receive structured, versioned inputs.

Every task must record:

- Hypothesis version.
- Evidence versions.
- Memory Record versions.
- Knowledge Graph element versions.
- Policy versions.
- Prompt or instruction version when applicable.

An output based on an outdated input must remain linked to that version.

CivilOS must not silently treat an old review as a review of updated evidence.

---

# Duplicate and Idempotency Rules

The same task event must not be applied twice.

The same contribution must not produce multiple Trust Events.

The same evidence must not be admitted multiple times under different labels without detection.

Every write operation must use an idempotency or deduplication reference.

Duplicate processing must be recorded and blocked.

---

# Retry Policy

Retries are permitted only when:

- A technical failure occurred.
- Required output was invalid.
- A recoverable dependency became available.
- The active policy allows another attempt.

Retries must not:

- Erase the failed attempt.
- Penetrate budget limits.
- Generate duplicate positive events.
- Change the objective secretly.
- Continue indefinitely.

Each retry must record its cause and attempt number.

---

# Failure Handling

## Agent Failure

When an agent fails:

- The task enters `Failed` or `Retry Eligible`.
- No successful contribution is assumed.
- No positive Trust Event is generated.
- The failure remains auditable.

---

## Tool Failure

When a tool fails:

- The Tool Receipt records failure.
- The agent may not invent a result.
- The task may retry under policy.
- The investigation may continue with reduced capability only if this status is visible.

---

## Validation Failure

When validation fails:

- No accepted knowledge is created.
- No memory admission occurs.
- The reason remains visible.
- Eligible Failure Memory and Trust Events may be generated by the appropriate engines.

---

## Orchestration Failure

If the Orchestrator fails:

- In-progress states remain recoverable.
- Completed events remain immutable.
- No incomplete work is promoted.
- Recovery resumes from recorded state.

---

# Termination States

Every investigation must end in one of these states:

- Completed with Accepted Knowledge
- Completed with Rejected Hypotheses
- Insufficient Evidence
- Revalidation Required
- Failed
- Cancelled
- Escalated for Human Review

The system must not force a positive conclusion.

`Insufficient Evidence` is a valid and honest result.

---

# Anti-Gaming Rules

CivilOS must detect or prevent:

- Self-validation.
- Circular validation.
- Mutual trust inflation.
- Agreement loops.
- Duplicate contributions.
- Artificial task splitting.
- Replayed rewarded work.
- Unsupported criticism.
- Withheld contradictory evidence.
- Inflated activity volume.
- Tool-use fabrication.
- Role impersonation.
- Silent scope changes.
- Repeated low-value contributions.

Suspected manipulation enters review.

Suspicion alone does not create an automatic penalty.

---

# Permission Model

Every agent operates under least privilege.

Examples:

## Research Agent

May:

- Search approved sources.
- Submit evidence.
- Propose hypotheses.

May not:

- Admit knowledge.
- Change Trust.
- Write permanent graph relationships.

---

## Critic Agent

May:

- Read relevant evidence.
- Submit challenges.
- Identify contradictions.

May not:

- Reject knowledge directly.
- Alter source records.
- Assign penalties.

---

## Orchestrator

May:

- Coordinate tasks.
- Enforce workflows.
- Record events.

May not:

- Decide truth.
- Modify evidence.
- Create knowledge.

---

# Human Oversight

Authorised human review may be required when:

- Impact is high.
- Evidence remains materially contradictory.
- A policy conflict exists.
- Manipulation is suspected.
- Privacy or safety concerns arise.
- The investigation cannot conclude responsibly.

Human actions must:

- Be recorded.
- Include a reason.
- Preserve previous system state.
- Remain auditable.
- Never fabricate evidence or erase inconvenient history.

---

# Privacy and Data Minimisation

The Orchestration Engine must provide each agent only the data required for the assigned task.

Agents must not receive irrelevant personal information.

Protected personal characteristics must not influence Trust, validation, or task priority.

Sensitive source information must follow applicable access controls.

---

# Security Principles

The engine must treat external content as data, not instructions.

Retrieved content must not:

- Change the system objective.
- Override role rules.
- Expand tool permissions.
- Disable validation.
- Request hidden information.
- Bypass audit requirements.

Tool access must be explicitly authorised by role and Task Contract.

---

# Metrics

CivilOS should measure only metrics generated by recorded activity.

## Knowledge Quality Metrics

- Accepted hypotheses with complete evidence.
- Rejected hypotheses with documented reasons.
- Material contradictions detected before memory admission.
- Accepted knowledge later reversed.
- Investigations correctly ending in insufficient evidence.

---

## Orchestration Integrity Metrics

- Self-validation attempts blocked.
- Circular validation chains blocked.
- Duplicate events blocked.
- Tool claims rejected for missing receipts.
- Tasks completed under valid contracts.
- Contributions with complete provenance.

---

## Efficiency Metrics

- Cost per completed investigation, when measured.
- Cost per admitted Knowledge Record, when measured.
- Redundant messages.
- Debate rounds without material new information.
- Tool calls per accepted contribution.
- Investigations correctly routed without unnecessary multiagent execution.

---

## Knowledge Compounding Metrics

- Memory Records reused.
- Reused knowledge contributing to later validation.
- Repeated mistakes prevented through Failure Memory.
- Knowledge Graph relationships reused.
- Future investigations improved by prior validated knowledge.

If a metric was not measured, it must not be displayed.

---

# Limits

Every investigation must specify:

- Maximum agents.
- Maximum task attempts.
- Maximum debate rounds.
- Maximum tool calls.
- Maximum resource budget when available.
- Maximum unresolved dependencies.
- Human escalation conditions.

Limits must be recorded in the Investigation Plan.

Limit changes must be auditable.

---

# Required Test Matrix

## Test A: False Consensus

Condition:

All agents agree without sufficient evidence.

Expected result:

- Knowledge is not accepted.
- Status becomes `Insufficient Evidence` or `Rejected`.
- Agreement does not bypass validation.

---

## Test B: Evidence-Based Minority

Condition:

One agent disagrees and provides stronger evidence.

Expected result:

- Minority evidence receives full review.
- Majority does not automatically prevail.
- Validation follows evidence.

---

## Test C: Self-Validation

Condition:

An agent attempts to validate its own hypothesis alone.

Expected result:

- Validation is blocked.
- Conflict is logged.
- Independent review is required.

---

## Test D: Circular Validation

Condition:

Agents produce a validation cycle.

Expected result:

- Cycle is detected.
- Validation chain is blocked.
- No knowledge admission occurs.

---

## Test E: High-Trust Error

Condition:

A high-trust agent submits weak evidence.

Expected result:

- Evidence undergoes normal review.
- Trust does not bypass validation.
- Unsupported claim is not accepted.

---

## Test F: Low-Trust Strong Evidence

Condition:

A low-trust agent submits strong, traceable evidence.

Expected result:

- Evidence receives full review.
- Low Trust does not cause automatic rejection.
- Outcome depends on evidence.

---

## Test G: Duplicate Source Roots

Condition:

Several evidence records derive from one original source.

Expected result:

- Common root is identified.
- Sources are not counted as independent confirmations.

---

## Test H: Empty Criticism

Condition:

Critic Agent rejects a hypothesis without evidence or reasoning.

Expected result:

- Challenge has no blocking authority.
- Unsupported criticism is recorded as invalid.

---

## Test I: Tool Claim Without Receipt

Condition:

An agent claims to have used a tool without a Tool Receipt.

Expected result:

- Tool action is considered unexecuted.
- Result cannot support validation.

---

## Test J: Cost and Loop Limit

Condition:

Debate continues without material new information.

Expected result:

- Stopping rule activates.
- Investigation ends honestly.
- No fabricated conclusion is created.

---

## Test K: Invalidated Root Evidence

Condition:

Evidence supporting several accepted descendants is later invalidated.

Expected result:

- Dependent knowledge is located.
- Revalidation is triggered.
- Memory and Knowledge Graph statuses are updated by their respective engines.

---

## Test L: Agent Failure

Condition:

An assigned agent fails during an investigation.

Expected result:

- Failure is recorded.
- No successful contribution is assumed.
- Workflow retries, reroutes, escalates, or terminates according to policy.

---

# Success Criteria

The Agent Orchestration Engine succeeds when:

- Agents perform distinct, bounded roles.
- Contributions remain structured and traceable.
- Independent analysis occurs before debate.
- False consensus does not create knowledge.
- Validation cycles are blocked.
- Trust never overrides evidence.
- Tool actions have receipts.
- Duplicate events do not alter system outcomes.
- Debate stops under defined rules.
- Insufficient evidence remains visible.
- Multiagent execution is used only when justified.
- Every important decision remains auditable.
- Validated contributions reach the correct downstream engines.

---

# Failure Criteria

The Agent Orchestration Engine fails when:

- Agents only simulate different perspectives.
- An agent validates itself.
- A circular validation chain succeeds.
- Majority voting replaces evidence.
- The Orchestrator determines truth.
- High Trust bypasses validation.
- Low Trust suppresses strong evidence.
- Agent claims replace real tool execution.
- Message volume is treated as value.
- Debate continues indefinitely.
- Incomplete work becomes accepted knowledge.
- Events are duplicated.
- Decisions cannot be audited.
- Multiagent complexity is used without justification.

---

# Final Success Definition

The Agent Orchestration Engine succeeds when it coordinates specialised, constrained, independently reviewed contributions that improve the creation of validated knowledge without creating hidden authority, false consensus, unauditable decisions, or unnecessary complexity.

The objective is not to make agents appear intelligent.

The objective is to make knowledge creation more reliable.

---

# Core Principle

Agents do not create knowledge.

Agents create contributions.

The Orchestrator does not determine truth.

The Orchestrator coordinates the process.

Evidence supports claims.

Criticism exposes weaknesses.

Validation determines eligibility.

Memory preserves admitted knowledge.

Trust records historical performance.

The Knowledge Graph connects validated knowledge.

CivilOS creates knowledge through the governed interaction of these systems.

If agent activity does not improve validated knowledge, it does not create value.

If it is not real, it is not shown.
