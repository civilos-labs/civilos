# CIVILOS_DATA_MODEL

## Purpose

This document defines the canonical data model of CivilOS.

The data model exists to represent the complete lifecycle of knowledge:

Question

↓

Investigation

↓

Hypothesis

↓

Evidence

↓

Criticism

↓

Validation

↓

Knowledge

↓

Memory

↓

Trust

↓

Knowledge Graph

↓

Reuse

↓

Knowledge Compounding

CivilOS is not a chat system.

CivilOS is not a message database.

CivilOS is a knowledge system.

The data model must preserve evidence, validation, provenance, revision history, contradictions, and reuse.

---

# Core Data Principle

The most important persistent object in CivilOS is:

```text
Knowledge Record
```

Not:

- Agent
- Message
- Conversation
- Prompt
- Response

Knowledge Records are the assets of the system.

Everything else exists to create, validate, preserve, connect, and reuse them.

---

# Data Model Design Goals

The model must support:

- Evidence-backed knowledge.
- Full traceability.
- Versioned history.
- Independent validation.
- Auditability.
- Controlled memory.
- Trust based on outcomes.
- Graph relationships.
- Knowledge reuse.
- Future evolution.

The model must prevent:

- Knowledge without validation.
- Knowledge without evidence.
- Trust without outcomes.
- Relationships without validation.
- Duplicate processing.
- Silent overwrites.
- Silent deletions.
- Hidden state ownership.

---

# Architectural Ownership

Every state has one owner.

| Responsibility | Owner |
|---------------|--------|
| Investigation State | Investigation |
| Task State | Task Contract |
| Hypothesis State | Hypothesis |
| Validation Outcome | Validation Decision |
| Memory Admission | Memory Admission Decision |
| Knowledge State | Knowledge Record |
| Trust History | Trust Event |
| Trust Result | Trust Calculation |
| Graph State | Graph Node / Graph Relationship |

No other component may become an alternative source of truth.

---

# Core Entities

---

## Investigation

Represents the examination of a question.

### Purpose

Acts as the root container for all work.

### Fields

```text
investigation_id
question
status
route_type
created_at
updated_at
closed_at
policy_version
audit_reference
```

### States

```text
Created
Planned
Investigating
Under Review
Completed
Insufficient Evidence
Failed
Cancelled
Escalated
```

---

## Task Contract

Represents a bounded unit of work.

### Fields

```text
task_id
investigation_id
assigned_role
objective
status
maximum_attempts
maximum_rounds
created_at
completed_at
```

### States

```text
Created
Assigned
Running
Completed
Failed
Cancelled
```

---

## Contribution

Represents a typed output.

### Fields

```text
contribution_id
investigation_id
task_id
agent_id
contribution_type
content_reference
created_at
status
```

### Contribution Types

```text
Hypothesis Proposal
Evidence Record
Scientific Review
Policy Review
Economic Review
Challenge
Validation Recommendation
Correction Proposal
Contradiction Record
```

---

## Hypothesis

Represents a claim under evaluation.

### Fields

```text
hypothesis_id
investigation_id
statement
version
status
created_at
updated_at
```

### States

```text
Proposed
Investigating
Challenged
Supported
Accepted
Rejected
Insufficient Evidence
Revalidation Required
```

Hypothesis is not knowledge.

---

## Source Record

Represents origin.

### Fields

```text
source_id
title
publisher
source_type
url_or_identifier
published_at
retrieved_at
status
```

### Source Types

```text
Article
Dataset
Research Paper
Government Record
Tool Result
Observation
Internal Knowledge
```

---

## Evidence Record

Represents information used in evaluation.

### Fields

```text
evidence_id
source_id
hypothesis_id
evidence_type
position
summary
created_at
```

### Positions

```text
Supporting
Contradicting
Contextual
```

Evidence without provenance is invalid.

---

## Challenge Record

Represents criticism.

### Fields

```text
challenge_id
hypothesis_id
submitted_by
statement
challenge_type
status
created_at
```

### Types

```text
Missing Evidence
Weak Assumption
Contradiction
Alternative Explanation
Causal Error
Methodological Issue
```

---

## Validation Decision

Represents the official validation result.

### Fields

```text
validation_id
hypothesis_id
decision
reasoning_summary
policy_version
created_at
```

### Decisions

```text
Accepted
Rejected
Insufficient Evidence
Revalidation Required
```

Validation creates eligibility.

Validation does not create knowledge.

---

## Memory Admission Decision

Represents admission review.

### Fields

```text
memory_admission_id
validation_id
decision
reason
created_at
```

### Decisions

```text
Admitted
Rejected
Merge Required
Revalidation Required
```

---

## Knowledge Record

Represents validated knowledge.

### Purpose

Most important asset of CivilOS.

### Fields

```text
knowledge_id
validation_id
current_version
knowledge_type
title
current_status
created_at
updated_at
```

### States

```text
Active
Challenged
Updated
Deprecated
Merged
Revalidation Required
```

Knowledge can never exist without:

```text
Validation
+
Memory Admission
```

---

## Knowledge Revision

Represents every change.

### Fields

```text
revision_id
knowledge_id
version
change_reason
created_at
previous_revision_id
```

Nothing important is overwritten.

---

## Trust Event

Represents outcome history.

### Fields

```text
trust_event_id
actor_id
event_type
outcome_reference
domain
created_at
```

### Examples

```text
Validated Evidence
Accepted Knowledge
Rejected Evidence
Successful Challenge
Failed Validation
```

Trust Events do not represent truth.

---

## Trust Calculation

Represents calculated trust.

### Fields

```text
trust_result_id
actor_id
domain
policy_version
trust_state
calculated_at
```

### States

```text
Unscored
Provisional
Established
Under Review
Suspended
```

---

## Graph Node

Represents graph knowledge.

### Fields

```text
node_id
knowledge_id
node_type
status
created_at
```

### Types

```text
Knowledge
Concept
Event
Risk
Opportunity
Evidence
```

---

## Relationship Proposal

Represents candidate connection.

### Fields

```text
proposal_id
source_node_id
target_node_id
relationship_type
status
created_at
```

Proposal is not relationship.

---

## Graph Relationship

Represents validated connection.

### Fields

```text
relationship_id
source_node_id
target_node_id
relationship_type
validation_reference
status
created_at
```

### States

```text
Active
Challenged
Deprecated
Updated
Rejected
```

---

## Knowledge Reuse Record

Represents compounding.

### Fields

```text
reuse_id
knowledge_id
investigation_id
purpose
outcome_reference
created_at
```

Retrieval is not reuse.

Actual influence must be recorded.

---

## Tool Receipt

Proof of execution.

### Fields

```text
tool_receipt_id
tool_name
request_reference
result_reference
status
executed_at
```

Without Tool Receipt:

```text
Tool action did not occur.
```

---

## Model Execution Record

Represents model activity.

### Fields

```text
execution_id
provider
model_id
status
created_at
cost
token_usage
```

Model output is not knowledge.

---

## Policy Version

### Fields

```text
policy_id
policy_type
version
effective_from
status
```

---

## Domain Event

Append-only history.

### Fields

```text
event_id
event_type
entity_id
occurred_at
actor
idempotency_key
```

Events are never silently deleted.

---

## Audit Record

### Fields

```text
audit_id
actor
action
entity_type
entity_id
reason
created_at
```

Every important decision must be auditable.

---

# Key Relationships

```text
Investigation
 ├── Task Contracts
 ├── Hypotheses
 └── Contributions

Hypothesis
 ├── Evidence Records
 ├── Challenges
 └── Validation Decisions

Validation Decision
 └── Memory Admission Decision

Memory Admission Decision
 └── Knowledge Record

Knowledge Record
 ├── Knowledge Revisions
 ├── Trust Events
 ├── Graph Nodes
 └── Knowledge Reuse Records

Graph Node
 └── Graph Relationships
```

---

# Required Invariants

CivilOS must never allow:

1. Knowledge without Validation.

2. Knowledge without Memory Admission.

3. Evidence without Source.

4. Positive Trust without outcome.

5. Graph Relationship without validation.

6. Tool result without Tool Receipt.

7. Duplicate event processing.

8. Silent overwrite of Knowledge.

9. Silent deletion of audit history.

10. Self-validation counted as independent review.

---

# MVP SQL Schema

```sql
CREATE TABLE investigations (
    investigation_id UUID PRIMARY KEY,
    question TEXT NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE hypotheses (
    hypothesis_id UUID PRIMARY KEY,
    investigation_id UUID NOT NULL,
    statement TEXT NOT NULL,
    version INTEGER NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (investigation_id)
        REFERENCES investigations(investigation_id)
);

CREATE TABLE sources (
    source_id UUID PRIMARY KEY,
    title TEXT NOT NULL,
    source_type VARCHAR(50),
    published_at TIMESTAMP,
    retrieved_at TIMESTAMP
);

CREATE TABLE evidence_records (
    evidence_id UUID PRIMARY KEY,
    source_id UUID NOT NULL,
    hypothesis_id UUID NOT NULL,
    position VARCHAR(50),
    summary TEXT,
    FOREIGN KEY (source_id)
        REFERENCES sources(source_id),
    FOREIGN KEY (hypothesis_id)
        REFERENCES hypotheses(hypothesis_id)
);

CREATE TABLE validation_decisions (
    validation_id UUID PRIMARY KEY,
    hypothesis_id UUID NOT NULL,
    decision VARCHAR(50) NOT NULL,
    reasoning_summary TEXT,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (hypothesis_id)
        REFERENCES hypotheses(hypothesis_id)
);

CREATE TABLE memory_admissions (
    memory_admission_id UUID PRIMARY KEY,
    validation_id UUID NOT NULL,
    decision VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (validation_id)
        REFERENCES validation_decisions(validation_id)
);

CREATE TABLE knowledge_records (
    knowledge_id UUID PRIMARY KEY,
    validation_id UUID NOT NULL,
    current_version INTEGER NOT NULL,
    current_status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (validation_id)
        REFERENCES validation_decisions(validation_id)
);

CREATE TABLE trust_events (
    trust_event_id UUID PRIMARY KEY,
    actor_id UUID NOT NULL,
    event_type VARCHAR(100) NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE graph_nodes (
    node_id UUID PRIMARY KEY,
    knowledge_id UUID NOT NULL,
    node_type VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (knowledge_id)
        REFERENCES knowledge_records(knowledge_id)
);

CREATE TABLE graph_relationships (
    relationship_id UUID PRIMARY KEY,
    source_node_id UUID NOT NULL,
    target_node_id UUID NOT NULL,
    relationship_type VARCHAR(100) NOT NULL
);
```

---

# Example Lifecycle

```text
Question:
How could water scarcity influence migration?

↓

Investigation
I001

↓

Hypothesis
H001

Water scarcity increases migration pressure

↓

Evidence
E001
E002
E003

↓

Challenge
C001

↓

Validation
V001 = Accepted

↓

Memory Admission
M001 = Admitted

↓

Knowledge Record
K001

↓

Graph Node
GN001

↓

Relationship
GN001
contributes_to
GN002

↓

Knowledge Reuse
R001
```

---

# Final Data Model Definition

CivilOS is centred on the Knowledge Record.

Everything else exists to create, validate, preserve, connect, challenge, reuse, and improve Knowledge Records.

The system's success is measured not by responses generated, but by validated knowledge accumulated and successfully reused.

---

# Core Principle

CivilOS does not persist answers.

CivilOS persists validated knowledge.

Knowledge must remain:

- Evidence-backed
- Traceable
- Auditable
- Revisable
- Reusable

If a record cannot explain where it came from, why it was accepted, how it changed, and where it was reused, it is not validated knowledge.

If it is not real, it is not shown.
