from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class HypothesisStatus(StrEnum):
    PROPOSED = "proposed"
    INVESTIGATING = "investigating"
    CHALLENGED = "challenged"
    SUPPORTED = "supported"
    CROSS_VALIDATED = "cross_validated"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"
    REVALIDATION_REQUIRED = "revalidation_required"


@dataclass(frozen=True, slots=True)
class Hypothesis:
    """
    A provisional claim evaluated inside a CivilOS Investigation.

    A Hypothesis is not knowledge.

    Meta AI agents and other authorised actors may propose hypotheses,
    evidence, criticism and validation recommendations.

    Only CivilOS validation and admission processes may transform an
    accepted Hypothesis into a persistent KnowledgeRecord.
    """

    hypothesis_id: UUID
    investigation_id: UUID
    statement: str
    proposed_by: UUID
    status: HypothesisStatus
    version: int
    created_at: datetime
    updated_at: datetime

    @classmethod
    def propose(
        cls,
        *,
        investigation_id: UUID,
        statement: str,
        proposed_by: UUID,
    ) -> "Hypothesis":
        """
        Create a new provisional hypothesis.

        Creating a Hypothesis does not validate it and does not create
        permanent knowledge.
        """

        normalized_statement = statement.strip()

        if not normalized_statement:
            raise ValueError(
                "Hypothesis statement cannot be empty."
            )

        now = datetime.now(timezone.utc)

        return cls(
            hypothesis_id=uuid4(),
            investigation_id=investigation_id,
            statement=normalized_statement,
            proposed_by=proposed_by,
            status=HypothesisStatus.PROPOSED,
            version=1,
            created_at=now,
            updated_at=now,
        )

    def start_investigation(self) -> "Hypothesis":
        """
        Move a proposed hypothesis into active investigation.
        """

        return self._transition_to(
            HypothesisStatus.INVESTIGATING
        )

    def challenge(self) -> "Hypothesis":
        """
        Mark the hypothesis as challenged.

        A challenge does not automatically reject the hypothesis.
        """

        return self._transition_to(
            HypothesisStatus.CHALLENGED
        )

    def mark_supported(self) -> "Hypothesis":
        """
        Record that eligible supporting evidence exists.

        Supported does not mean accepted.
        """

        return self._transition_to(
            HypothesisStatus.SUPPORTED
        )

    def mark_cross_validated(self) -> "Hypothesis":
        """
        Record completion of the required independent review.

        Cross-validation does not itself create knowledge.
        """

        return self._transition_to(
            HypothesisStatus.CROSS_VALIDATED
        )

    def accept(self) -> "Hypothesis":
        """
        Record an accepted validation outcome.

        Acceptance creates eligibility for Memory Admission.
        It does not directly create a KnowledgeRecord.
        """

        return self._transition_to(
            HypothesisStatus.ACCEPTED
        )

    def reject(self) -> "Hypothesis":
        """
        Record a rejected validation outcome.

        Rejected hypotheses cannot become accepted knowledge.
        """

        return self._transition_to(
            HypothesisStatus.REJECTED
        )

    def mark_insufficient_evidence(self) -> "Hypothesis":
        """
        Record that available evidence cannot responsibly support
        acceptance or rejection.
        """

        return self._transition_to(
            HypothesisStatus.INSUFFICIENT_EVIDENCE
        )

    def require_revalidation(self) -> "Hypothesis":
        """
        Require a new validation process after a material challenge
        or new contradictory evidence.
        """

        return self._transition_to(
            HypothesisStatus.REVALIDATION_REQUIRED
        )

    def revise_statement(
        self,
        new_statement: str,
    ) -> "Hypothesis":
        """
        Create a new version of the hypothesis statement.

        The caller must persist the previous version before saving
        the returned version.
        """

        if self.status not in {
            HypothesisStatus.PROPOSED,
            HypothesisStatus.INVESTIGATING,
            HypothesisStatus.CHALLENGED,
            HypothesisStatus.INSUFFICIENT_EVIDENCE,
            HypothesisStatus.REVALIDATION_REQUIRED,
        }:
            raise ValueError(
                f"Hypothesis in status '{self.status.value}' "
                "cannot be revised."
            )

        normalized_statement = new_statement.strip()

        if not normalized_statement:
            raise ValueError(
                "Revised hypothesis statement cannot be empty."
            )

        if normalized_statement == self.statement:
            raise ValueError(
                "Revised hypothesis statement must be different."
            )

        return Hypothesis(
            hypothesis_id=self.hypothesis_id,
            investigation_id=self.investigation_id,
            statement=normalized_statement,
            proposed_by=self.proposed_by,
            status=HypothesisStatus.PROPOSED,
            version=self.version + 1,
            created_at=self.created_at,
            updated_at=datetime.now(timezone.utc),
        )

    def _transition_to(
        self,
        new_status: HypothesisStatus,
    ) -> "Hypothesis":
        """
        Apply a controlled and auditable-ready state transition.

        Actual persistence must create the corresponding Domain Event
        and Audit Record.
        """

        valid_transitions = {
            HypothesisStatus.PROPOSED: {
                HypothesisStatus.INVESTIGATING,
            },
            HypothesisStatus.INVESTIGATING: {
                HypothesisStatus.CHALLENGED,
                HypothesisStatus.SUPPORTED,
                HypothesisStatus.REJECTED,
                HypothesisStatus.INSUFFICIENT_EVIDENCE,
            },
            HypothesisStatus.CHALLENGED: {
                HypothesisStatus.INVESTIGATING,
                HypothesisStatus.SUPPORTED,
                HypothesisStatus.REJECTED,
                HypothesisStatus.INSUFFICIENT_EVIDENCE,
                HypothesisStatus.REVALIDATION_REQUIRED,
            },
            HypothesisStatus.SUPPORTED: {
                HypothesisStatus.CHALLENGED,
                HypothesisStatus.CROSS_VALIDATED,
                HypothesisStatus.REJECTED,
                HypothesisStatus.INSUFFICIENT_EVIDENCE,
            },
            HypothesisStatus.CROSS_VALIDATED: {
                HypothesisStatus.ACCEPTED,
                HypothesisStatus.REJECTED,
                HypothesisStatus.INSUFFICIENT_EVIDENCE,
                HypothesisStatus.REVALIDATION_REQUIRED,
            },
            HypothesisStatus.ACCEPTED: {
                HypothesisStatus.REVALIDATION_REQUIRED,
            },
            HypothesisStatus.INSUFFICIENT_EVIDENCE: {
                HypothesisStatus.INVESTIGATING,
                HypothesisStatus.REVALIDATION_REQUIRED,
            },
            HypothesisStatus.REVALIDATION_REQUIRED: {
                HypothesisStatus.INVESTIGATING,
                HypothesisStatus.CHALLENGED,
            },
        }

        allowed_statuses = valid_transitions.get(
            self.status,
            set(),
        )

        if new_status not in allowed_statuses:
            raise ValueError(
                "Invalid hypothesis transition: "
                f"{self.status.value} -> {new_status.value}"
            )

        return Hypothesis(
            hypothesis_id=self.hypothesis_id,
            investigation_id=self.investigation_id,
            statement=self.statement,
            proposed_by=self.proposed_by,
            status=new_status,
            version=self.version,
            created_at=self.created_at,
            updated_at=datetime.now(timezone.utc),
        )
