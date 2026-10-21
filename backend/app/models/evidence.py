from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class EvidencePosition(StrEnum):
    SUPPORTING = "supporting"
    CONTRADICTING = "contradicting"
    CONTEXTUAL = "contextual"


class EvidenceStatus(StrEnum):
    SUBMITTED = "submitted"
    UNDER_REVIEW = "under_review"
    VERIFIED = "verified"
    REJECTED = "rejected"
    UNRESOLVED = "unresolved"
    SUPERSEDED = "superseded"


@dataclass(frozen=True, slots=True)
class Evidence:
    """
    A traceable unit of information used to evaluate a Hypothesis.

    Evidence is not a Source.

    A Source identifies the originating document, dataset,
    observation or verified tool result.

    Evidence identifies the specific source material used to support,
    contradict or contextualise a Hypothesis.

    Meta AI may identify or summarise candidate evidence.
    Meta AI output is not automatically evidence.

    Evidence does not decide whether a Hypothesis becomes knowledge.
    That responsibility belongs to the Knowledge Validation Engine.
    """

    evidence_id: UUID
    investigation_id: UUID
    hypothesis_id: UUID
    source_id: UUID
    submitted_by: UUID
    position: EvidencePosition
    summary: str
    source_locator: str
    content_fingerprint: str
    status: EvidenceStatus
    version: int
    created_at: datetime
    updated_at: datetime
    reviewed_by: UUID | None = None
    review_reason: str | None = None
    superseded_by_id: UUID | None = None

    @classmethod
    def submit(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        source_id: UUID,
        submitted_by: UUID,
        position: EvidencePosition,
        summary: str,
        source_locator: str,
        content_fingerprint: str,
    ) -> Evidence:
        """
        Submit candidate evidence for independent review.

        Submission does not verify evidence and does not validate
        the related Hypothesis.
        """

        normalized_summary = summary.strip()
        normalized_locator = source_locator.strip()
        normalized_fingerprint = content_fingerprint.strip()

        if not normalized_summary:
            raise ValueError(
                "Evidence summary cannot be empty."
            )

        if not normalized_locator:
            raise ValueError(
                "Evidence source locator cannot be empty."
            )

        if not normalized_fingerprint:
            raise ValueError(
                "Evidence content fingerprint cannot be empty."
            )

        now = datetime.now(timezone.utc)

        return cls(
            evidence_id=uuid4(),
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            source_id=source_id,
            submitted_by=submitted_by,
            position=position,
            summary=normalized_summary,
            source_locator=normalized_locator,
            content_fingerprint=normalized_fingerprint,
            status=EvidenceStatus.SUBMITTED,
            version=1,
            created_at=now,
            updated_at=now,
        )

    def start_review(
        self,
        *,
        reviewer_id: UUID,
    ) -> Evidence:
        """
        Begin independent evidence review.

        The submitting actor cannot be the reviewer.
        """

        if self.status != EvidenceStatus.SUBMITTED:
            raise ValueError(
                "Only submitted evidence can enter review."
            )

        self._ensure_independent_reviewer(reviewer_id)

        return self._copy_with(
            status=EvidenceStatus.UNDER_REVIEW,
            reviewed_by=reviewer_id,
            review_reason=None,
        )

    def verify(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Evidence:
        """
        Mark evidence as verified after independent review.

        Verified evidence may participate in validation.
        Verification does not make the Hypothesis true.
        """

        if self.status != EvidenceStatus.UNDER_REVIEW:
            raise ValueError(
                "Evidence must be under review before verification."
            )

        self._ensure_independent_reviewer(reviewer_id)
        normalized_reason = self._normalize_review_reason(reason)

        return self._copy_with(
            status=EvidenceStatus.VERIFIED,
            reviewed_by=reviewer_id,
            review_reason=normalized_reason,
        )

    def reject(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Evidence:
        """
        Reject evidence that fails provenance, relevance,
        integrity or verification requirements.
        """

        if self.status not in {
            EvidenceStatus.SUBMITTED,
            EvidenceStatus.UNDER_REVIEW,
            EvidenceStatus.UNRESOLVED,
        }:
            raise ValueError(
                f"Evidence in status '{self.status.value}' "
                "cannot be rejected."
            )

        self._ensure_independent_reviewer(reviewer_id)
        normalized_reason = self._normalize_review_reason(reason)

        return self._copy_with(
            status=EvidenceStatus.REJECTED,
            reviewed_by=reviewer_id,
            review_reason=normalized_reason,
        )

    def mark_unresolved(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Evidence:
        """
        Record that the evidence cannot currently be verified
        or rejected responsibly.

        Unresolved evidence cannot support Knowledge acceptance.
        """

        if self.status not in {
            EvidenceStatus.SUBMITTED,
            EvidenceStatus.UNDER_REVIEW,
        }:
            raise ValueError(
                f"Evidence in status '{self.status.value}' "
                "cannot become unresolved."
            )

        self._ensure_independent_reviewer(reviewer_id)
        normalized_reason = self._normalize_review_reason(reason)

        return self._copy_with(
            status=EvidenceStatus.UNRESOLVED,
            reviewed_by=reviewer_id,
            review_reason=normalized_reason,
        )

    def revise(
        self,
        *,
        summary: str,
        source_locator: str,
        content_fingerprint: str,
    ) -> Evidence:
        """
        Create a new version of candidate evidence.

        The previous version must remain stored by persistence.
        A revised version returns to submitted status and requires
        a new independent review.
        """

        if self.status not in {
            EvidenceStatus.REJECTED,
            EvidenceStatus.UNRESOLVED,
        }:
            raise ValueError(
                "Only rejected or unresolved evidence can be revised."
            )

        normalized_summary = summary.strip()
        normalized_locator = source_locator.strip()
        normalized_fingerprint = content_fingerprint.strip()

        if not normalized_summary:
            raise ValueError(
                "Revised evidence summary cannot be empty."
            )

        if not normalized_locator:
            raise ValueError(
                "Revised source locator cannot be empty."
            )

        if not normalized_fingerprint:
            raise ValueError(
                "Revised content fingerprint cannot be empty."
            )

        if (
            normalized_summary == self.summary
            and normalized_locator == self.source_locator
            and normalized_fingerprint == self.content_fingerprint
        ):
            raise ValueError(
                "Revised evidence must contain a material change."
            )

        return self._copy_with(
            summary=normalized_summary,
            source_locator=normalized_locator,
            content_fingerprint=normalized_fingerprint,
            status=EvidenceStatus.SUBMITTED,
            version=self.version + 1,
            reviewed_by=None,
            review_reason=None,
            superseded_by_id=None,
        )

    def supersede(
        self,
        *,
        replacement_evidence_id: UUID,
    ) -> Evidence:
        """
        Mark this evidence version as superseded without deleting it.
        """

        if replacement_evidence_id == self.evidence_id:
            raise ValueError(
                "Evidence cannot supersede itself."
            )

        if self.status == EvidenceStatus.SUPERSEDED:
            raise ValueError(
                "Evidence is already superseded."
            )

        return self._copy_with(
            status=EvidenceStatus.SUPERSEDED,
            superseded_by_id=replacement_evidence_id,
        )

    def _ensure_independent_reviewer(
        self,
        reviewer_id: UUID,
    ) -> None:
        if reviewer_id == self.submitted_by:
            raise ValueError(
                "Evidence cannot be independently reviewed "
                "by the actor that submitted it."
            )

    @staticmethod
    def _normalize_review_reason(
        reason: str,
    ) -> str:
        normalized_reason = reason.strip()

        if not normalized_reason:
            raise ValueError(
                "Evidence review reason cannot be empty."
            )

        return normalized_reason

    def _copy_with(
        self,
        *,
        summary: str | None = None,
        source_locator: str | None = None,
        content_fingerprint: str | None = None,
        status: EvidenceStatus | None = None,
        version: int | None = None,
        reviewed_by: UUID | None = None,
        review_reason: str | None = None,
        superseded_by_id: UUID | None = None,
    ) -> Evidence:
        """
        Return a new immutable Evidence state.

        Persistence must store Domain Events and Audit Records
        for material transitions.
        """

        return Evidence(
            evidence_id=self.evidence_id,
            investigation_id=self.investigation_id,
            hypothesis_id=self.hypothesis_id,
            source_id=self.source_id,
            submitted_by=self.submitted_by,
            position=self.position,
            summary=(
                summary
                if summary is not None
                else self.summary
            ),
            source_locator=(
                source_locator
                if source_locator is not None
                else self.source_locator
            ),
            content_fingerprint=(
                content_fingerprint
                if content_fingerprint is not None
                else self.content_fingerprint
            ),
            status=status or self.status,
            version=(
                version
                if version is not None
                else self.version
            ),
            created_at=self.created_at,
            updated_at=datetime.now(timezone.utc),
            reviewed_by=reviewed_by,
            review_reason=review_reason,
            superseded_by_id=superseded_by_id,
        )
