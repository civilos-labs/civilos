# Knowledge Graph Engine

## Purpose

The Knowledge Graph Engine represents, connects, queries, revises, and audits validated knowledge inside CivilOS.

The engine transforms isolated Knowledge Records into a connected and traceable knowledge structure.

The Knowledge Graph Engine does not create truth.

The Knowledge Graph Engine does not validate hypotheses.

The Knowledge Graph Engine does not invent relationships.

The Knowledge Graph Engine represents knowledge and relationships that have already passed the required validation and admission processes.

---

# Core Question

The Knowledge Graph Engine must answer:

How is one validated knowledge record related to another?

It must not answer:

What relationship appears plausible to a language model?

Plausibility is not validation.

A relationship may enter the graph only when the relationship has evidence, provenance, validation, and an auditable admission decision.

---

# Core Principles

1. Every permanent node must reference validated or explicitly classified knowledge.

2. Every permanent relationship must be supported by evidence.

3. Every relationship must preserve provenance.

4. Correlation must not be represented as causation.

5. A relationship proposed by one agent requires independent review.

6. Contradictory knowledge must be represented, not silently removed.

7. Updates must preserve historical versions.

8. Deprecated knowledge must remain auditable.

9. The graph must not display unsupported relationships as validated knowledge.

10. If it is not real, it is not shown.

---

# Responsibilities

The Knowledge Graph Engine is responsible for:

- Creating graph nodes from eligible records.
- Creating relationships between eligible nodes.
- Preserving evidence and provenance references.
- Recording validation status.
- Detecting possible duplicates and conflicts.
- Maintaining temporal validity.
- Updating and deprecating graph elements.
- Preserving revision history.
- Supporting traceable graph queries.
- Returning relationships with their evidence and validation status.
- Recording every material graph change as an auditable event.

---

# Non-Responsibilities

The Knowledge Graph Engine does not:

- Generate unsupported claims.
- Validate raw evidence.
- Accept or reject hypotheses.
- Admit knowledge into memory.
- Assign trust.
- Replace the Knowledge Validation Engine.
- Replace the Memory Engine.
- Replace the Trust Engine.
- Allow an agent to create permanent knowledge alone.
- Treat model-generated similarity as permanent knowledge.
- Convert correlation into causation.
- Delete disputed knowledge silently.

---

# Separation of Responsibilities

## Knowledge Validation Engine

Determines whether a hypothesis satisfies the validation requirements.

---

## Memory Engine

Preserves validated and revisable Knowledge Records.

---

## Trust Engine

Calculates an entity's historical performance from recorded Trust Events.

---

## Knowledge Graph Engine

Represents eligible knowledge and validated relationships.

---

## Agent Orchestration Engine

Coordinates agents and investigation workflows.

---

The Knowledge Graph Engine consumes validated system records.

The Knowledge Graph Engine does not bypass upstream controls.

---

# Eligible Inputs

The Knowledge Graph Engine may receive:

- Admitted Knowledge Records.
- Validated Evidence Records.
- Accepted Validation Decisions.
- Approved Relationship Proposals.
- Memory revision events.
- Knowledge deprecation events.
- Revalidation outcomes.
- Contradiction records.
- Merge decisions.
- Authorised ontology updates.

Raw agent output is not eligible for permanent graph admission.

Unvalidated hypotheses are not eligible for permanent graph admission.

Untraceable evidence is not eligible for permanent graph admission.

---

# Graph Element Types

The graph contains Nodes and Relationships.

Every element must have:

- A globally unique identifier.
- A defined type.
- A current status.
- A creation timestamp.
- A provenance record.
- An audit reference.
- A revision history.

---

# Node Types

## Knowledge Node

Represents a validated Knowledge Record admitted through the Memory Engine.

Examples:

- Water scarcity increases agricultural pressure.
- Aging infrastructure creates energy reliability risks.

---

## Concept Node

Represents a defined concept used to organise knowledge.

Examples:

- Water Scarcity
- Migration
- Food Security
- Energy Infrastructure

A Concept Node does not automatically represent a validated factual claim.

---

## Event Node

Represents a traceable event relevant to one or more Knowledge Records.

Examples:

- Drought
- Power Grid Failure
- Supply Chain Disruption

An Event Node must identify its source or originating record.

---

## Evidence Node

Represents validated evidence used by the knowledge system.

An Evidence Node must reference its Evidence Record and source provenance.

---

## Risk Node

Represents a validated or explicitly classified risk.

Examples:

- Food Supply Risk
- Energy Reliability Risk
- Economic Instability Risk

A Risk Node must not be presented as certain harm unless the supporting knowledge justifies that claim.

---

## Opportunity Node

Represents a validated or explicitly classified opportunity.

Examples:

- Water Infrastructure Investment
- Renewable Energy Expansion
- Agricultural Technology Adoption

---

## Agent Node

Represents an agent or contributing entity when attribution is required.

Agent Nodes may link to contributions and events.

Agent Nodes do not represent authority or truth.

---

## Investigation Node

Represents an auditable CivilOS investigation.

It may connect:

- Questions
- Hypotheses
- Evidence
- Validation decisions
- Knowledge Records
- Agent contributions

---

# Relationship Types

CivilOS may support relationships including:

- `supports`
- `contradicts`
- `influences`
- `contributes_to`
- `increases`
- `decreases`
- `depends_on`
- `derived_from`
- `validated_by`
- `supported_by`
- `challenged_by`
- `revises`
- `replaces`
- `deprecated_by`
- `associated_with`
- `observed_during`
- `produced_by`
- `reused_in`

Relationship types must have documented meanings.

Agents must not invent uncontrolled synonyms for existing relationship types.

New relationship types require ontology review.

---

# Relationship Semantics

## Causal Relationship

Examples:

- `causes`
- `increases`
- `decreases`
- `contributes_to`

A causal relationship requires evidence supporting causation.

Correlation alone is insufficient.

Temporal sequence alone is insufficient.

Language-model plausibility is insufficient.

---

## Evidentiary Relationship

Examples:

- `supports`
- `contradicts`
- `supported_by`

An evidentiary relationship connects evidence to a claim, hypothesis, or Knowledge Record.

---

## Provenance Relationship

Examples:

- `derived_from`
- `produced_by`
- `validated_by`

A provenance relationship records origin, authorship, process, or validation history.

---

## Revision Relationship

Examples:

- `revises`
- `replaces`
- `deprecated_by`

A revision relationship preserves knowledge evolution.

Old knowledge must not be silently removed.

---

## Associative Relationship

Example:

- `associated_with`

An associative relationship must not be interpreted as causation.

The relationship must retain its weaker semantic meaning.

---

# Relationship Proposal

Relationships begin as proposals.

A Relationship Proposal must contain:

```json
{
  "proposal_id": "RP001",
  "source_node_id": "KN001",
  "relationship_type": "contributes_to",
  "target_node_id": "KN002",
  "proposed_by": "A001",
  "domain": "climate_migration",
  "evidence_references": ["E001", "E002"],
  "reasoning_summary": "Validated water stress evidence contributes to migration pressure under specified conditions.",
  "created_at": "timestamp",
  "status": "proposed"
}
```

A Relationship Proposal is not a permanent graph relationship.

---

# Relationship Validation Requirements

A proposed relationship may be admitted only when:

- The source node exists.
- The target node exists.
- Both nodes have eligible statuses.
- The relationship type is defined.
- Supporting evidence exists.
- Evidence is traceable.
- The relationship meaning matches the evidence.
- Required criticism has occurred.
- Required independent validation has occurred.
- Material contradictions are documented.
- The validation decision is recorded.
- No unresolved blocking condition exists.

All required conditions must pass.

---

# Independent Validation Rule

The agent proposing a relationship cannot be its sole validator.

The agent that created a source claim cannot solely validate the resulting relationship.

At least one independent validation record is required under the active graph policy.

Agreement without documented review does not count as independent validation.

---

# Graph Admission Gate

A validated Relationship Proposal must pass the Graph Admission Gate.

The Graph Admission Gate verifies:

- Node eligibility.
- Relationship type validity.
- Evidence availability.
- Provenance completeness.
- Validation decision.
- Independent review.
- Duplicate detection.
- Conflict detection.
- Temporal validity.
- Ontology compatibility.
- Current policy version.

Possible outcomes:

- Admitted
- Rejected
- Merge Required
- Insufficient Evidence
- Revalidation Required
- Ontology Review Required

No agent may bypass the Graph Admission Gate.

---

# Node States

Every graph node must have one current state.

Allowed states:

## Proposed

The node has been proposed but is not yet admitted as a permanent graph element.

---

## Active

The node is currently eligible for use.

---

## Challenged

Material evidence or contradiction requires review.

---

## Updated

The node has been revised through an auditable process.

---

## Deprecated

The node is no longer considered currently reliable or applicable.

The historical record remains available.

---

## Merged

The node has been consolidated with another node.

The original identifier and audit history remain available.

---

## Rejected

The proposed node failed graph admission.

A rejected node must not appear as active knowledge.

---

# Relationship States

Every graph relationship must have one current state.

Allowed states:

- Proposed
- Under Review
- Active
- Challenged
- Updated
- Deprecated
- Rejected
- Revalidation Required

State changes must be recorded as graph events.

Silent state changes are not allowed.

---

# Graph Operations

The Knowledge Graph Engine exposes the following operations.

## Create Node Proposal

Input:

- Eligible source record
- Node type
- Provenance

Output:

- Proposed Node

---

## Admit Node

Input:

- Proposed Node
- Admission decision

Output:

- Active Node or Rejection Record

---

## Create Relationship Proposal

Input:

- Source Node
- Relationship Type
- Target Node
- Evidence references
- Reasoning summary

Output:

- Relationship Proposal

---

## Validate Relationship

Input:

- Relationship Proposal
- Evidence Records
- Criticism Records
- Independent validation

Output:

- Validation Decision

---

## Admit Relationship

Input:

- Validated Relationship Proposal
- Graph Admission Decision

Output:

- Active Relationship or Rejection Record

---

## Query Graph

Input:

- Query
- Context
- Status filters
- Domain filters
- Temporal filters

Output:

- Nodes
- Relationships
- Evidence references
- Validation statuses
- Provenance
- Audit references

---

## Challenge Graph Element

Input:

- Node or Relationship
- Contradictory evidence
- Challenge reason

Output:

- Challenged status
- Revalidation request

---

## Update Graph Element

Input:

- Existing element
- New validated information
- Update decision

Output:

- Updated element
- Preserved revision history

---

## Deprecate Graph Element

Input:

- Active element
- Validated deprecation decision

Output:

- Deprecated status

Historical records remain available.

---

## Merge Nodes

Input:

- Duplicate or equivalent nodes
- Merge decision

Output:

- Canonical node
- Merge relationships
- Preserved legacy identifiers

---

# Node Record Structure

Example:

```json
{
  "node_id": "KN001",
  "node_type": "knowledge",
  "canonical_label": "Water scarcity increases agricultural pressure",
  "status": "active",
  "domain": "water_security",
  "knowledge_reference": "M001",
  "validation_reference": "V001",
  "evidence_references": ["E001", "E002"],
  "valid_from": "timestamp",
  "valid_to": null,
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "version": 1,
  "audit_reference": "AUDIT001"
}
```

---

# Relationship Record Structure

Example:

```json
{
  "relationship_id": "R001",
  "source_node_id": "KN001",
  "relationship_type": "contributes_to",
  "target_node_id": "KN002",
  "status": "active",
  "domain": "water_security",
  "evidence_references": ["E001", "E002"],
  "validation_reference": "V002",
  "proposed_by": "A001",
  "validated_by": ["A002", "A005"],
  "valid_from": "timestamp",
  "valid_to": null,
  "created_at": "timestamp",
  "updated_at": "timestamp",
  "version": 1,
  "audit_reference": "AUDIT002"
}
```

---

# Provenance Requirements

Every active node and relationship must be traceable.

Required provenance includes:

- Originating investigation.
- Source Knowledge Record.
- Source Validation Decision.
- Evidence references.
- Proposing entity.
- Validating entities.
- Admission decision.
- Policy version.
- Creation timestamp.
- Revision history.

If provenance is incomplete, the element must not be admitted as active validated knowledge.

---

# Temporal Validity

Knowledge and relationships may change over time.

Every time-sensitive graph element should support:

- `valid_from`
- `valid_to`
- `observed_at`
- `recorded_at`

CivilOS must distinguish:

- When an event occurred.
- When evidence was published.
- When CivilOS recorded the information.
- When the relationship became valid.
- When the relationship stopped being valid.

Historical truth must not be overwritten by current truth.

---

# Contradiction Handling

Contradictions are first-class graph relationships.

When validated knowledge conflicts, CivilOS must:

1. Preserve both records.

2. Create or update a `contradicts` relationship.

3. Record supporting evidence for each side.

4. Mark affected elements for review when required.

5. Trigger revalidation.

6. Preserve the final decision and revision history.

Possible outcomes:

- Both claims remain active under different conditions.
- One claim becomes challenged.
- One claim becomes updated.
- One claim becomes deprecated.
- More evidence remains necessary.

CivilOS must not force false consensus.

---

# Duplicate Detection and Entity Resolution

The graph must detect possible duplicate concepts, entities, events, and Knowledge Records.

Duplicate detection may use:

- Canonical identifiers.
- Exact matching.
- Normalised names.
- Source identifiers.
- Semantic similarity as a suggestion.

Semantic similarity alone must not merge nodes automatically.

Merge decisions require review under the active graph policy.

---

# Canonicalisation Rules

Graph elements should use canonical labels and stable identifiers.

Aliases may be retained.

Example:

```json
{
  "canonical_label": "World Health Organization",
  "aliases": ["WHO"]
}
```

Canonicalisation must preserve original source wording in provenance records.

---

# Ontology Governance

Relationship and node types must be controlled.

The graph ontology must define:

- Node types.
- Relationship types.
- Required fields.
- Allowed source and target combinations.
- Validation requirements.
- Temporal requirements.
- Provenance requirements.

Ontology changes must be versioned.

New types must not silently alter the meaning of historical graph records.

---

# Graph Policy

The Knowledge Graph Engine must apply a versioned Graph Policy.

The policy defines:

- Eligible node types.
- Eligible relationship types.
- Admission requirements.
- Independent validation requirements.
- Duplicate handling.
- Merge rules.
- Challenge rules.
- Deprecation rules.
- Query visibility rules.

Every admission decision must record the applied Graph Policy version.

---

# Graph Events

The engine should record events including:

- Node Proposed
- Node Admitted
- Node Rejected
- Node Challenged
- Node Updated
- Node Deprecated
- Nodes Merged
- Relationship Proposed
- Relationship Validated
- Relationship Admitted
- Relationship Rejected
- Relationship Challenged
- Relationship Updated
- Relationship Deprecated
- Revalidation Requested
- Ontology Updated
- Graph Query Executed
- Graph Knowledge Reused

Every event must include:

- Event ID
- Event type
- Related entity ID
- Actor
- Timestamp
- Policy version
- Audit reference

---

# Trust Integration

Graph activity may generate Trust Events only after validated outcomes.

Examples:

- Validated Relationship Contribution
- Invalid Relationship Proposal
- Useful Contradiction Detection
- Successful Entity Resolution
- Unsupported Causal Claim
- Repeated Invalid Relationship Proposal

The Knowledge Graph Engine must not calculate trust.

The Trust Engine consumes eligible recorded outcomes.

---

# Memory Integration

The Memory Engine preserves validated Knowledge Records.

The Knowledge Graph Engine represents connections among eligible records.

Graph updates must not silently rewrite Memory Records.

Memory revisions may trigger graph revalidation.

Graph contradictions may trigger memory challenges.

Both systems must preserve references to each other.

---

# Validation Integration

The Knowledge Validation Engine remains responsible for validating claims and hypotheses.

The Knowledge Graph Engine validates graph admission requirements and relationship integrity.

Graph admission does not replace knowledge validation.

A valid Knowledge Record does not automatically make every proposed relationship valid.

Each relationship requires its own supporting evidence and validation.

---

# Agent Integration

Agents may:

- Propose nodes.
- Propose relationships.
- Provide evidence.
- Raise challenges.
- Participate in independent validation.

Agents may not:

- Admit permanent graph elements directly.
- Validate their own proposals alone.
- Bypass the Graph Admission Gate.
- Delete contradictory evidence.
- Convert similarity into causality.
- Create unsupported relationships.

---

# Human Oversight

Authorised reviewers may:

- Inspect nodes and relationships.
- Inspect evidence and provenance.
- Challenge graph elements.
- Request revalidation.
- Approve ontology changes.
- Review merge decisions.
- Review suspected manipulation.

Human actions must be recorded and auditable.

Human intervention must not create unsupported knowledge.

---

# Anti-Gaming Rules

CivilOS must detect or prevent:

- Duplicate relationship proposals.
- Circular validation.
- Self-validation.
- Agent agreement loops.
- Fabricated evidence references.
- Causal claims based only on similarity.
- Excessive low-value node creation.
- Replaying rewarded graph contributions.
- Coordinated mutual validation.
- Silent removal of contradictory relationships.

Suspected manipulation must enter review.

Suspected manipulation must not automatically create a penalty without validation.

---

# Query Rules

Graph queries must respect:

- Element status.
- Domain.
- Temporal validity.
- Evidence availability.
- Validation history.
- Access policy.
- Deprecation status.
- Contradiction status.

Default user-facing results should distinguish:

- Validated knowledge.
- Challenged knowledge.
- Deprecated knowledge.
- Unresolved relationships.
- Contradictory knowledge.

CivilOS must not present all graph elements as equally reliable.

---

# Result Structure

A graph query result should include:

```json
{
  "query_id": "QG001",
  "nodes": ["KN001", "KN002"],
  "relationships": ["R001"],
  "validation_status": "active",
  "evidence_references": ["E001", "E002"],
  "contradictions": [],
  "policy_version": "1.0",
  "audit_reference": "AUDIT020"
}
```

If evidence or validation is unresolved, the result must state that status explicitly.

---

# Audit Requirements

Every active relationship must be traceable through:

Relationship

↓

Graph Admission Decision

↓

Relationship Validation

↓

Source and Target Knowledge Records

↓

Validation Decisions

↓

Evidence

↓

Sources

Every graph change must preserve:

- Previous version.
- New version.
- Change reason.
- Actor.
- Timestamp.
- Policy version.
- Audit reference.

No material graph change may occur without an audit trail.

---

# Recovery and Reliability Rules

## Duplicate Processing

The same graph event must not be applied twice.

Idempotency or deduplication controls must prevent duplicate elements and duplicate Trust Events.

---

## Incomplete Processing

If admission processing stops before completion:

- No active element is created.
- The proposal remains pending or failed.
- The failure is logged.

---

## Missing Dependencies

If evidence, validation, or Memory Records are unavailable:

- Admission remains blocked.
- The missing dependency is recorded.
- No unsupported active element is created.

---

## Invalid Policy

If the active Graph Policy cannot be loaded or verified:

- New admissions stop.
- Existing graph history remains available.
- The degraded state is displayed honestly.

---

## Corrupted Element

If integrity verification fails:

- The element enters `Under Review`.
- User-facing influence may be limited.
- The audit trail remains preserved.
- Recovery actions are recorded.

---

# Privacy and Data Minimisation

The Knowledge Graph Engine should store only data required for:

- Knowledge representation.
- Evidence provenance.
- Validation.
- Auditability.
- Relationship discovery.

The graph must not infer sensitive personal attributes without a legitimate, documented, evidence-backed purpose.

Protected personal characteristics must not be used to calculate Trust or influence.

---

# Performance Principles

Correctness and traceability take priority over graph size.

CivilOS should prefer:

- Fewer validated relationships.
- Smaller auditable subgraphs.
- Clear provenance.
- Explicit uncertainty.

CivilOS should avoid:

- Large speculative graphs.
- Uncontrolled relationship creation.
- Duplicate nodes.
- Hidden inference chains.
- Unsupported causal paths.

A small validated graph is more valuable than a large invented graph.

---

# Success Criteria

The Knowledge Graph Engine succeeds when:

- Every active relationship is evidence-backed.
- Every graph element is traceable.
- Correlation is not presented as causation.
- Contradictions remain visible.
- Revisions preserve history.
- Duplicate nodes are controlled.
- Deprecated knowledge remains auditable.
- Queries expose validation status.
- Graph knowledge is reused in later investigations.
- No agent creates a permanent relationship alone.

---

# Failure Criteria

The Knowledge Graph Engine fails when:

- Unsupported relationships become active.
- An agent bypasses graph admission.
- Similarity is presented as causation.
- Contradictions are silently deleted.
- Provenance becomes unavailable.
- Historical changes are overwritten.
- Duplicate processing distorts the graph.
- Deprecated knowledge appears as current without warning.
- Graph elements cannot be audited.
- The graph displays invented certainty.

---

# Final Success Definition

The Knowledge Graph Engine succeeds when it transforms validated Knowledge Records into a connected, temporal, revisable, and auditable structure that improves future investigations.

The graph must preserve not only what CivilOS knows, but:

- Why CivilOS knows it.
- Which evidence supports it.
- Who validated it.
- When it was valid.
- What contradicts it.
- How it changed.
- Where it was reused.

---

# Core Principle

The Knowledge Graph is not a visual decoration.

The Knowledge Graph is not a collection of model-generated associations.

The Knowledge Graph is the auditable structure of validated relationships inside CivilOS.

Memory preserves knowledge.

The Knowledge Graph connects knowledge.

Validation controls admission.

Evidence supports every important relationship.

Contradictions remain visible.

History remains traceable.

No single agent creates permanent graph knowledge alone.

If a relationship is not evidence-backed, validated, traceable, and auditable, it must not be shown as knowledge.

If it is not real, it is not shown.
