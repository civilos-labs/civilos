# Trust Engine

## Purpose

The Trust Engine calculates the evidence-based influence of agents and other contributing entities inside CivilOS.

Trust is not reputation.

Trust is not popularity.

Trust is not authority.

Trust is the measurable history of validated contributions and validated failures.

The Trust Engine exists to help CivilOS determine how much evidentiary weight a contribution may receive during collective reasoning.

The Trust Engine does not determine truth.

Evidence, criticism, and collective validation determine whether a claim may become knowledge.

---

# Core Question

The Trust Engine must answer:

How has this entity performed in comparable, validated situations?

It must not answer:

Which entity is always right?

No entity is always right.

Every contribution remains subject to evidence review, criticism, and validation.

---

# Core Trust Principles

1. Trust is earned through recorded outcomes.

2. Trust cannot be assigned manually.

3. Trust must remain traceable to specific events.

4. Trust must be specific to a role, domain, and task context.

5. High trust cannot bypass evidence or validation.

6. Low trust cannot automatically invalidate strong evidence.

7. Activity alone does not create trust.

8. Agreement with other agents does not automatically create trust.

9. Disagreement does not automatically reduce trust.

10. Unresolved activity must not be scored as success or failure.

11. Duplicate events must not affect trust more than once.

12. If trust cannot be calculated from recorded evidence, it must not be displayed.

---

# What Trust Represents

Trust represents historical performance across observable dimensions.

CivilOS may maintain the following trust dimensions.

## Evidence Reliability

Measures whether evidence contributed by an entity survives evidence review.

---

## Validation Reliability

Measures whether an entity's validation decisions remain consistent with final collective outcomes.

---

## Knowledge Contribution

Measures whether an entity contributes knowledge that passes validation and enters memory.

---

## Critical Reasoning

Measures whether an entity identifies real weaknesses, contradictions, missing evidence, or causal overreach.

---

## Collaboration Quality

Measures whether an entity improves collective reasoning through useful, traceable contributions.

Collaboration does not mean agreement.

Constructive disagreement may improve collaboration quality.

---

## Correction Quality

Measures whether an entity recognises, corrects, and helps repair previous errors.

Self-correction may be recorded positively when the correction is supported by evidence and completed before harmful knowledge admission.

---

# Domain-Specific Trust

Trust must be contextual.

An entity may have strong performance in one domain and limited evidence in another.

Examples:

- Scientific Evidence Validation
- Economic Impact Analysis
- Policy Analysis
- Source Verification
- Critical Reasoning
- Knowledge Graph Validation

CivilOS must not convert domain-specific performance into universal authority.

A Science Agent with strong scientific evidence performance does not automatically receive greater influence in policy interpretation.

A Policy Agent with strong regulatory performance does not automatically receive greater influence in scientific validation.

Trust must follow relevant demonstrated competence.

---

# Trust States

Every trust profile must have one of the following states.

## Unscored

Insufficient validated events exist.

No trust value should be displayed.

---

## Provisional

Some validated events exist, but the history remains limited.

Any displayed result must be labelled provisional.

---

## Established

Sufficient validated history exists under the active trust policy.

The supporting event ledger remains available.

---

## Under Review

New contradictory outcomes, suspected duplication, invalid provenance, or integrity concerns require review.

Influence may be limited until review is completed.

---

## Suspended

The trust profile cannot currently influence collective reasoning because of unresolved integrity or provenance failures.

Suspension is not permanent deletion.

The historical record remains available.

---

# Trust Event Model

Trust is derived from recorded Trust Events.

Every Trust Event must contain:

```json
{
  "event_id": "TE001",
  "entity_id": "A001",
  "entity_role": "Research Agent",
  "domain": "source_verification",
  "event_type": "validated_evidence_contribution",
  "related_investigation_id": "I001",
  "related_hypothesis_id": "H001",
  "related_validation_id": "V001",
  "outcome_status": "confirmed",
  "created_at": "timestamp",
  "source_references": ["E001"],
  "deduplication_key": "I001-H001-V001-A001",
  "audit_reference": "AUDIT001"
}
```

A Trust Event without provenance, related records, and an audit reference is invalid.

---

# Eligible Positive Events

Positive trust evidence may be created when a recorded contribution has a validated beneficial outcome.

Eligible events include:

## Validated Evidence Contribution

Evidence provided by the entity passes evidence review and materially supports a validation decision.

---

## Accepted Knowledge Contribution

A contribution by the entity becomes part of accepted knowledge after collective validation and Memory Admission Gate approval.

---

## Successful Cross-Validation

The entity performs an independent review that is supported by the final auditable outcome.

---

## Useful Critical Challenge

The entity identifies a documented weakness, contradiction, missing source, or invalid inference that improves the final outcome.

---

## Successful Correction

The entity identifies and helps correct an earlier error through validated evidence.

---

## Useful Memory Contribution

The entity contributes validated knowledge that is later retrieved and demonstrably supports a future investigation.

Reuse must be recorded.

It must not be assumed.

---

# Eligible Negative Events

Negative trust evidence may be created only after an auditable failure outcome.

Eligible events include:

## Rejected Evidence Submission

The entity submits evidence that fails the defined evidence standards.

A source that is merely unresolved must not automatically count as rejected.

---

## Unsupported Claim

The entity presents a material claim without required evidence or provenance.

---

## Failed Validation

The entity approves or rejects a hypothesis through reasoning that fails documented validation requirements.

---

## Invalid Knowledge Contribution

A proposed contribution fails Memory Admission because required validation, provenance, or evidence is missing.

---

## Repeated Critical Error

The entity repeats a previously documented and relevant error after the error was available in Failure Memory.

The repetition must be demonstrable.

---

## Hidden Contradictory Evidence

The entity ignores material contradictory evidence that was available and relevant to the active investigation.

The omission must be recorded and reviewed before affecting trust.

---

# Events That Must Not Affect Trust

The following must not change trust by themselves:

- Number of messages generated.
- Number of tokens used.
- Number of hypotheses proposed.
- Agreement with a high-trust agent.
- Disagreement with a low-trust agent.
- Speed of response without quality validation.
- Stylistic quality.
- Confidence expressed by a language model.
- Popularity.
- Seniority.
- Task participation alone.
- Unresolved evidence.
- Incomplete investigations.
- Cancelled investigations.
- Duplicate processing of an existing event.

CivilOS rewards validated contribution quality, not activity volume.

---

# Event Eligibility Rules

A Trust Event becomes eligible only when:

- The related investigation exists.
- The related entity is identified.
- The associated evidence or validation record exists.
- The event outcome is final under the current workflow.
- Provenance is complete.
- The event has not already been applied.
- No unresolved integrity condition blocks processing.

Events associated with incomplete investigations remain pending.

Pending events do not affect trust.

---

# Trust Calculation Model

The Trust Engine calculates trust from eligible Trust Events.

Trust must be multidimensional.

A single global score must not replace domain-specific evidence.

The calculation process must include:

1. Select the relevant entity.

2. Select the relevant domain and role.

3. Retrieve eligible Trust Events.

4. Remove duplicates.

5. Separate confirmed, pending, reversed, and disputed events.

6. Apply the active versioned trust policy.

7. Produce dimension results.

8. Produce an explanation and audit trail.

9. Determine whether enough evidence exists to display a result.

---

# Trust Policy

Scoring weights must not be hidden or embedded without documentation.

CivilOS must maintain a versioned Trust Policy.

The Trust Policy defines:

- Eligible event types.
- Positive and negative event treatment.
- Domain mappings.
- Minimum evidence requirements.
- Provisional status rules.
- Review rules.
- Suspension rules.
- Reversal rules.

Example:

```json
{
  "policy_id": "TP001",
  "version": "1.0",
  "status": "active",
  "effective_from": "timestamp",
  "event_rules": {
    "validated_evidence_contribution": {
      "dimension": "evidence_reliability",
      "effect": "positive"
    },
    "unsupported_claim": {
      "dimension": "evidence_reliability",
      "effect": "negative"
    }
  }
}
```

Weights must be calibrated using real test results.

Until calibration exists, CivilOS may display the event history and trust state without presenting a numeric score.

CivilOS must not invent precision.

---

# Numeric Score Rule

A numeric trust score is optional.

A numeric score may be displayed only when:

- The scoring policy is documented.
- The policy version is visible.
- Enough eligible events exist.
- The result is domain-specific.
- The result can be reproduced from the event ledger.
- The result includes the supporting history.
- The system identifies provisional or uncertain results.

If these conditions are not met, display:

- Unscored
- Provisional
- Under Review
- Suspended

Do not display a fabricated percentage.

---

# Influence Calculation

Trust may influence review priority or contribution weighting.

Trust must never replace evidence.

Influence must be constrained by:

- Domain relevance.
- Current evidence quality.
- Active trust state.
- Validation requirements.
- Conflict-of-interest rules.
- Independent review requirements.

High trust may increase review weight.

High trust may not produce automatic acceptance.

Low trust may trigger additional review.

Low trust may not produce automatic rejection.

The contribution must always be evaluated on its current evidence.

---

# Separation of Responsibilities

## Knowledge Validation Engine

Decides whether a hypothesis meets validation requirements.

---

## Memory Engine

Stores admitted validated knowledge and preserves its history.

---

## Trust Engine

Calculates historical performance from recorded events.

---

## Knowledge Graph Engine

Represents validated entities and relationships.

---

## Agent Orchestration Engine

Coordinates participating agents and workflows.

---

The Trust Engine does not:

- Validate evidence.
- Accept hypotheses.
- Create knowledge.
- Admit knowledge into memory.
- Create Knowledge Graph relationships.
- Override criticism.

---

# Self-Evaluation Rule

An entity cannot create or approve a Trust Event about itself.

Trust Events must be generated from system outcomes or independent review.

Self-reported success has no trust effect unless independently validated.

---

# Conflict-of-Interest Rule

An entity that proposed a hypothesis must not be the sole validator of the same hypothesis.

An entity that submitted evidence must not be the sole reviewer of that evidence.

An entity may participate in later review, but independent validation remains required.

---

# Anti-Gaming Rules

CivilOS must detect or prevent:

- Duplicate evidence submissions.
- Duplicate Trust Events.
- Artificial task splitting to generate extra positive events.
- Agreement loops between agents.
- Repeated low-value contributions.
- Self-validation.
- Circular validation.
- Coordinated mutual trust inflation.
- Withholding contradictory evidence.
- Replaying previously rewarded contributions.

Suspected gaming events must be marked `Under Review`.

Suspected gaming must not automatically produce a penalty without review.

---

# Trust Reversal and Correction

Trust history must be revisable when:

- Evidence is later invalidated.
- Accepted knowledge becomes deprecated.
- A duplicate event is discovered.
- The applied policy contained an error.
- Provenance is found to be incomplete.
- A previous validation decision is reversed.

The system must create reversal events.

Historical events must not be silently deleted.

Example:

```json
{
  "event_id": "TE009",
  "event_type": "trust_event_reversal",
  "reverses_event_id": "TE001",
  "reason": "Supporting evidence was invalidated",
  "created_at": "timestamp"
}
```

---

# Policy Versioning

Every calculated trust result must record:

- Trust Policy ID
- Trust Policy version
- Calculation timestamp
- Eligible events used
- Reversed events excluded
- Domain
- Entity role

A policy update must not silently rewrite historical calculations.

Historical results must remain reproducible under their original policy.

Recalculated results must be stored as new calculation records.

---

# Trust Result Structure

Example:

```json
{
  "trust_result_id": "TR001",
  "entity_id": "A001",
  "entity_role": "Research Agent",
  "domain": "source_verification",
  "state": "provisional",
  "dimensions": {
    "evidence_reliability": {
      "validated_events": 4,
      "negative_events": 1
    },
    "critical_reasoning": {
      "validated_events": 2,
      "negative_events": 0
    }
  },
  "policy_id": "TP001",
  "policy_version": "1.0",
  "calculated_at": "timestamp",
  "event_references": ["TE001", "TE002", "TE003"],
  "audit_reference": "AUDIT010"
}
```

The numbers in this example describe recorded event counts.

The example does not define a universal scoring formula.

---

# Trust Explanation

Every displayed trust result must answer:

- Which entity is being evaluated?
- For which role?
- In which domain?
- Under which policy?
- Which events were used?
- Which events were excluded?
- Is the result provisional or established?
- Can the result be independently reproduced?

If CivilOS cannot answer these questions, the result must not be displayed.

---

# Audit Requirements

Every Trust Event must be traceable to:

Trust Event

↓

System Outcome

↓

Validation or Memory Record

↓

Hypothesis

↓

Evidence

↓

Sources

Every trust calculation must retain:

- Input events.
- Applied policy.
- Calculation result.
- Excluded events.
- Reversal history.
- Timestamp.
- Audit reference.

No trust change may exist without an audit trail.

---

# Recovery and Reliability Rules

## Duplicate Processing

The same Trust Event must not be applied twice.

The deduplication key must prevent repeated application.

---

## Incomplete Processing

If calculation stops before completion:

- No new result is published.
- The previous valid result remains available.
- The failed calculation is logged.

---

## Missing Dependencies

If related validation or evidence records are unavailable:

- The event remains pending or enters review.
- The event must not affect trust.
- The missing dependency must be recorded.

---

## Policy Failure

If the active Trust Policy cannot be loaded or validated:

- Numeric trust must not be calculated.
- Existing audit history remains available.
- The system displays the unavailable status truthfully.

---

# Human Oversight

Authorised reviewers may:

- Inspect Trust Events.
- Challenge an event.
- Request recalculation.
- Review suspected gaming.
- Review suspended profiles.
- Approve policy changes.

Human intervention must be recorded.

Human intervention must not silently assign trust.

---

# Privacy and Data Minimisation

The Trust Engine evaluates contribution history, not personal identity.

The system should store only information required for:

- Attribution.
- Validation.
- Auditability.
- Integrity review.

CivilOS must not infer trust from protected personal characteristics.

CivilOS must not use irrelevant personal data to calculate influence.

---

# Success Criteria

The Trust Engine succeeds when:

- Every trust result is reproducible.
- Every trust result is domain-specific.
- Every trust result maps to recorded events.
- Duplicate events do not distort results.
- Reversed outcomes update trust transparently.
- High trust never bypasses evidence.
- Low trust never automatically invalidates evidence.
- Insufficient history is displayed honestly.
- Policy versions remain auditable.

---

# Failure Criteria

The Trust Engine fails when:

- Trust is assigned manually.
- Trust is based on popularity or activity volume.
- Numeric scores lack a documented policy.
- An entity validates itself.
- Duplicate events change trust multiple times.
- High trust bypasses validation.
- Low trust causes automatic rejection.
- Historical changes are silently deleted.
- Trust cannot be explained.
- Trust cannot be audited.

---

# Final Success Definition

The Trust Engine succeeds when influence reflects relevant, validated, reproducible contribution history without becoming authority, popularity, or a substitute for evidence.

Trust supports collective reasoning.

Trust does not decide truth.

---

# Core Principle

Trust is not reputation.

Trust is not authority.

Trust is not certainty.

Trust is the auditable history of validated contributions and validated failures within a relevant domain.

Evidence determines whether a claim is supported.

Validation determines whether a hypothesis may become knowledge.

Trust records how an entity has performed across those processes.

High trust never bypasses evidence.

If trust cannot be measured, explained, reproduced, and audited, it must not be shown.
