from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class ChallengeType(StrEnum):
    MISSING_EVIDENCE = "missing_evidence"
    WEAK_ASSUMPTION = "weak_assumption"
    CONTRADICTION = "contradiction"
    ALTERNATIVE_EXPLANATION = "alternative_explanation"
    CAUSAL_OVERREACH = "causal_overreach"
    METHODOLOGICAL_ISSUE = "methodological_issue"
    INVALID_PROVENANCE = "invalid_provenance"
    CONFLICT_OF_INTEREST = "conflict_of_interest"
    SCOPE_ERROR = "scope_error"
    TEMPORAL_ERROR = "temporal_error"


class ChallengeStatus(StrEnum):
    OPEN = "open"
    RESPONDED = "responded"
    RESOLVED = "resolved"
    UNRESOLVED = "unresolved"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"
    SUPERSEDED = "superseded"


class ChallengeResolution(StrEnum):
    SUSTAINED = "sustained"
    PARTIALLY_SUSTAINED = "partially_sustained"
    OVERRULED = "overruled"
    MORE_EVIDENCE_REQUIRED = "more_evidence_required"
    HYPOTHESIS_REVISION_REQUIRED = "hypothesis_revision_required"
    REVALIDATION_REQUIRED = "revalidation_required"


@dataclass(frozen=True, slots=True)
class Challenge:
    """
    A documented criticism raised during a CivilOS Investigation.

    A Challenge is not a rejection.

    A Challenge identifies a material weakness, contradiction,
    missing dependency, invalid inference or alternative explanation
    that must be examined before knowledge can be admitted.

    Meta AI agents and authorised participants may raise Challenges.

    No agent may resolve its own Challenge alone.

    Challenge resolution does not create Knowledge. It contributes
    to the record evaluated by the Knowledge Validation Engine.
    """

    challenge_id: UUID
    investigation_id: UUID
    hypothesis_id: UUID
    submitted_by: UUID
    challenge_type: ChallengeType
    statement: str
    rationale: str
    status: ChallengeStatus
    version: int
    evidence_ids: tuple[UUID, ...]
    created_at: datetime
    updated_at: datetime
    responded_by: UUID | None = None
    response: str | None = None
    resolved_by: UUID | None = None
    resolution: ChallengeResolution | None = None
    resolution_reason: str | None = None
    superseded_by_id: UUID | None = None

    def __post_init__(self) -> None:
        if not self.statement.strip():
            raise ValueError(
                "Challenge statement cannot be empty."
            )

        if not self.rationale.strip():
            raise ValueError(
                "Challenge rationale cannot be empty."
            )

        if self.version < 1:
            raise ValueError(
                "Challenge version must be at least 1."
            )

        if len(self.evidence_ids) != len(set(self.evidence_ids)):
            raise ValueError(
                "Challenge evidence references must be unique."
            )

        if self.response is not None and not self.response.strip():
            raise ValueError(
                "Challenge response cannot be empty when provided."
            )

        if (
            self.resolution_reason is not None
            and not self.resolution_reason.strip()
        ):
            raise ValueError(
                "Challenge resolution reason cannot be empty "
                "when provided."
            )

        if self.status == ChallengeStatus.RESPONDED:
            if self.responded_by is None or self.response is None:
                raise ValueError(
                    "A responded Challenge requires a respondent "
                    "and response."
                )

        if self.status == ChallengeStatus.RESOLVED:
            if (
                self.resolved_by is None
                or self.resolution is None
                or self.resolution_reason is None
            ):
                raise ValueError(
                    "A resolved Challenge requires a reviewer, "
                    "resolution and reason."
                )

        if self.status == ChallengeStatus.SUPERSEDED:
            if self.superseded_by_id is None:
                raise ValueError(
                    "A superseded Challenge requires a replacement."
                )

    @classmethod
    def raise_challenge(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        submitted_by: UUID,
        challenge_type: ChallengeType,
        statement: str,
        rationale: str,
        evidence_ids: tuple[UUID, ...] = (),
    ) -> Challenge:
        """
        Raise a new Challenge against a Hypothesis.

        A Challenge requires a statement and rationale.

        Evidence references are optional because certain logical,
        methodological or scope objections may be valid before new
        evidence is available.

        Raising a Challenge does not reject the Hypothesis.
        """

        normalized_statement = statement.strip()
        normalized_rationale = rationale.strip()
        unique_evidence_ids = tuple(dict.fromkeys(evidence_ids))

        if not normalized_statement:
            raise ValueError(
                "Challenge statement cannot be empty."
            )

        if not normalized_rationale:
            raise ValueError(
                "Challenge rationale cannot be empty."
            )

        now = datetime.now(timezone.utc)

        return cls(
            challenge_id=uuid4(),
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            submitted_by=submitted_by,
            challenge_type=challenge_type,
            statement=normalized_statement,
            rationale=normalized_rationale,
            status=ChallengeStatus.OPEN,
            version=1,
            evidence_ids=unique_evidence_ids,
            created_at=now,
            updated_at=now,
        )

    def respond(
        self,
        *,
        respondent_id: UUID,
        response: str,
        evidence_ids: tuple[UUID, ...] = (),
    ) -> Challenge:
        """
        Record a response to an open or unresolved Challenge.

        A response does not resolve the Challenge.

        The original Challenge remains preserved and an independent
        reviewer must evaluate the complete record.
        """

        if self.status not in {
            ChallengeStatus.OPEN,
            ChallengeStatus.UNRESOLVED,
        }:
            raise ValueError(
                f"Challenge in status '{self.status.value}' "
                "cannot receive a response."
            )

        normalized_response = response.strip()

        if not normalized_response:
            raise ValueError(
                "Challenge response cannot be empty."
            )

        combined_evidence_ids = tuple(
            dict.fromkeys(
                self.evidence_ids + evidence_ids
            )
        )

        return replace(
            self,
            status=ChallengeStatus.RESPONDED,
            evidence_ids=combined_evidence_ids,
            responded_by=respondent_id,
            response=normalized_response,
            resolved_by=None,
            resolution=None,
            resolution_reason=None,
            updated_at=datetime.now(timezone.utc),
        )

    def resolve(
        self,
        *,
        reviewer_id: UUID,
        resolution: ChallengeResolution,
        reason: str,
    ) -> Challenge:
        """
        Resolve a Challenge through independent review.

        Resolution records whether the Challenge was sustained,
        partially sustained, overruled, or requires further action.

        Resolution does not accept or reject the Hypothesis directly.
        """

        if self.status not in {
            ChallengeStatus.OPEN,
            ChallengeStatus.RESPONDED,
            ChallengeStatus.UNRESOLVED,
        }:
            raise ValueError(
                f"Challenge in status '{self.status.value}' "
                "cannot be resolved."
            )

        self._ensure_independent_reviewer(reviewer_id)

        normalized_reason = reason.strip()

        if not normalized_reason:
            raise ValueError(
                "Challenge resolution reason cannot be empty."
            )

        return replace(
            self,
            status=ChallengeStatus.RESOLVED,
            resolved_by=reviewer_id,
            resolution=resolution,
            resolution_reason=normalized_reason,
            updated_at=datetime.now(timezone.utc),
        )

    def mark_unresolved(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Challenge:
        """
        Record that the Challenge cannot currently be resolved.

        Unresolved material Challenges remain visible to Validation.
        """

        if self.status not in {
            ChallengeStatus.OPEN,
            ChallengeStatus.RESPONDED,
        }:
            raise ValueError(
                f"Challenge in status '{self.status.value}' "
                "cannot become unresolved."
            )

        self._ensure_independent_reviewer(reviewer_id)

        normalized_reason = reason.strip()

        if not normalized_reason:
            raise ValueError(
                "Unresolved Challenge reason cannot be empty."
            )

        return replace(
            self,
            status=ChallengeStatus.UNRESOLVED,
            resolved_by=reviewer_id,
            resolution=None,
            resolution_reason=normalized_reason,
            updated_at=datetime.now(timezone.utc),
        )

    def reject_as_invalid(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Challenge:
        """
        Reject a Challenge that lacks material relevance, contains
        invalid reasoning, duplicates an existing Challenge, or fails
        the applicable Challenge policy.

        Disagreement alone is not enough to reject a Challenge.
        """

        if self.status not in {
            ChallengeStatus.OPEN,
            ChallengeStatus.RESPONDED,
            ChallengeStatus.UNRESOLVED,
        }:
            raise ValueError(
                f"Challenge in status '{self.status.value}' "
                "cannot be rejected."
            )

        self._ensure_independent_reviewer(reviewer_id)

        normalized_reason = reason.strip()

        if not normalized_reason:
            raise ValueError(
                "Challenge rejection reason cannot be empty."
            )

        return replace(
            self,
            status=ChallengeStatus.REJECTED,
            resolved_by=reviewer_id,
            resolution=None,
            resolution_reason=normalized_reason,
            updated_at=datetime.now(timezone.utc),
        )

    def withdraw(
        self,
        *,
        requested_by: UUID,
        reason: str,
    ) -> Challenge:
        """
        Withdraw a Challenge by the actor that submitted it.

        Withdrawal preserves the Challenge and its history.
        """

        if requested_by != self.submitted_by:
            raise ValueError(
                "Only the submitting actor may withdraw a Challenge."
            )

        if self.status not in {
            ChallengeStatus.OPEN,
            ChallengeStatus.UNRESOLVED,
        }:
            raise ValueError(
                f"Challenge in status '{self.status.value}' "
                "cannot be withdrawn."
            )

        normalized_reason = reason.strip()

        if not normalized_reason:
            raise ValueError(
                "Challenge withdrawal reason cannot be empty."
            )

        return replace(
            self,
            status=ChallengeStatus.WITHDRAWN,
            resolution_reason=normalized_reason,
            updated_at=datetime.now(timezone.utc),
        )

    def revise(
        self,
        *,
        statement: str,
        rationale: str,
        evidence_ids: tuple[UUID, ...] = (),
    ) -> Challenge:
        """
        Create a new version of an unresolved or rejected Challenge.

        Persistence must preserve the previous version before saving
        the returned version.
        """

        if self.status not in {
            ChallengeStatus.UNRESOLVED,
            ChallengeStatus.REJECTED,
        }:
            raise ValueError(
                "Only unresolved or rejected Challenges "
                "can be revised."
            )

        normalized_statement = statement.strip()
        normalized_rationale = rationale.strip()
        unique_evidence_ids = tuple(dict.fromkeys(evidence_ids))

        if not normalized_statement:
            raise ValueError(
                "Revised Challenge statement cannot be empty."
            )

        if not normalized_rationale:
            raise ValueError(
                "Revised Challenge rationale cannot be empty."
            )

        if (
            normalized_statement == self.statement
            and normalized_rationale == self.rationale
            and unique_evidence_ids == self.evidence_ids
        ):
            raise ValueError(
                "Revised Challenge must contain a material change."
            )

        return replace(
            self,
            statement=normalized_statement,
            rationale=normalized_rationale,
            status=ChallengeStatus.OPEN,
            version=self.version + 1,
            evidence_ids=unique_evidence_ids,
            responded_by=None,
            response=None,
            resolved_by=None,
            resolution=None,
            resolution_reason=None,
            superseded_by_id=None,
            updated_at=datetime.now(timezone.utc),
        )

    def supersede(
        self,
        *,
        replacement_challenge_id: UUID,
    ) -> Challenge:
        """
        Mark this Challenge as superseded while preserving its history.
        """

        if replacement_challenge_id == self.challenge_id:
            raise ValueError(
                "Challenge cannot supersede itself."
            )

        if self.status == ChallengeStatus.SUPERSEDED:
            raise ValueError(
                "Challenge is already superseded."
            )

        return replace(
            self,
            status=ChallengeStatus.SUPERSEDED,
            superseded_by_id=replacement_challenge_id,
            updated_at=datetime.now(timezone.utc),
        )

    def _ensure_independent_reviewer(
        self,
        reviewer_id: UUID,
    ) -> None:
        if reviewer_id == self.submitted_by:
            raise ValueError(
                "The submitting actor cannot independently "
                "resolve or reject the same Challenge."
            )

        if (
            self.responded_by is not None
            and reviewer_id == self.responded_by
        ):
            raise ValueError(
                "The responding actor cannot independently "
                "resolve or reject the same Challenge."
            )
