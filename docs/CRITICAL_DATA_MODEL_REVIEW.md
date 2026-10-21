# Critical Data Model Review

## Purpose

This document critically evaluates the CivilOS data model before implementation.

The objective is to identify ambiguity, duplication, invalid state ownership, missing provenance, destructive updates, unauditable decisions, broken dependencies, and unnecessary complexity before database schemas are created.

This document is not the final data model.

This document defines the constraints that the final data model must satisfy.

CivilOS cannot produce auditable knowledge if its data model cannot preserve:

- Origin
- Evidence
- Criticism
- Validation
- Admission
- Revision
- Contradiction
- Trust events
- Graph relationships
- Reuse
- Audit history

If the data model loses any of these links, CivilOS violates its own architecture.

---

# Core Data Principle

CivilOS does not store truth as an unsupported value.

CivilOS stores records that explain:

- What was claimed
- Which evidence was examined
- Which criticism occurred
- Which validation rules were applied
- Which decision was reached
- Whether the result entered memory
- How the result changed
- Where the result was reused
- Which system events occurred

If a record cannot be traced, versioned, explained, and audited, it must not be treated as validated knowledge.

---

# Fundamental Data Distinctions

The final model must preserve the following distinctions.

## Question Is Not Investigation

A question is user input.

An Investigation is the governed process created to examine that question.

One question may create multiple investigations.

One investigation must preserve its original question.

---

## Hypothesis Is Not Knowledge

A Hypothesis is a claim under evaluation.

A Knowledge Record is an admitted result of validation and Memory Admission.

A Hypothesis must never become Knowledge merely because an agent proposed it.

---

## Evidence Is Not Source

A Source identifies where information originated.

An Evidence Record identifies the specific information used in relation to a hypothesis or claim.

One Source may support multiple Evidence Records.

One Evidence Record must identify its provenance.

---

## Validation Is Not Memory Admission

A Validation Decision determines whether a hypothesis satisfies the active validation rules.

Memory Admission determines whether accepted material becomes a persistent Knowledge Record.

An accepted hypothesis is eligible for memory.

It does not bypass Memory Admission.

---

## Knowledge Is Not Graph Relationship

A Knowledge Record represents admitted validated knowledge.

A Graph Relationship represents a validated connection between eligible graph elements.

Two valid Knowledge Records do not automatically create a valid relationship.

Every permanent relationship requires its own evidence, provenance, validation, and admission.

---

## Trust Is Not Truth

A Trust Event records a validated performance outcome.

A Trust Result summarises relevant historical performance under a versioned Trust Policy.

Trust must not determine whether a current claim is true.

---

## Event Is Not Current State

A Domain Event records that something occurred.

A current-state record represents the system's present authoritative state.

The Event Ledger preserves history.

Current-state records support efficient and controlled system operation.

The final model must not confuse these responsibilities.

---

# Proposed Minimum Authoritative Entities

The final data model should begin with the smallest justified set of authoritative entities.

## Investigation

Represents one governed examination of a question.

---

## Investigation Plan

Defines route, roles, limits, policies, dependencies, and validation requirements.

---

## Task Contract

Defines one bounded unit of agent or system work.

---

## Agent

Identifies an agent instance or participating computational entity.

---

## Agent Role

Defines permissions, responsibilities, prohibited actions, and expected contribution types.

---

## Contribution

Records a structured output produced by an agent.

---

## Hypothesis

Represents a claim under evaluation.

---

## Source Record

Represents the origin of information.

---

## Evidence Record

Represents information used to support, contradict, or contextualise a claim.

---

## Challenge Record

Represents a documented objection, weakness, contradiction, or alternative explanation.

---

## Cross-Validation Record

Represents an independent review of a hypothesis, evidence, or challenge set.

---

## Validation Decision

Represents the authoritative validation outcome for a hypothesis version.

---

## Memory Admission Decision

Represents the authoritative decision to admit, reject, merge, or revalidate accepted material.

---

## Knowledge Record

Represents admitted, validated, revisable, reusable knowledge.

---

## Knowledge Revision

Preserves each change to a Knowledge Record.

---

## Trust Event

Represents a validated positive, negative, reversal, or review event.

---

## Trust Calculation Record

Represents a reproducible Trust result under a specific policy version.

---

## Graph Node

Represents an admitted graph entity.

---

## Relationship Proposal

Represents a proposed connection between graph elements.

---

## Graph Relationship

Represents an admitted and validated relationship.

---

## Tool Receipt

Proves that an authorised tool execution occurred or failed.

---

## Model Execution Record

Records model provider, model identifier, configuration, execution status, and structured-output result.

---

## Policy Version

Represents one immutable version of a system policy.

---

## Domain Event

Records a material system event in the append-only Event Ledger.

---

## Audit Record

Connects an action or decision to its actor, inputs, outputs, policy versions, timestamp, and reason.

---

# Attack 1: Undefined Unit of Knowledge

## Risk

The model may treat any of the following as knowledge:

- Agent output
- Hypothesis
- Evidence
- Validation Decision
- Memory entry
- Graph node
- Final conclusion

This creates multiple incompatible definitions of truth.

## Required Decision

The authoritative persistent knowledge unit is:

```text
Knowledge Record
```

A Knowledge Record may exist only when:

- A related Hypothesis exists.
- A successful Validation Decision exists.
- Required Evidence Records exist.
- Required provenance exists.
- A successful Memory Admission Decision exists.
- The applicable policy versions are recorded.

## Required Test

Attempt to create a Knowledge Record without each required dependency.

Every invalid attempt must fail.

---

# Attack 2: Multiple Sources of Truth

## Risk

Validation, Memory, Trust, Graph, and Orchestration may each store their own interpretation of the same state.

Example:

```text
Hypothesis.status = accepted
ValidationDecision = rejected
MemoryAdmission = admitted
```

This inconsistency destroys auditability.

## Required Authority Rules

- Investigation status belongs to the Investigation record.
- Task status belongs to the Task Contract execution record.
- Hypothesis lifecycle belongs to the Hypothesis record.
- Validation outcome belongs to the Validation Decision.
- Memory admission outcome belongs to the Memory Admission Decision.
- Knowledge current status belongs to the Knowledge Record.
- Trust history belongs to Trust Events.
- Current Trust result belongs to the Trust Calculation Record.
- Graph element state belongs to its Graph Node or Graph Relationship.
- Tool execution truth belongs to the Tool Receipt.

## Required Test

Create conflicting downstream projections.

The authoritative source must remain identifiable and unchanged.

---

# Attack 3: Missing Provenance

## Risk

A conclusion may exist without a reconstructable origin.

## Required Lineage

Every Knowledge Record must support this traversal:

```text
Knowledge Record
↓
Memory Admission Decision
↓
Validation Decision
↓
Hypothesis Version
↓
Evidence Records
↓
Source Records
```

It must also support:

```text
Knowledge Record
↓
Contributions
↓
Tasks
↓
Agents and Roles
↓
Model and Tool Execution Records
```

## Required Rule

The lineage must use explicit identifiers.

Textual descriptions are not sufficient foreign-key equivalents.

## Required Test

Select any Knowledge Record.

The complete lineage must be reconstructable without guessing.

---

# Attack 4: Evidence and Source Duplication

## Risk

The system may create separate but overlapping entities such as:

```text
Source
Citation
Reference
Document
Evidence
Evidence Source
```

without clear meanings.

## Required Distinction

### Source Record

Identifies the originating publication, dataset, document, tool result, or primary record.

### Evidence Record

Identifies the specific material used in relation to a hypothesis.

### Evidence Reference

Links a decision, challenge, contribution, or relationship to an Evidence Record.

## Required Rule

Republished copies must preserve the original source root when known.

Five pages derived from one report must not be counted as five independent sources.

---

# Attack 5: Unversioned Mutable Knowledge

## Risk

Updating a row may erase what CivilOS previously believed and why.

## Required Rule

Knowledge is never silently overwritten.

Every material update must create:

- A new Knowledge Revision.
- A new version number.
- A change reason.
- New evidence references when applicable.
- A validation or revalidation reference.
- Prior-version linkage.
- An Audit Record.

## Required Knowledge States

- Active
- Challenged
- Updated
- Deprecated
- Merged
- Revalidation Required

## Required Test

Update and deprecate knowledge.

All historical versions must remain reconstructable.

---

# Attack 6: Invalid Deletion

## Risk

Deleting evidence, validation, knowledge, Trust Events, or graph relationships may destroy audit history.

## Required Deletion Policy

The following records must not be silently hard-deleted:

- Hypotheses
- Evidence Records used in decisions
- Challenges
- Validation Decisions
- Memory Admission Decisions
- Knowledge Records
- Knowledge Revisions
- Trust Events
- Trust Calculation Records
- Graph Relationships
- Domain Events
- Audit Records
- Tool Receipts
- Model Execution Records used by accepted outcomes
- Policy Versions used in decisions

## Allowed Alternatives

- Deprecated
- Revoked
- Superseded
- Merged
- Cancelled
- Reversed
- Redacted under an authorised policy
- Tombstoned while preserving required audit metadata

## Required Test

Attempt a prohibited hard deletion.

The operation must fail or apply a controlled retention workflow.

---

# Attack 7: State Ownership Conflict

## Risk

Multiple components may change the same state directly.

## Required Rule

Each state transition must have one authorised owner.

Examples:

- Knowledge Validation Engine creates Validation Decisions.
- Memory Engine creates Memory Admission Decisions and Knowledge Revisions.
- Trust Engine creates Trust Calculation Records.
- Knowledge Graph Engine creates Graph Admission Decisions and Graph Relationships.
- Agent Orchestration Engine changes orchestration and task states.

No module may update another module's authoritative records directly.

Cross-module effects occur through commands and Domain Events.

---

# Attack 8: Invalid State Transitions

## Risk

Records may jump directly from proposed to accepted, or deprecated back to active, without the required process.

## Required Rule

Every stateful entity needs an explicit state machine.

The final model must define allowed transitions for:

- Investigation
- Task
- Hypothesis
- Evidence review
- Challenge
- Validation
- Memory admission
- Knowledge
- Trust profile
- Graph node
- Graph relationship

## Required Fields

Every state transition must record:

- Previous state
- New state
- Actor
- Reason
- Timestamp
- Policy version
- Audit reference

## Required Test

Attempt every forbidden transition.

Every forbidden transition must fail.

---

# Attack 9: Circular Validation

## Risk

Validation records can form cycles that imitate independence.

## Required Data Support

The model must represent:

- Proposing agent
- Evidence contributor
- Reviewing agent
- Validating agent
- Dependency relationships
- Shared model configuration
- Shared evidence roots

## Required Rule

A validator cannot be counted as independent when the applicable policy identifies an invalid dependency.

## Required Test

Store:

```text
A validates B
B validates C
C validates A
```

The cycle must be detectable through data relationships.

---

# Attack 10: False Evidence Independence

## Risk

Multiple Evidence Records may appear independent while sharing one root source.

## Required Model

Source Records must support:

- Parent source
- Original source
- Publisher
- Publication date
- Retrieval date
- Source type
- Canonical identifier
- Content fingerprint
- Derived-from relationship

## Required Test

Create several evidence records derived from one source.

The model must expose the common origin.

---

# Attack 11: Duplicate Processing

## Risk

The same event may create repeated:

- Knowledge Records
- Trust Events
- Graph Relationships
- Contributions
- Metrics
- Tool results

## Required Fields

State-changing commands and Domain Events must support:

- Idempotency key
- Deduplication key
- Processing status
- First processed timestamp
- Existing-result reference

## Required Test

Replay each critical event.

System state must not change twice.

---

# Attack 12: Event Ledger Confusion

## Risk

Attempting full event sourcing may make the hackathon MVP unnecessarily complex.

Using only current-state tables may destroy history.

## Required Decision

CivilOS MVP uses:

```text
Authoritative Current-State Records
+
Append-Only Domain Event Ledger
```

The Event Ledger supports history, audit, recovery, Trust, and debugging.

Current-state records support operational reads and controlled transactions.

CivilOS does not need to rebuild all operational state exclusively from events in MVP V1.

## Required Test

Compare critical current-state records with their recent events.

Inconsistencies must be detectable.

---

# Attack 13: Partial Transaction Corruption

## Risk

A failure may create only part of an operation.

Example:

```text
Knowledge Record created
Trust Event missing
Audit Record missing
```

## Required Atomic Boundaries

### Knowledge Admission

Must atomically create:

- Memory Admission Decision
- Knowledge Record or Knowledge Revision
- Knowledge Admitted Event
- Audit Record

### Graph Admission

Must atomically create:

- Graph Admission Decision
- Graph Node or Relationship
- Graph Event
- Audit Record

### Trust Calculation

Must atomically create:

- Trust Calculation Record
- Policy reference
- Event references
- Audit Record

## Required Test

Force a failure in the middle of each transaction.

No invalid partial active state may remain.

---

# Attack 14: Orphaned Records

## Risk

Records may reference deleted or missing parents.

## Required Integrity Rules

Examples:

- Evidence must reference an existing Source when required.
- Validation must reference an existing Hypothesis version.
- Knowledge must reference an existing Validation Decision.
- Trust Events must reference real system outcomes.
- Graph Relationships must reference existing eligible nodes.
- Contributions must reference valid Tasks and Investigations.

Foreign-key or equivalent application-level integrity must be enforced.

## Required Test

Attempt to create every major entity with a missing dependency.

The operation must fail.

---

# Attack 15: Trust Without Outcomes

## Risk

Trust may be calculated from activity rather than validated outcomes.

## Required Rule

Trust Events must reference an auditable system outcome.

Invalid Trust foundations include:

- Message count
- Token count
- Popularity
- Agreement
- Self-reported success
- Participation alone

## Required Test

Attempt to create positive Trust from activity without outcome validation.

The event must remain ineligible or be rejected.

---

# Attack 16: Trust Policy Rewrites History

## Risk

Changing Trust weights may silently change old scores.

## Required Model

Trust Calculation Records must preserve:

- Policy ID
- Policy version
- Input Trust Events
- Excluded events
- Calculation timestamp
- Domain
- Role
- Result
- Explanation

Recalculation creates a new record.

It must not silently overwrite the old calculation.

---

# Attack 17: Graph as a Second Memory

## Risk

Knowledge may be duplicated independently in Memory and Graph.

## Required Distinction

Memory owns Knowledge Records.

Graph owns Graph Nodes and Graph Relationships.

A Knowledge Node references a Knowledge Record.

It does not become a separate independent source of truth.

## Required Test

Change Knowledge status.

The Graph must detect the new state without rewriting historical Knowledge content.

---

# Attack 18: Unsupported Graph Causality

## Risk

A Graph Relationship may display causation based only on similarity or agent language.

## Required Relationship Data

Every admitted relationship needs:

- Source Node
- Target Node
- Relationship Type
- Evidence references
- Validation reference
- Proposed by
- Validated by
- Current state
- Temporal validity
- Policy version
- Audit reference

## Required Rule

Causal relationship types require causal evidence under the active policy.

Semantic similarity may propose a relationship.

It cannot admit the relationship.

---

# Attack 19: Unbounded JSON Fields

## Risk

Placing all data into arbitrary JSON creates flexibility but destroys validation, indexing, integrity, and clarity.

## Required Decision

Use normalised authoritative columns for:

- Identifiers
- States
- Relationships
- Timestamps
- Policy versions
- Ownership
- Provenance
- Audit references
- Idempotency

Use JSON only for:

- Bounded metadata
- Provider-specific details
- Extensible non-authoritative attributes
- Structured payloads governed by schemas

Every important JSON payload requires a schema version.

---

# Attack 20: Over-Normalisation

## Risk

Excessive normalisation can create dozens of joins and slow implementation.

## Required Decision

Normalise authoritative identity, provenance, state, and relationships.

Allow bounded denormalised read models for user-facing queries.

Read models must reference authoritative records.

Read models must never become hidden sources of truth.

---

# Attack 21: Premature Vector Database

## Risk

A vector database may be treated as memory or truth.

## Required Rule

Vector search provides candidate retrieval.

It is not authoritative storage.

A vector result must reference an authoritative Knowledge Record, Evidence Record, or Source Record.

Embedding similarity does not validate knowledge.

The MVP may operate without a dedicated vector database.

---

# Attack 22: Premature Graph Database

## Risk

A dedicated graph database adds operational complexity before the model stabilises.

## Required Decision

The MVP may represent nodes and edges in relational tables.

A dedicated graph database is optional.

Migration becomes justified only when real graph traversal requirements exceed the primary store's capabilities.

The graph database, if added, must not become an unaudited parallel source of truth.

---

# Attack 23: Missing Temporal Semantics

## Risk

The system may confuse when something occurred with when CivilOS learned it.

## Required Temporal Fields

Relevant records may require:

- occurred_at
- published_at
- retrieved_at
- observed_at
- valid_from
- valid_to
- recorded_at
- created_at
- updated_at
- deprecated_at

These fields must have distinct meanings.

## Required Test

Create knowledge about a past event discovered today.

The model must preserve both times.

---

# Attack 24: Timezone Ambiguity

## Risk

Timestamps recorded without timezone destroy ordering and reproducibility.

## Required Rule

Persist timestamps in a standard timezone-aware format.

Display may localise timestamps.

Stored authoritative timestamps must not lose timezone information.

---

# Attack 25: Identity Confusion

## Risk

The model may confuse:

- Human user
- Human reviewer
- Agent definition
- Agent instance
- Model provider
- Model execution
- System component

## Required Distinction

The final model must represent actors explicitly.

An `Actor` abstraction may identify the actor type while preserving role-specific records.

Attribution must never depend on a display name alone.

---

# Attack 26: Agent Version Ambiguity

## Risk

An agent's prompt, tools, model, or policy may change, making historical comparisons invalid.

## Required Model

Agent execution records must preserve:

- Agent definition ID
- Agent definition version
- Role version
- Prompt or instruction version
- Model configuration reference
- Tool permission version
- Policy versions
- Execution timestamp

Historical contributions must remain linked to their original configuration.

---

# Attack 27: Model Output Treated as Evidence

## Risk

A model-generated statement may be stored as evidence.

## Required Rule

Model output is a Contribution or candidate interpretation.

It becomes Evidence only when it references a legitimate source or a valid system observation under the Evidence Policy.

Model confidence is not evidence.

Model eloquence is not evidence.

---

# Attack 28: Tool Claim Without Receipt

## Risk

An agent may claim a tool was used.

## Required Rule

Only a Tool Receipt proves tool execution.

Evidence produced through a tool must reference:

- Tool Receipt
- Tool result
- Tool version or adapter
- Execution status
- Timestamp
- Audit reference

Without a valid Tool Receipt, the action is treated as not executed.

---

# Attack 29: Prompt and Policy Loss

## Risk

Historical decisions may be impossible to reproduce because instructions changed.

## Required Model

Material executions must preserve references to:

- Prompt version
- Role version
- Model configuration
- Validation Policy
- Memory Policy
- Trust Policy
- Graph Policy
- Orchestration Policy

The model should store references, not necessarily duplicate entire policy bodies in every row.

---

# Attack 30: Missing Uncertainty Representation

## Risk

The schema may force everything into accepted or rejected.

## Required States

CivilOS must support:

- Insufficient Evidence
- Unresolved
- Under Review
- Challenged
- Revalidation Required

Uncertainty must be explicit.

It must not be hidden in free-form notes.

---

# Attack 31: Contradictions Erased by Updates

## Risk

Updating knowledge may overwrite conflicting evidence or claims.

## Required Model

Contradictions must be represented explicitly through:

- Challenge Records
- Contradiction references
- Graph contradiction relationships
- Knowledge state changes
- Revalidation records

The model must preserve both sides and the decision history.

---

# Attack 32: Merge Without History

## Risk

Duplicate Knowledge or Graph Nodes may be merged and lose identifiers or references.

## Required Rule

Merge operations must preserve:

- Canonical record
- Merged record IDs
- Merge reason
- Actor
- Timestamp
- Prior references
- Audit Record

References to merged records must remain resolvable.

---

# Attack 33: Cascading Invalidations

## Risk

A source becomes invalid, but downstream Knowledge, Trust, and Graph records remain active.

## Required Dependency Model

CivilOS must track dependencies between:

- Sources and Evidence
- Evidence and Validation
- Validation and Knowledge
- Knowledge and Graph Relationships
- Outcomes and Trust Events
- Knowledge and reuse events

Invalidating an upstream record must identify downstream records for review.

Automatic deletion is prohibited.

Revalidation is required.

---

# Attack 34: Reversal Without Compensation

## Risk

A positive Trust Event or Knowledge admission may remain active after its basis is reversed.

## Required Model

Reversals must create compensating records.

Examples:

- Trust Event Reversal
- Knowledge Revalidation Request
- Graph Relationship Challenge
- Memory Deprecation Decision

Historical records remain available.

Current views must reflect the latest valid state.

---

# Attack 35: Missing Reuse Evidence

## Risk

CivilOS may claim knowledge compounding without storing proof of reuse.

## Required Entity

The final model needs a `Knowledge Reuse Record` or an equivalent auditable event.

It should identify:

- Knowledge Record
- Later Investigation
- Task or decision where reused
- Reuse purpose
- Outcome reference
- Timestamp
- Audit reference

Retrieval alone does not prove useful reuse.

---

# Attack 36: Metrics Without Ground Truth

## Risk

Counts may be calculated from incomplete or duplicated data.

## Required Rule

Every metric must define:

- Source records
- Inclusion criteria
- Exclusion criteria
- Policy or formula version
- Calculation timestamp
- Deduplication rule

Metrics are derived views.

Metrics are not authoritative truth.

---

# Attack 37: Data Leakage

## Risk

Agents may receive more data than required.

## Required Model Support

The model must support:

- Data classification
- Access scope
- Sensitivity label
- Retention policy
- Actor permissions
- Redaction references

Audit records must identify access to protected records.

---

# Attack 38: Personal Identity Used in Trust

## Risk

Trust may be influenced by irrelevant personal attributes.

## Required Rule

Trust calculations may use contribution outcomes.

Trust calculations must not use protected personal characteristics.

The final model should not make those attributes available to Trust calculations unless a legitimate legal requirement exists and the use is explicitly governed.

---

# Attack 39: Secret Exposure

## Risk

API keys or credentials may be stored in normal domain tables, logs, prompts, or Tool Receipts.

## Required Rule

Secrets are stored outside the domain model in authorised secret management.

Domain records may store secret references.

They must not store secret values.

---

# Attack 40: Retention Without Policy

## Risk

Auditability may be used as an excuse to store everything forever.

## Required Model

Every sensitive or operational record class should support:

- Retention policy reference
- Legal hold status when applicable
- Redaction status
- Deletion or tombstone process
- Audit metadata

Auditability and privacy must coexist.

---

# Attack 41: Test Fixtures Mixed With Real Data

## Risk

Synthetic test records may appear as real knowledge.

## Required Rule

Every record must support an environment or data classification such as:

- Production
- Development
- Test
- Fixture

Test fixtures must never appear in production knowledge views.

Synthetic data must be explicitly labelled.

---

# Attack 42: Provider Unavailable State Missing

## Risk

When no model provider or credits are available, the system may fabricate agent output.

## Required Model

Model-dependent tasks must support states such as:

- Awaiting Provider
- Provider Unavailable
- Execution Failed
- Retry Eligible

No Model Execution Record may claim success without a real provider response.

---

# Attack 43: Overly Broad Status Fields

## Risk

A generic `status` string across every table creates inconsistent meanings.

## Required Decision

Each domain entity needs a bounded status vocabulary.

Status values should use constraints or validated enums.

Transitions should be governed by domain-specific rules.

---

# Attack 44: Missing Database Constraints

## Risk

Application code alone may fail to protect critical invariants.

## Required Constraints

Where technically possible, the database should enforce:

- Unique identifiers
- Unique idempotency keys
- Required foreign keys
- Non-null authoritative fields
- Valid status values
- Unique active versions when required
- Relationship endpoint integrity
- One active policy version per policy type when required

Application rules and database constraints should reinforce each other.

---

# Attack 45: Query Models Becoming Authoritative

## Risk

A user-facing projection may diverge from authoritative records and later be treated as truth.

## Required Rule

Read models must contain references to source records and projection timestamps.

Critical decisions must read from authoritative records or verified projections.

Projection rebuilds must be possible.

---

# Attack 46: Missing Concurrency Control

## Risk

Two validators or updates may overwrite one another.

## Required Model Support

Versioned mutable records should support optimistic concurrency or equivalent controls.

Examples:

- Version number
- Updated timestamp
- Expected previous version

Conflicting writes must not silently succeed.

---

# Attack 47: Schema Migration Destroys History

## Risk

Changing database structure may make old records unreadable.

## Required Rule

Schema migrations must be versioned and reversible where feasible.

Structured payloads must include schema versions.

Historical data migration must preserve identifiers and audit references.

---

# Attack 48: Unbounded Payload Growth

## Risk

Full model outputs, tool results, and documents may bloat transactional tables.

## Required Decision

Large raw payloads may use object storage or a dedicated payload store.

Authoritative records retain:

- Payload reference
- Content fingerprint
- Media type
- Size
- Integrity status
- Access policy
- Audit reference

Raw storage must not replace structured domain records.

---

# Attack 49: Content Integrity Loss

## Risk

A source or tool result may change after retrieval.

## Required Fields

Important external content should support:

- Content fingerprint
- Retrieved timestamp
- Source location
- Original identifier
- Stored snapshot reference when lawful and permitted
- Availability status

The model must distinguish live source state from retrieved evidence state.

---

# Attack 50: Model Too Large for the MVP

## Risk

The perfect schema becomes impossible to implement during the hackathon.

## Required MVP Discipline

The final model must distinguish:

- MVP-required entities
- Deferred entities
- Derived projections
- Optional infrastructure

The MVP should implement the minimum tables necessary to prove:

```text
Question
↓
Hypothesis
↓
Evidence
↓
Challenge
↓
Validation
↓
Memory Admission
↓
Knowledge Record
↓
Trust Events
↓
Graph Relationship
↓
Knowledge Reuse
```

The model must preserve future extensibility without requiring full enterprise complexity on day one.

---

# Required MVP Entities

The minimum serious MVP should include:

1. Investigation

2. Task Contract

3. Agent Definition or Agent Role

4. Contribution

5. Hypothesis

6. Source Record

7. Evidence Record

8. Challenge Record

9. Validation Decision

10. Memory Admission Decision

11. Knowledge Record

12. Knowledge Revision

13. Trust Event

14. Graph Node

15. Relationship Proposal

16. Graph Relationship

17. Tool Receipt

18. Model Execution Record

19. Policy Version

20. Domain Event

21. Audit Record

22. Knowledge Reuse Record

This list must still be challenged during final modelling.

The final model may combine records only when responsibilities and invariants remain clear.

---

# Deferred or Optional MVP Capabilities

The following may be deferred if the MVP can preserve the required behaviour without them:

- Dedicated graph database
- Dedicated vector database
- Complex ontology tables
- Full policy-editing interface
- Enterprise identity federation
- Multi-tenant billing
- Automated retention workflows
- Large payload storage service
- Advanced analytics warehouse
- Distributed event broker
- Independent microservice databases

Deferral must not remove evidence, validation, provenance, audit, or reuse tracking.

---

# Required Relationship Map

The final data model must explicitly represent at least these relationships:

```text
Investigation
  ├── has many Task Contracts
  ├── has many Hypotheses
  ├── has many Contributions
  └── produces zero or more Validation Decisions

Task Contract
  ├── belongs to Investigation
  ├── assigned to Agent or Role
  └── produces Contributions

Hypothesis
  ├── belongs to Investigation
  ├── has many Evidence Records
  ├── has many Challenge Records
  ├── has many Cross-Validation Records
  └── has one or more Validation Decisions across versions

Evidence Record
  ├── belongs to Source Record
  ├── relates to Hypothesis
  └── may support, contradict, or contextualise

Validation Decision
  ├── belongs to Hypothesis version
  ├── references Evidence
  ├── references Challenges
  └── creates eligibility for Memory Admission

Memory Admission Decision
  ├── references Validation Decision
  └── may create or update Knowledge Record

Knowledge Record
  ├── references Validation Decision
  ├── has many Knowledge Revisions
  ├── may generate Trust Events
  ├── may become Graph Node
  └── may be reused in later Investigations

Trust Event
  ├── references a real outcome
  ├── references an Actor or Agent
  └── contributes to Trust Calculation

Graph Relationship
  ├── connects two eligible Graph Nodes
  ├── references validation
  ├── references evidence
  └── maintains temporal and revision history

Knowledge Reuse Record
  ├── references prior Knowledge Record
  ├── references later Investigation
  └── records the demonstrated reuse outcome
```

---

# Required Invariants

The final data model must make these conditions impossible or detectable.

1. Knowledge without Validation.

2. Active Knowledge without Memory Admission.

3. Evidence without provenance where provenance is required.

4. Positive Trust without a real outcome.

5. Active Graph Relationship without evidence and validation.

6. A tool-based result without a Tool Receipt.

7. Duplicate application of the same event.

8. Silent overwriting of Knowledge.

9. Silent deletion of audit history.

10. Self-validation counted as independent validation.

11. Circular validation counted as independent validation.

12. Test data displayed as production knowledge.

13. Deprecated Knowledge displayed as active without status.

14. A metric shown without a real calculation source.

15. A successful model action without a real Model Execution Record.

---

# Required Data Model Tests

## Test 1: Create Knowledge Without Validation

Expected:

Rejected by application and database integrity rules.

---

## Test 2: Create Knowledge Without Memory Admission

Expected:

Rejected.

---

## Test 3: Replay Knowledge Admission Event

Expected:

Existing result returned or duplicate ignored.

No second Knowledge Record.

---

## Test 4: Reverse Validation

Expected:

Dependent Knowledge flagged for revalidation.

Trust and Graph dependencies identified.

History preserved.

---

## Test 5: Update Knowledge Concurrently

Expected:

One write succeeds under valid version control.

Conflicting write requires reload or review.

---

## Test 6: Delete Evidence Used by Knowledge

Expected:

Hard deletion blocked or controlled retention workflow applied.

Knowledge dependency remains visible.

---

## Test 7: Duplicate Source Roots

Expected:

Evidence records retain common root.

Independent-source count remains accurate.

---

## Test 8: Create Positive Trust Event Without Outcome

Expected:

Rejected or ineligible.

---

## Test 9: Create Graph Relationship Without Evidence

Expected:

Admission rejected.

---

## Test 10: Tool Claim Without Receipt

Expected:

No eligible Evidence Record produced.

---

## Test 11: Reuse Knowledge

Expected:

Knowledge Reuse Record created with later Investigation and outcome reference.

---

## Test 12: Provider Unavailable

Expected:

Model task records unavailable or failed status.

No fabricated Model Execution success.

---

## Test 13: Test Fixture Isolation

Expected:

Fixture records excluded from production queries and metrics.

---

## Test 14: Historical Reconstruction

Expected:

Any Knowledge Record can be traced to Validation, Hypothesis, Evidence, Source, Agent contributions, policies, and events.

---

## Test 15: Graph and Memory Separation

Expected:

Graph node references Knowledge Record.

Graph does not become an independent conflicting Knowledge source.

---

# Questions the Final Data Model Must Answer

Before `CIVILOS_DATA_MODEL.md` is approved, the model must answer:

1. What is the authoritative unit of validated knowledge?

2. Which exact dependencies are mandatory for a Knowledge Record?

3. Which component owns every state transition?

4. Can every decision be reconstructed?

5. Can every important record be versioned?

6. Can every change be audited?

7. Can contradictions be represented without deletion?

8. Can Trust be reversed when its basis changes?

9. Can graph dependencies be located after evidence invalidation?

10. Can knowledge reuse be proven?

11. Can duplicate processing be prevented?

12. Can test data be isolated?

13. Can provider failure be represented honestly?

14. Can the MVP be implemented without unnecessary infrastructure?

15. Can the schema evolve without rewriting history?

If any answer is no, the data model is not ready.

---

# Architecture Decisions Produced by This Review

The final data model should adopt these decisions unless a stronger justified alternative is documented.

## Decision 1

Use a relational transactional database as the MVP source of truth.

---

## Decision 2

Represent graph nodes and relationships relationally in the MVP.

---

## Decision 3

Use an append-only Domain Event Ledger alongside current-state records.

---

## Decision 4

Use immutable validation decisions and versioned Knowledge revisions.

---

## Decision 5

Use explicit Source and Evidence records.

---

## Decision 6

Treat model outputs as Contributions, not Evidence or Knowledge.

---

## Decision 7

Require Tool Receipts for tool-backed claims.

---

## Decision 8

Use idempotency keys for all critical writes.

---

## Decision 9

Store policy and configuration versions with decisions.

---

## Decision 10

Record knowledge reuse explicitly.

---

## Decision 11

Use controlled states and transitions instead of arbitrary status strings.

---

## Decision 12

Avoid hard deletion for auditable knowledge records.

---

## Decision 13

Keep Trust, Memory, Validation, Graph, and Orchestration ownership separate.

---

## Decision 14

Do not require a dedicated vector or graph database for the MVP.

---

## Decision 15

Implement the minimum model required to prove valid knowledge creation and compounding.

---

# Final Critical Verdict

CivilOS will not fail because the database lacks enough tables.

CivilOS will fail if the model cannot distinguish:

- Claim from knowledge.
- Source from evidence.
- Validation from admission.
- Memory from graph.
- Trust from truth.
- Event history from current state.
- Retrieval from useful reuse.
- Correlation from causation.
- Real execution from agent claims.
- Test data from production knowledge.

The final data model must protect these distinctions structurally.

Application prompts are not sufficient protection.

Documentation is not sufficient protection.

Critical invariants must be enforced through schemas, constraints, ownership, transactions, versioning, events, and tests.

---

# Core Principle

CivilOS is only as trustworthy as its data lineage.

Every accepted Knowledge Record must explain:

- Where it came from.
- Which hypothesis it represents.
- Which evidence supports it.
- Which criticism challenged it.
- Which validation admitted it.
- Which policy governed it.
- How it changed.
- Where it was reused.
- What currently contradicts it.

If the data model cannot answer those questions, CivilOS does not possess validated knowledge.

It possesses unverified records.

If it is not real, it is not shown.
