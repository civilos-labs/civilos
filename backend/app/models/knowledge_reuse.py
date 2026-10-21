from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class ReusePurpose(StrEnum):
    HYPOTHESIS_CREATION = "hypothesis_creation"
    EVIDENCE_ASSESSMENT = "evidence_assessment"
    CHALLENGE_ANALYSIS = "challenge_analysis"
    VALIDATION_SUPPORT = "validation_support"
    INVESTIGATION_PLANNING = "investigation_planning"
    KNOWLEDGE_EVOLUTION = "knowledge_evolution"


class ReuseImpact(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass(frozen=True, slots=True)
class KnowledgeReuse:
    """
    Auditable record proving that existing knowledge influenced
    a later investigation.

    Reading knowledge is not reuse.

    Reuse exists only when knowledge materially influences
    decisions, evidence evaluation, validation activities,
    investigation planning or new knowledge creation.
    """

    reuse_id: UUID
    knowledge_id: UUID
    investigation_id: UUID
    used_by: UUID
    purpose: ReusePurpose
    impact: ReuseImpact
    justification: str
    outcome_summary: str
    created_at: datetime

    @classmethod
    def record(
        cls,
        *,
        knowledge_id: UUID,
        investigation_id: UUID,
        used_by: UUID,
        purpose: ReusePurpose,
        impact: ReuseImpact,
        justification: str,
        outcome_summary: str,
    ) -> "KnowledgeReuse":
        normalized_justification = justification.strip()
        normalized_outcome = outcome_summary.strip()

        if not normalized_justification:
            raise ValueError(
                "Reuse justification cannot be empty."
            )

        if not normalized_outcome:
            raise ValueError(
                "Reuse outcome summary cannot be empty."
            )

        return cls(
            reuse_id=uuid4(),
            knowledge_id=knowledge_id,
            investigation_id=investigation_id,
            used_by=used_by,
            purpose=purpose,
            impact=impact,
            justification=normalized_justification,
            outcome_summary=normalized_outcome,
            created_at=datetime.now(timezone.utc),
        )
