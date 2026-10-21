# CivilOS System Flow

## Purpose

This document defines the end-to-end operational flow of CivilOS.

It describes how a user question becomes an investigation, how hypotheses are evaluated, how validated knowledge is admitted into memory, and how prior knowledge improves future investigations.

CivilOS is not a response-generation pipeline.

CivilOS is a knowledge-validation and knowledge-compounding system.

---

# System Objective

CivilOS must transform uncertain claims into auditable knowledge through:

Question

↓

Investigation

↓

Hypotheses

↓

Evidence

↓

Criticism

↓

Cross-Validation

↓

Validation Decision

↓

Memory Admission

↓

Knowledge Graph Integration

↓

Future Reuse

↓

Knowledge Compounding

Every transition must produce a traceable record.

No stage may fabricate an outcome, metric, source, or status.

---

# Core System Laws

1. If it is not real, it is not shown.

2. No evidence, no knowledge.

3. No validation, no memory.

4. Trust is earned through recorded outcomes.

5. No single agent can create permanent knowledge alone.

6. Every accepted claim must remain traceable to evidence.

7. Knowledge remains open to challenge, revision, and deprecation.

8. An incomplete investigation must never appear as validated knowledge.

---

# Core Artifacts

CivilOS processes the following artifacts.

## Investigation

Represents the complete examination of a user question.

Required fields:

- Investigation ID
- User question
- Creation timestamp
- Current status
- Participating agents
- Related hypotheses
- Final outcome

---

## Hypothesis

Represents a claim proposed for evaluation.

Required fields:

- Hypothesis ID
- Investigation ID
- Statement
- Proposing agent
- Current state
- Evidence references
- Challenge references
- Validation references

A hypothesis is not knowledge.

---

## Evidence Record

Represents information that supports, weakens, or contradicts a hypothesis.

Required fields:

- Evidence ID
- Hypothesis ID
- Source title
- Source publisher or organisation
- Source location
- Publication date when available
- Retrieval timestamp
- Evidence position
- Validation status

Evidence position must be one of:

- Supporting
- Contradicting
- Contextual

---

## Challenge Record

Represents a documented objection or alternative explanation.

Required fields:

- Challenge ID
- Hypothesis ID
- Challenging agent
- Challenge statement
- Supporting evidence references
- Resolution status

A challenge without reasoning or evidence cannot automatically reject a hypothesis.

---

## Validation Decision

Represents the auditable outcome of hypothesis review.

Required fields:

- Validation ID
- Hypothesis ID
- Decision
- Decision reasons
- Evidence references
- Challenge references
- Validating agents
- Timestamp

Decision must be one of:

- Accepted
- Rejected
- Insufficient Evidence
- Revalidation Required

---

## Knowledge Record

Represents validated knowledge admitted into CivilOS memory.

Required fields:

- Knowledge ID
- Source hypothesis ID
- Source validation ID
- Content
- Knowledge type
- Current status
- Evidence references
- Revision history
- Creation timestamp

A Knowledge Record cannot exist without a successful validation decision and Memory Admission Gate approval.

---

# Investigation States

Every investigation must have one current state.

Allowed states:

- Created
- Investigating
- Under Review
- Completed
- Failed
- Cancelled

A failed, cancelled, or incomplete investigation cannot produce accepted knowledge.

---

# Hypothesis States

Every hypothesis must have one current state.

Allowed states:

- Proposed
- Investigating
- Challenged
- Supported
- Cross-Validated
- Accepted
- Rejected
- Insufficient Evidence
- Revalidation Required

State changes must be recorded.

Silent state changes are not allowed.

---

# Stage 1: Question Intake

## Input

- User question

## Process

CivilOS creates an Investigation Record.

The original question must be preserved without alteration.

## Output

- Investigation ID
- Investigation status: Created

## Failure Condition

The investigation cannot begin if the question is missing or cannot be stored.

---

# Stage 2: Investigation Planning

## Process

CivilOS identifies:

- Required domains
- Required evidence types
- Participating agent roles
- Known memory relevant to the question
- Initial validation requirements

Retrieved memory is treated as prior knowledge, not automatic truth.

Existing knowledge remains subject to relevance and status checks.

## Output

- Investigation plan
- Agent assignments
- Relevant memory references

---

# Stage 3: Hypothesis Creation

## Process

One or more agents propose hypotheses.

Each hypothesis must be stored separately.

The system must not require a fabricated minimum or maximum number of hypotheses.

## Output

- Hypothesis Records
- Hypothesis status: Proposed

## Rule

Agents may propose hypotheses.

Agents may not declare their own hypotheses to be permanent knowledge.

---

# Stage 4: Evidence Collection

## Process

Agents collect evidence supporting, contradicting, or contextualising each hypothesis.

Every evidence item must retain source provenance.

## Output

- Evidence Records
- Updated hypothesis status: Investigating

## Failure Conditions

Evidence must not be admitted when:

- The source cannot be identified.
- The evidence cannot be traced.
- The evidence is fabricated.
- The evidence has no relationship to the hypothesis.

---

# Stage 5: Evidence Review

## Process

Evidence is evaluated for:

- Traceability
- Relevance
- Verifiability
- Source identity
- Relationship to the hypothesis
- Supporting or contradicting position

## Possible Outcomes

- Validated
- Rejected
- Unresolved

## Rule

An unresolved source may remain attached for review, but it cannot support acceptance.

---

# Stage 6: Criticism

## Process

The Critic Agent and other applicable agents examine:

- Unsupported assumptions
- Missing evidence
- Logical weaknesses
- Contradictions
- Alternative explanations
- Causal overreach

## Output

- Challenge Records
- Updated hypothesis status: Challenged

## Rule

Criticism must be documented.

Unsupported criticism has no authority.

---

# Stage 7: Cross-Validation

## Process

Multiple agents independently review the hypothesis, evidence, and challenges.

Cross-validation must record:

- Reviewing agent
- Evidence examined
- Challenges examined
- Decision
- Reasoning summary

## Rule

Cross-validation is not simple agreement.

Agreement without independent review does not count as validation.

---

# Stage 8: Validation Decision

The Knowledge Validation Engine evaluates the complete record.

## Acceptance Requirements

A hypothesis may be accepted only when:

- Supporting evidence exists.
- Required evidence is validated.
- Sources are traceable.
- Material contradictions are addressed.
- Required criticism occurred.
- Multiple agents completed independent validation.
- The reasoning trail is complete.

## Rejection Conditions

A hypothesis must be rejected when:

- Evidence is missing or invalid.
- The claim is contradicted by stronger validated evidence.
- Critical weaknesses remain unresolved.
- Required provenance is unavailable.
- Validation rules fail.

## Insufficient Evidence

A hypothesis receives `Insufficient Evidence` when the available material cannot responsibly support acceptance or rejection.

Insufficient evidence is not acceptance.

Insufficient evidence is not failure.

## Revalidation Required

A previously accepted hypothesis receives `Revalidation Required` when new evidence creates a material challenge.

---

# Validation Branches

## Accepted Branch

Accepted Hypothesis

↓

Memory Admission Gate

↓

Knowledge Record

↓

Trust Events

↓

Knowledge Graph Integration

↓

Future Reuse

---

## Rejected Branch

Rejected Hypothesis

↓

Failure Memory Candidate

↓

Trust Events

↓

Historical Record

Rejected hypotheses do not become accepted knowledge.

---

## Insufficient Evidence Branch

Insufficient Evidence

↓

Pending Investigation Record

↓

Future Evidence Collection

No permanent knowledge is created.

---

## Revalidation Branch

Existing Knowledge

↓

New Contradictory Evidence

↓

Challenge

↓

Revalidation

↓

Active, Updated, Challenged, or Deprecated

Knowledge is never silently overwritten.

---

# Stage 9: Memory Admission Gate

Acceptance by the Knowledge Validation Engine makes a hypothesis eligible for memory.

It does not bypass the Memory Admission Gate.

## Admission Checks

The Memory Admission Gate verifies:

- Validation decision exists.
- Evidence references remain available.
- Required provenance is complete.
- Knowledge type is identified.
- No unresolved blocking condition exists.
- Duplicate or conflicting knowledge is detected.

## Outcomes

- Admitted
- Rejected from Memory
- Merge Required
- Revalidation Required

## Rule

No direct agent output may enter permanent memory.

---

# Stage 10: Memory Integration

Admitted knowledge is classified as:

- Fact Memory
- Discovery Memory
- Failure Memory
- Strategy Memory

Memory preserves:

- Knowledge content
- Evidence provenance
- Validation history
- Revision history
- Current status

Memory does not create truth.

Memory preserves validated and revisable knowledge.

---

# Stage 11: Trust Events

Recorded system outcomes generate Trust Events.

Examples include:

- Validated Evidence Contribution
- Accepted Knowledge Contribution
- Successful Cross-Validation
- Useful Criticism
- Rejected Evidence Submission
- Unsupported Claim
- Failed Validation
- Repeated Critical Error

## Rule

The Trust Engine consumes recorded events.

The Trust Engine does not decide whether a claim is true.

High trust does not bypass evidence, criticism, or validation.

---

# Stage 12: Knowledge Graph Integration

The Knowledge Graph Engine represents validated knowledge and relationships.

## Possible Additions

- Knowledge nodes
- Evidence nodes
- Concept nodes
- Validated relationships
- Contradiction relationships
- Revision relationships

## Admission Rule

A graph relationship must include:

- Source knowledge references
- Evidence references
- Validation status
- Creation history

The Knowledge Graph does not invent relationships.

The Knowledge Graph represents validated relationships.

---

# Stage 13: Result Delivery

CivilOS may present:

- Current conclusion
- Validation status
- Supporting evidence
- Counterarguments
- Rejected hypotheses
- Agent contributions
- Memory actions
- Knowledge Graph actions
- Audit references

## Display Rule

Only recorded system activity may be displayed.

If a metric was not calculated, it must not be shown.

If evidence is unresolved, the unresolved status must remain visible.

---

# Stage 14: Future Reuse

Future investigations may retrieve active, relevant, and validated knowledge.

Retrieved knowledge must include:

- Current status
- Evidence references
- Validation history
- Revision history
- Contradiction links

## Rule

Retrieved knowledge supports future reasoning.

Retrieved knowledge does not bypass new investigation requirements.

---

# Stage 15: Knowledge Compounding

CivilOS creates compounding value when:

- Validated knowledge is reused.
- Future investigations require less repeated work.
- Previous failures prevent repeated mistakes.
- Earlier discoveries support new validated relationships.
- Knowledge remains current through revision.

Knowledge compounding must be measured from recorded reuse events.

It must not be assumed.

---

# Event Model

CivilOS should record events such as:

- Investigation Created
- Hypothesis Proposed
- Evidence Added
- Evidence Validated
- Evidence Rejected
- Challenge Raised
- Cross-Validation Completed
- Hypothesis Accepted
- Hypothesis Rejected
- Insufficient Evidence Recorded
- Revalidation Requested
- Memory Admission Approved
- Memory Admission Rejected
- Knowledge Updated
- Knowledge Deprecated
- Trust Event Created
- Graph Relationship Added
- Knowledge Reused

Every event must include:

- Event ID
- Event type
- Related entity ID
- Actor
- Timestamp
- Source references when applicable

---

# Audit Requirements

Every accepted knowledge record must be traceable through:

Knowledge Record

↓

Memory Admission Decision

↓

Validation Decision

↓

Hypothesis

↓

Evidence

↓

Sources

Every rejected hypothesis must retain:

- Rejection reason
- Evidence reviewed
- Challenges raised
- Decision history

No important decision may exist without an audit trail.

---

# Recovery and Safety Rules

## Incomplete Processing

If processing stops before validation completes:

- The investigation remains incomplete.
- No accepted knowledge is created.
- No positive trust event is generated.

## Duplicate Events

Repeated processing of the same recorded event must not apply the same trust or memory update twice.

## Missing Source

If a required source becomes unavailable:

- The affected knowledge is flagged for review.
- The knowledge is not silently deleted.
- The audit record remains preserved.

## Conflicting Updates

Conflicting updates trigger revalidation.

No agent may silently overwrite accepted knowledge.

---

# Human Oversight

CivilOS must preserve the ability for authorised review to:

- Inspect evidence.
- Inspect validation decisions.
- Challenge accepted knowledge.
- Request revalidation.
- Review deprecated knowledge.

Human intervention must also be recorded and auditable.

Human authority does not justify fabricated evidence or hidden changes.

---

# System Success Criteria

The complete CivilOS flow succeeds when:

- Every accepted claim has validated evidence.
- Every accepted claim survives documented criticism.
- Every knowledge record passes the Memory Admission Gate.
- Every trust change maps to a recorded event.
- Every graph relationship is traceable.
- Reused knowledge improves a later investigation.
- Rejected and incomplete work cannot appear as accepted knowledge.
- All important decisions remain auditable.

---

# System Failure Criteria

CivilOS fails when:

- Unsupported claims become accepted knowledge.
- Agents bypass validation.
- Memory accepts direct unvalidated output.
- Trust is assigned without recorded events.
- The Knowledge Graph contains unsupported relationships.
- Failed processing creates accepted knowledge.
- Duplicate events distort trust or memory.
- Important decisions cannot be traced.

---

# Final Success Definition

CivilOS succeeds when validated knowledge created today improves future investigations without hiding uncertainty, contradictions, revisions, or failures.

The system must prove knowledge compounding through actual reuse.

It must not claim improvement without recorded evidence.

---

# Core Principle

CivilOS does not turn answers into truth.

CivilOS turns hypotheses into auditable, revisable, reusable knowledge through evidence, criticism, collective validation, controlled memory admission, and future reuse.

If it is not real, it is not shown.
