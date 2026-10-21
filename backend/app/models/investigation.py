from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class InvestigationStatus(StrEnum):
    CREATED = "created"
    PLANNED = "planned"
    INVESTIGATING = "investigating"
    UNDER_REVIEW = "under_review"
    AWAITING_VALIDATION = "awaiting_validation"
    COMPLETED = "completed"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"
    REVALIDATION_REQUIRED = "revalidation_required"
    FAILED = "failed"
    CANCELLED = "cancelled"
    ESCALATED = "escalated"


@dataclass(frozen=True, slots=True)
class Investigation:
    """
    Root entity of the CivilOS knowledge lifecycle.

    Every hypothesis, evidence record, challenge,
    validation decision, Knowledge Record and
    reuse event begins inside an Investigation.
    """

    investigation_id: UUID
    question: str
    status: InvestigationStatus
    created_at: datetime
    updated_at: datetime
    closed_at: datetime | None = None

    @classmethod
    def create(cls, question: str) -> "Investigation":
        question = question.strip()

        if not question:
            raise ValueError(
                "Investigation question cannot be empty."
            )

        now = datetime.now(timezone.utc)

        return cls(
            investigation_id=uuid4(),
            question=question,
            status=InvestigationStatus.CREATED,
            created_at=now,
            updated_at=now,
        )

    def change_status(
        self,
        new_status: InvestigationStatus,
    ) -> "Investigation":
        valid_transitions = {
            InvestigationStatus.CREATED: {
                InvestigationStatus.PLANNED,
                InvestigationStatus.CANCELLED,
                InvestigationStatus.FAILED,
            },
            InvestigationStatus.PLANNED: {
                InvestigationStatus.INVESTIGATING,
                InvestigationStatus.CANCELLED,
                InvestigationStatus.FAILED,
            },
            InvestigationStatus.INVESTIGATING: {
                InvestigationStatus.UNDER_REVIEW,
                InvestigationStatus.INSUFFICIENT_EVIDENCE,
                InvestigationStatus.FAILED,
            },
            InvestigationStatus.UNDER_REVIEW: {
                InvestigationStatus.AWAITING_VALIDATION,
                InvestigationStatus.INVESTIGATING,
                InvestigationStatus.ESCALATED,
                InvestigationStatus.FAILED,
            },
            InvestigationStatus.AWAITING_VALIDATION: {
                InvestigationStatus.COMPLETED,
                InvestigationStatus.INSUFFICIENT_EVIDENCE,
                InvestigationStatus.REVALIDATION_REQUIRED,
                InvestigationStatus.FAILED,
            },
            InvestigationStatus.REVALIDATION_REQUIRED: {
                InvestigationStatus.INVESTIGATING,
                InvestigationStatus.FAILED,
            },
            InvestigationStatus.ESCALATED: {
                InvestigationStatus.INVESTIGATING,
                InvestigationStatus.UNDER_REVIEW,
                InvestigationStatus.FAILED,
            },
        }

        allowed = valid_transitions.get(
            self.status,
            set()
        )

        if new_status not in allowed:
            raise ValueError(
                f"Invalid transition: "
                f"{self.status.value} -> {new_status.value}"
            )

        now = datetime.now(timezone.utc)

        terminal_states = {
            InvestigationStatus.COMPLETED,
            InvestigationStatus.INSUFFICIENT_EVIDENCE,
            InvestigationStatus.FAILED,
            InvestigationStatus.CANCELLED,
        }

        return Investigation(
            investigation_id=self.investigation_id,
            question=self.question,
            status=new_status,
            created_at=self.created_at,
            updated_at=now,
            closed_at=(
                now
                if new_status in terminal_states
                else None
            ),
        )
