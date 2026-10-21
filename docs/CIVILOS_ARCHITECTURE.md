# CivilOS Architecture

## Purpose

This document defines the technical architecture of CivilOS.

It connects the CivilOS knowledge engines into one coherent, implementable, auditable, and recoverable system.

CivilOS is not a chatbot architecture.

CivilOS is not a collection of agents connected by prompts.

CivilOS is a governed knowledge-production system that transforms uncertain hypotheses into validated, revisable, reusable, and auditable knowledge.

---

# Architectural Objective

CivilOS must support the following end-to-end process:

User Question

↓

Investigation

↓

Hypotheses

↓

Evidence

↓

Criticism

↓

Independent Validation

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

↓

Knowledge Compounding

Every material transition must produce a structured and auditable record.

No component may fabricate evidence, validation, Trust, knowledge, relationships, metrics, or execution results.

---

# Core Architectural Laws

1. If it is not real, it is not shown.

2. No evidence, no knowledge.

3. No validation, no memory.

4. Trust is earned through recorded outcomes.

5. No single agent can create permanent knowledge alone.

6. Every accepted claim must remain traceable to evidence.

7. Knowledge remains open to challenge, revision, and deprecation.

8. Incomplete processing must never appear as validated knowledge.

9. The Orchestrator coordinates work but never determines truth.

10. High Trust never bypasses evidence.

11. Agreement does not equal validation.

12. Every important state transition must be auditable.

13. Every write operation must be idempotent or protected against duplicates.

14. Every component must have one explicit responsibility.

15. The MVP must prefer implementation simplicity over premature distribution.

---

# Architecture Style

## MVP Architecture

CivilOS V1 should be implemented as a modular monolith.

The system runs as one deployable backend with clearly separated internal modules.

The MVP must not require independent microservices for every engine.

Logical separation is required.

Premature infrastructure complexity is not required.

---

## Why a Modular Monolith

A modular monolith provides:

- Clear component boundaries.
- Lower deployment complexity.
- Simpler local development.
- Easier debugging.
- Shared transactional control.
- Faster implementation.
- A future path to service extraction when justified.

---

## Future Evolution

Components may later become independent services only when operational evidence justifies separation.

Possible future extraction triggers include:

- Independent scaling requirements.
- Distinct security boundaries.
- Separate data ownership.
- High-volume asynchronous workloads.
- Different deployment requirements.
- Proven performance bottlenecks.

CivilOS must not become a distributed system merely for appearance.

---

# High-Level Components

CivilOS contains the following primary components:

1. API and Application Layer

2. Agent Orchestration Engine

3. Knowledge Validation Engine

4. Memory Engine

5. Trust Engine

6. Knowledge Graph Engine

7. Evidence Store

8. Event Ledger

9. Model Gateway

10. Tool Gateway

11. Policy Registry

12. Audit and Observability Layer

13. Persistence Layer

14. User Interface

---

# High-Level Architecture Flow

```text
User Interface
      |
      v
API and Application Layer
      |
      v
Agent Orchestration Engine
      |
      +----------------------+
      |                      |
      v                      v
Model Gateway           Tool Gateway
      |                      |
      +----------+-----------+
                 |
                 v
       Structured Contributions
                 |
                 v
      Knowledge Validation Engine
                 |
        +--------+--------+
        |                 |
        v                 v
     Accepted          Rejected /
        |          Insufficient Evidence
        v                 |
Memory Admission Gate     v
        |            Failure Records
        v
   Memory Engine
        |
        +-----------------------+
        |                       |
        v                       v
 Trust Event Generation   Knowledge Graph Proposals
        |                       |
        v                       v
   Trust Engine          Knowledge Graph Engine
        |                       |
        +-----------+-----------+
                    |
                    v
          Auditable Result View
                    |
                    v
              Future Reuse
```

---

# Component Authority Matrix

Each component has one primary authority.

## API and Application Layer

Owns:

- Request reception.
- Authentication context.
- Request validation.
- Response delivery.
- User-facing investigation lifecycle commands.

Does not own:

- Knowledge validation.
- Trust calculation.
- Memory admission.
- Graph admission.

---

## Agent Orchestration Engine

Owns:

- Investigation plans.
- Task creation.
- Role assignment.
- Workflow coordination.
- Dependencies.
- Limits.
- Retries.
- Stopping conditions.
- Agent contribution collection.

Does not own:

- Truth determination.
- Evidence validation.
- Knowledge acceptance.
- Memory admission.
- Trust assignment.
- Permanent graph admission.

---

## Knowledge Validation Engine

Owns:

- Hypothesis evaluation.
- Evidence requirement enforcement.
- Challenge evaluation.
- Independent-validation requirements.
- Acceptance, rejection, insufficient-evidence, and revalidation decisions.

Does not own:

- Permanent memory storage.
- Trust calculation.
- Graph representation.
- Agent coordination.

---

## Memory Engine

Owns:

- Memory Admission Gate.
- Knowledge Record preservation.
- Knowledge state.
- Revision history.
- Contradiction handling.
- Retrieval.
- Reuse records.
- Deprecation.

Does not own:

- Initial hypothesis acceptance.
- Trust policy.
- Graph relationship validation.
- Agent assignment.

---

## Trust Engine

Owns:

- Trust Events.
- Trust Policy application.
- Domain-specific Trust calculations.
- Trust states.
- Trust reversals.
- Trust explanations.

Does not own:

- Truth.
- Evidence validation.
- Knowledge acceptance.
- Memory admission.
- Graph admission.

---

## Knowledge Graph Engine

Owns:

- Graph Admission Gate.
- Graph nodes.
- Relationship proposals.
- Relationship validation requirements.
- Graph states.
- Temporal validity.
- Graph revisions.
- Contradiction relationships.
- Graph queries.

Does not own:

- Raw evidence validation.
- Hypothesis acceptance.
- Trust calculation.
- Agent coordination.

---

## Evidence Store

Owns:

- Evidence Records.
- Source provenance.
- Supporting, contradicting, and contextual positions.
- Evidence versions.
- Source availability status.
- Evidence integrity references.

Does not determine:

- Whether a hypothesis becomes knowledge.
- Whether an agent gains Trust.
- Whether a graph relationship is admitted.

---

## Event Ledger

Owns:

- Append-only domain events.
- Event identifiers.
- Idempotency keys.
- Timestamps.
- Entity references.
- Actor references.
- Event payload references.
- Event version.

The Event Ledger must not silently delete historical events.

Corrections use compensating or reversal events.

---

## Model Gateway

Owns:

- Model-provider abstraction.
- Model requests.
- Structured-output validation.
- Model identity recording.
- Request and response references.
- Provider error handling.
- Token and cost collection when available.
- Model policy enforcement.

Does not own:

- Truth.
- Knowledge validation.
- Trust assignment.
- Permanent memory.
- Permanent graph relationships.

---

## Tool Gateway

Owns:

- Approved tool execution.
- Permission enforcement.
- Tool receipts.
- Tool errors.
- Result references.
- Execution timestamps.

No agent claim may replace a Tool Receipt.

---

## Policy Registry

Owns versioned policies including:

- Evidence Policy.
- Validation Policy.
- Memory Admission Policy.
- Trust Policy.
- Graph Policy.
- Orchestration Policy.
- Access Policy.
- Retention Policy.

Every material decision must record the policy version applied.

---

## Audit and Observability Layer

Owns:

- Audit trails.
- Structured logs.
- Metrics generated from real activity.
- Traces.
- Failure records.
- Integrity alerts.
- Review views.

Observability data does not become knowledge automatically.

---

# Core Domain Records

The architecture must support the following primary records:

- Investigation
- Investigation Plan
- Task Contract
- Agent
- Agent Role
- Contribution
- Hypothesis
- Evidence Record
- Source Record
- Challenge Record
- Cross-Validation Record
- Validation Decision
- Memory Admission Decision
- Knowledge Record
- Memory Revision
- Trust Event
- Trust Result
- Graph Node
- Relationship Proposal
- Graph Relationship
- Tool Receipt
- Model Execution Record
- Policy Version
- Audit Record
- Domain Event

Specific field definitions belong in `CIVILOS_DATA_MODEL.md`.

---

# Investigation Lifecycle

An Investigation must follow a controlled state machine.

Allowed states:

- Created
- Planned
- Investigating
- Under Review
- Awaiting Validation
- Completed
- Insufficient Evidence
- Revalidation Required
- Failed
- Cancelled
- Escalated

State transitions must be recorded.

A failed, cancelled, incomplete, or unresolved investigation cannot produce accepted knowledge unless a separate valid partial decision explicitly identifies what was accepted.

---

# Knowledge Lifecycle

Knowledge moves through the following architecture:

```text
Hypothesis
      |
      v
Evidence and Criticism
      |
      v
Cross-Validation
      |
      v
Validation Decision
      |
      v
Memory Admission Gate
      |
      v
Knowledge Record
      |
      +----------------------+
      |                      |
      v                      v
Trust Events          Graph Proposals
      |                      |
      v                      v
Trust Engine       Knowledge Graph Engine
      |
      v
Future Reuse
```

A Validation Decision creates eligibility.

A Validation Decision does not bypass Memory Admission.

Memory admission creates an eligible Knowledge Record.

A Knowledge Record does not make every possible relationship valid.

Every graph relationship requires its own admission process.

---

# Request Flow

## Step 1: Request Intake

The API receives a user question.

The original question is preserved.

The system creates an Investigation.

---

## Step 2: Routing

The Agent Orchestration Engine selects the minimum justified route:

- Direct Retrieval
- Single-Agent Investigation
- Adversarial Review
- Full Collective Investigation

The selected route, reason, limits, and required roles are recorded.

---

## Step 3: Memory and Graph Retrieval

Relevant active knowledge may be retrieved.

Retrieved knowledge includes:

- Current status.
- Evidence references.
- Validation history.
- Revision history.
- Contradictions.
- Graph context.

Retrieved knowledge supports investigation planning.

Retrieved knowledge does not become automatic truth for the new investigation.

---

## Step 4: Investigation Planning

The Orchestration Engine defines:

- Hypotheses required.
- Agent roles.
- Task Contracts.
- Evidence requirements.
- Validation requirements.
- Budgets.
- Tool permissions.
- Stopping conditions.

---

## Step 5: Contribution Production

Agents produce typed contributions.

Examples:

- Hypothesis proposals.
- Evidence Records.
- Source limitations.
- Scientific reviews.
- Economic analyses.
- Policy analyses.
- Challenges.
- Contradictions.
- Validation recommendations.

Free-form text alone cannot become permanent knowledge.

---

## Step 6: Evidence Processing

Tool calls pass through the Tool Gateway.

Every successful or failed tool call produces a Tool Receipt.

Evidence is stored with provenance.

Evidence without provenance cannot support acceptance.

---

## Step 7: Criticism and Independent Review

Relevant agents complete independent initial analysis.

Structured criticism then occurs.

Self-validation, circular validation, and unsupported criticism are blocked.

---

## Step 8: Knowledge Validation

The Knowledge Validation Engine creates one of the following decisions:

- Accepted
- Rejected
- Insufficient Evidence
- Revalidation Required

Only accepted hypotheses become eligible for memory.

---

## Step 9: Memory Admission

The Memory Admission Gate checks:

- Validation Decision.
- Evidence availability.
- Provenance.
- Knowledge classification.
- Duplicate knowledge.
- Conflicts.
- Blocking conditions.

Possible outcomes:

- Admitted
- Rejected from Memory
- Merge Required
- Revalidation Required

---

## Step 10: Trust Processing

Validated outcomes generate Trust Events.

The Trust Engine calculates domain-specific historical performance.

Trust never changes the original validation outcome.

---

## Step 11: Graph Processing

Knowledge Records may generate Graph Node or Relationship Proposals.

The Knowledge Graph Engine performs graph-specific admission.

No relationship becomes active without its required evidence and validation.

---

## Step 12: Result Assembly

The Application Layer assembles a read model containing only recorded system activity.

The result may include:

- Current conclusion.
- Validation status.
- Supporting evidence.
- Contradictory evidence.
- Challenges.
- Rejected hypotheses.
- Agent contributions.
- Memory actions.
- Trust explanations.
- Graph actions.
- Audit references.
- Uncertainty and limitations.

If a field was not calculated or recorded, it must not be displayed.

---

# Command and Query Separation

CivilOS should separate writes from reads at the application level.

## Commands

Commands request state changes.

Examples:

- Create Investigation
- Propose Hypothesis
- Add Evidence
- Raise Challenge
- Request Validation
- Admit Knowledge
- Create Trust Event
- Propose Graph Relationship
- Challenge Knowledge

Commands may succeed or fail.

---

## Queries

Queries retrieve current views.

Examples:

- Get Investigation
- Get Validation Record
- Search Active Knowledge
- Explain Trust Result
- Traverse Validated Relationships
- Get Audit Trail

Queries must not change system state.

---

# Internal Communication Model

The MVP may use in-process module calls and an append-only Event Ledger.

The architecture should behave as if components communicate through explicit contracts.

This preserves future service boundaries without requiring premature distributed infrastructure.

## Synchronous Interactions

Use synchronous calls when an immediate decision is required.

Examples:

- Input validation.
- Policy validation.
- Memory Admission check.
- Permission check.

---

## Event-Driven Interactions

Use domain events for outcomes that may trigger multiple downstream actions.

Examples:

```text
HypothesisAccepted
KnowledgeAdmitted
KnowledgeChallenged
KnowledgeDeprecated
TrustEventCreated
GraphRelationshipAdmitted
KnowledgeReused
```

One component publishes the event.

Other components react according to their responsibility.

---

# Event Contract

Every domain event must contain:

```json
{
  "event_id": "EV001",
  "event_type": "KnowledgeAdmitted",
  "entity_id": "K001",
  "investigation_id": "I001",
  "actor": "memory_engine",
  "occurred_at": "timestamp",
  "payload_reference": "PAYLOAD001",
  "policy_versions": {
    "memory_policy": "1.0",
    "validation_policy": "1.0"
  },
  "idempotency_key": "KnowledgeAdmitted-K001-v1",
  "audit_reference": "AUDIT001"
}
```

Schema validation is required before event processing.

Unknown or invalid event versions must not be processed silently.

---

# Source of Truth Rules

CivilOS must define one source of truth for each responsibility.

## Investigation State

Source of truth:

- Investigation Record

---

## Hypothesis Validation

Source of truth:

- Validation Decision

---

## Accepted Knowledge

Source of truth:

- Active Knowledge Record in the Memory Engine

---

## Trust History

Source of truth:

- Trust Event Ledger

---

## Current Trust Result

Source of truth:

- Versioned Trust Calculation Record

---

## Graph Relationship

Source of truth:

- Active Graph Relationship Record

---

## Evidence Provenance

Source of truth:

- Evidence Record and Source Record

---

No downstream projection may silently override its source of truth.

---

# Consistency Model

CivilOS must distinguish strong local consistency from eventual downstream consistency.

## Strong Consistency Required

Strong consistency is required when:

- Creating a Validation Decision.
- Processing Memory Admission.
- Preventing duplicate events.
- Updating knowledge state.
- Applying Trust Event reversal.
- Admitting a graph relationship.
- Enforcing permissions.

---

## Eventual Consistency Allowed

Eventual consistency may be acceptable when:

- Updating user-facing projections.
- Refreshing analytics.
- Updating non-critical search indexes.
- Building visual graph projections.
- Calculating derived read models.

The user interface must not present stale data as current without status information when the difference is material.

---

# Transaction Boundaries

The MVP should preserve atomicity for critical operations.

Examples:

## Knowledge Admission Transaction

Must atomically produce:

- Memory Admission Decision.
- Knowledge Record.
- Knowledge Admitted Event.
- Audit Record.

If the transaction fails:

- No active Knowledge Record is created.
- No positive Trust Event is generated.
- No permanent graph proposal is treated as admitted.

---

## Trust Calculation Transaction

Must atomically produce:

- Trust Calculation Record.
- Applied policy version.
- Event references.
- Audit Record.

---

## Graph Admission Transaction

Must atomically produce:

- Graph Admission Decision.
- Active Node or Relationship.
- Graph Event.
- Audit Record.

---

# Idempotency and Duplicate Protection

Every command or event capable of changing state must include an idempotency key.

The system must prevent:

- Duplicate Knowledge Records.
- Duplicate Trust Events.
- Duplicate graph relationships.
- Duplicate tool results.
- Duplicate agent contributions.
- Duplicate retries producing repeated rewards.

Repeated processing of the same idempotency key must return the existing result or a duplicate status.

It must not perform the operation twice.

---

# Versioning Strategy

CivilOS must version:

- Domain records.
- Policies.
- Event schemas.
- Prompt and instruction templates.
- Model configuration.
- Tool configuration.
- Knowledge revisions.
- Graph ontology.
- API contracts.

Historical decisions must remain reproducible against their original versions.

Updates must not silently rewrite history.

---

# Model Gateway

CivilOS must access AI models through a provider-independent Model Gateway.

The Model Gateway must record:

- Provider.
- Model identifier.
- Model configuration.
- Request reference.
- Response reference.
- Structured-output status.
- Execution timestamp.
- Token usage when available.
- Cost when available.
- Error status.
- Retry count.

---

## Provider Independence

Business rules must not depend directly on one provider SDK.

Provider adapters may support:

- Meta models.
- Open-weight models.
- Other authorised providers.
- Local models when available.

Switching provider must not bypass validation, provenance, audit, or policy requirements.

---

## No-Credit Behaviour

If no authorised model provider is available:

- Model-dependent actions remain unavailable.
- The system must show the unavailable status honestly.
- Previously recorded data may still be inspected.
- CivilOS must not fabricate agent execution.
- CivilOS must not substitute synthetic outputs unless explicitly marked as test fixtures outside production flow.

---

# Tool Gateway

All external tool use passes through the Tool Gateway.

The Tool Gateway enforces:

- Role permissions.
- Approved tool list.
- Request validation.
- Rate limits.
- Timeouts.
- Result storage.
- Tool Receipts.
- Error reporting.
- Secret isolation.

Agents receive tool results.

Agents do not receive unrestricted credentials.

---

# Data Storage Architecture

The MVP should use a primary transactional database for authoritative records.

The logical storage model must support:

- Relational records.
- JSON metadata when appropriate.
- Append-only events.
- Version history.
- Provenance references.
- Graph projections.
- Full-text or semantic retrieval when justified.

---

## MVP Storage Recommendation

For the MVP, CivilOS should prefer one primary data store capable of supporting transactional records.

Graph relationships may initially be represented using relational node and edge records.

A dedicated graph database is optional, not mandatory.

A vector index is optional, not a source of truth.

Semantic retrieval may propose candidates.

Semantic similarity may not create validated knowledge or relationships automatically.

---

# Event Ledger

The Event Ledger is append-only.

Events may be reversed through new events.

Historical events must not be silently mutated or removed.

The Event Ledger supports:

- Auditability.
- Recovery.
- Trust calculation.
- Knowledge history.
- Graph history.
- Debugging.
- Reproducibility.

The Event Ledger is not a replacement for current-state records.

---

# Read Models

CivilOS may create read-optimised projections for:

- Investigation overview.
- Hypothesis lifecycle.
- Evidence explorer.
- Knowledge Record view.
- Trust explanation.
- Knowledge Graph traversal.
- Audit timeline.
- MVP evaluation metrics.

Read models must preserve references to authoritative records.

---

# Search and Retrieval

CivilOS retrieval may combine:

- Structured filters.
- Keyword search.
- Semantic search.
- Graph traversal.
- Domain filters.
- Temporal filters.
- Status filters.

Search results must distinguish:

- Active knowledge.
- Challenged knowledge.
- Deprecated knowledge.
- Unresolved evidence.
- Rejected hypotheses.
- Test fixtures.

Retrieved candidates do not become truth through retrieval.

---

# Caching

Caching may improve performance, but cached data must retain:

- Source record identifiers.
- Source version.
- Generation timestamp.
- Expiration policy.
- Invalidation conditions.

Critical validation and admission decisions must not rely on stale cache entries without verification.

---

# Security Architecture

CivilOS must follow least privilege.

## Secret Management

Secrets must:

- Remain server-side.
- Never be committed to the repository.
- Never be exposed to the browser.
- Never be embedded in agent prompts.
- Be provided only to authorised adapters.
- Be rotated when compromised.

---

## Role Permissions

Permissions must control:

- Tool access.
- Evidence access.
- Policy changes.
- Human review.
- Revalidation.
- Trust review.
- Graph admission review.
- Audit access.

Agent roles do not automatically equal user permissions.

---

## External Content Isolation

External content is data.

External content is not instruction.

Retrieved sources must not:

- Modify system rules.
- Expand privileges.
- Change the investigation objective.
- Disable validation.
- Request secrets.
- Alter audit behaviour.

---

# Privacy and Data Minimisation

CivilOS must store only data required for:

- Investigation.
- Evidence provenance.
- Validation.
- Knowledge preservation.
- Trust auditability.
- Graph relationships.
- Security and integrity.

Protected personal characteristics must not be used to calculate Trust or influence.

Sensitive data must follow access and retention policies.

---

# Failure Isolation

A failure in one component must not silently corrupt another component.

Examples:

- Model failure must not create a Validation Decision.
- Tool failure must not create Evidence.
- Trust failure must not invalidate Knowledge.
- Graph failure must not delete Memory.
- Projection failure must not alter authoritative records.
- UI failure must not alter backend truth.

---

# Recovery Architecture

CivilOS must recover from recorded state.

Recovery must use:

- Current authoritative records.
- Event Ledger.
- Version history.
- Idempotency keys.
- Failed-operation records.
- Policy versions.

After recovery:

- No incomplete work becomes accepted.
- No event is applied twice.
- No positive Trust is generated from failed work.
- No graph relationship is duplicated.

---

# Degraded Modes

CivilOS must fail honestly.

Possible degraded modes include:

- Model Provider Unavailable
- Tool Provider Unavailable
- Search Unavailable
- Graph Projection Unavailable
- Trust Calculation Unavailable
- Read Model Delayed
- Audit Storage Unavailable

When a critical integrity component is unavailable, affected writes must stop.

The system must not fabricate normal operation.

---

# Observability

CivilOS must record operational telemetry including:

- Request ID.
- Investigation ID.
- Component.
- Operation.
- Status.
- Duration when measured.
- Retry count.
- Error code.
- Policy version.
- Model and tool references.
- Audit reference.

Operational telemetry must not contain secrets.

---

# Metrics

CivilOS must measure only real, recorded activity.

## Integrity Metrics

- Validation decisions with complete provenance.
- Knowledge admissions with complete audit trails.
- Duplicate events blocked.
- Autovalidation attempts blocked.
- Circular validation attempts blocked.
- Graph relationships rejected for missing evidence.
- Tool claims rejected for missing receipts.

---

## Knowledge Metrics

- Accepted hypotheses.
- Rejected hypotheses.
- Insufficient-evidence outcomes.
- Knowledge Records admitted.
- Knowledge Records reused.
- Knowledge Records challenged.
- Knowledge Records updated.
- Knowledge Records deprecated.
- Contradictions preserved.

---

## Efficiency Metrics

- Investigations completed.
- Resource usage per investigation when available.
- Resource usage per admitted Knowledge Record when available.
- Debate rounds without material new information.
- Multiagent routes avoided when unnecessary.
- Tool calls producing eligible Evidence Records.

---

## Reliability Metrics

- Failed operations.
- Retry success.
- Duplicate processing prevented.
- Recovery operations completed.
- Stale projections detected.
- Missing dependencies detected.

If a metric was not measured, it must not be displayed.

---

# Human Oversight Architecture

Authorised human reviewers may:

- Inspect evidence.
- Review validation.
- Challenge accepted knowledge.
- Request revalidation.
- Review suspected gaming.
- Approve policy changes.
- Review deprecated knowledge.
- Review graph merges.
- Cancel investigations.

Human actions must:

- Include actor identity.
- Include reason.
- Preserve prior state.
- Produce an audit event.
- Follow permissions.

Human intervention does not justify fabricated evidence, hidden changes, or silent Trust assignment.

---

# Deployment Architecture

## MVP Deployment

The MVP may use:

- One backend service.
- One primary transactional database.
- One frontend application.
- Provider adapters.
- Internal module boundaries.
- In-process domain events.
- Background jobs only when required.

---

## MVP Non-Requirements

The MVP does not require:

- Multiple microservices.
- Kubernetes.
- Distributed consensus.
- A dedicated graph database.
- A dedicated vector database.
- A distributed message broker.
- Autonomous background agents.
- Production-scale infrastructure.

These may be added only when justified by evidence.

---

# API Boundary

The API should expose controlled operations such as:

- Create Investigation
- Get Investigation
- Propose Hypothesis
- Add Evidence
- Raise Challenge
- Request Validation
- Retrieve Knowledge
- Request Revalidation
- Explain Trust
- Query Knowledge Graph
- Get Audit Trail

The API must not expose direct operations such as:

- Set Trust Score
- Mark Hypothesis Accepted Without Validation
- Insert Permanent Knowledge Directly
- Insert Permanent Graph Relationship Directly
- Delete Audit History
- Bypass Admission Gate

---

# User Interface Boundary

The user interface may display only backend-recorded state.

The interface must not calculate or invent:

- Trust.
- Validation.
- Evidence counts.
- Knowledge states.
- Agent activity.
- Graph relationships.
- Metrics.

The interface may visualise recorded information.

The interface is not a source of truth.

---

# Architecture Decision Records

Important architecture decisions should be captured as versioned Architecture Decision Records.

Examples:

- Modular Monolith for MVP.
- Append-Only Event Ledger.
- Provider-Agnostic Model Gateway.
- Relational Graph Projection for MVP.
- Trust Separate from Truth.
- No Direct Agent Writes to Memory.
- No Majority Vote for Validation.
- No Synthetic Production Metrics.

Each decision should include:

- Context.
- Decision.
- Alternatives considered.
- Consequences.
- Date.
- Version.

---

# Test Architecture

CivilOS must support automated tests at several levels.

## Unit Tests

Verify individual rules and state transitions.

---

## Contract Tests

Verify module boundaries and schemas.

---

## Integration Tests

Verify flows across multiple engines.

---

## End-to-End Tests

Verify complete investigations.

---

## Integrity Tests

Verify that invalid actions are blocked.

Examples:

- Direct memory write.
- Manual Trust assignment.
- Unsupported graph relationship.
- Missing Tool Receipt.
- Duplicate event replay.
- Circular validation.

---

## Recovery Tests

Verify:

- Restart recovery.
- Idempotent replay.
- Partial failure handling.
- Dependency restoration.
- Policy-loading failure.

---

# Required End-to-End Architecture Tests

## Test 1: Accepted Knowledge Flow

Expected path:

```text
Question
↓
Hypothesis
↓
Evidence
↓
Criticism
↓
Validation
↓
Memory Admission
↓
Knowledge Record
↓
Trust Events
↓
Graph Integration
↓
Result
```

All references must remain traceable.

---

## Test 2: Rejected Hypothesis Flow

A rejected hypothesis must not create:

- Active Knowledge Record.
- Positive knowledge Trust Event.
- Active graph relationship.

---

## Test 3: Insufficient Evidence Flow

The system must return `Insufficient Evidence`.

The interface must not invent a conclusion.

---

## Test 4: Revalidation Flow

New contradictory evidence must trigger:

- Knowledge challenge.
- Revalidation.
- Status update.
- Dependency review.
- Preserved history.

---

## Test 5: Component Failure

A downstream component failure must not corrupt upstream truth.

Example:

Graph failure must not invalidate accepted Memory.

---

## Test 6: Duplicate Event Replay

Replaying an event must not:

- Duplicate knowledge.
- Duplicate Trust.
- Duplicate graph relationships.
- Duplicate metrics.

---

## Test 7: Provider Unavailable

When no model provider is available:

- Model actions remain unavailable.
- Existing records remain visible.
- No agent output is fabricated.
- The status is shown honestly.

---

# Architectural Success Criteria

CivilOS architecture succeeds when:

- Every component has one clear responsibility.
- Every source of truth is explicit.
- Every critical write is protected.
- Every material transition is auditable.
- No agent bypasses validation.
- No component silently overrides another component.
- Failed processing does not produce accepted knowledge.
- Duplicate execution does not distort system state.
- Provider changes do not bypass CivilOS rules.
- Knowledge can be challenged, updated, deprecated, and reused.
- The MVP remains implementable by a small team.
- The system can prove knowledge compounding from recorded reuse.

---

# Architectural Failure Criteria

The architecture fails when:

- Multiple components determine truth.
- The Orchestrator becomes an authority.
- Trust overrides evidence.
- Agents write directly to permanent memory.
- Graph relationships bypass validation.
- Historical records are overwritten.
- Events are processed multiple times.
- Missing providers generate fake activity.
- The user interface invents system state.
- Component failure corrupts unrelated records.
- The MVP requires unnecessary distributed infrastructure.
- Knowledge reuse cannot be demonstrated.

---

# Final Architecture Definition

CivilOS is a modular, event-recorded, policy-governed knowledge system.

Agents produce structured contributions.

Tools produce verifiable receipts.

Models produce candidate outputs.

The Knowledge Validation Engine determines eligibility.

The Memory Engine preserves admitted knowledge.

The Trust Engine records historical performance.

The Knowledge Graph Engine connects validated knowledge.

The Agent Orchestration Engine coordinates the process.

The Event Ledger preserves history.

The Audit Layer makes decisions explainable.

The API exposes controlled operations.

The User Interface displays recorded truth.

No single component owns the entire process.

No single agent creates permanent knowledge.

---

# Final Success Definition

CivilOS succeeds when validated knowledge created today can improve future investigations tomorrow through a system that remains traceable, revisable, recoverable, secure, provider-independent, and honest about uncertainty.

CivilOS must prove improvement through recorded reuse.

CivilOS must not claim improvement without evidence.

---

# Core Principle

CivilOS does not turn model output into truth.

CivilOS turns structured contributions into auditable, revisable, reusable knowledge through evidence, criticism, independent validation, controlled admission, persistent memory, recorded Trust, validated relationships, and future reuse.

Agents create contributions.

CivilOS creates knowledge.

If it is not real, it is not shown.
