from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class ValidationOutcome(StrEnum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"
    REVALIDATION_REQUIRED = "revalidation_required"


class ValidationRuleStatus(StrEnum):
    PASSED = "passed"
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True, slots=True)
class ValidationRuleResult:
    """
    Result of applying one explicit validation rule.

    A rule result is not a final Validation Decision.
    """

    rule_id: str
    status: ValidationRuleStatus
    reason: str

    def __post_init__(self) -> None:
        normalized_rule_id = self.rule_id.strip()
        normalized_reason = self.reason.strip()

        if not normalized_rule_id:
            raise ValueError(
                "Validation rule ID cannot be empty."
            )

        if not normalized_reason:
            raise ValueError(
                "Validation rule reason cannot be empty."
            )

        object.__setattr__(
            self,
            "rule_id",
            normalized_rule_id,
        )
        object.__setattr__(
            self,
            "reason",
            normalized_reason,
        )


@dataclass(frozen=True, slots=True)
class ValidationDecision:
    """
    Immutable and auditable decision about one Hypothesis version.

    A ValidationDecision determines whether the Hypothesis is eligible
    to continue to the Memory Admission Gate.

    Acceptance does not create a KnowledgeRecord.

    Trust, agent confidence, model confidence and majority agreement
    cannot replace evidence, criticism or independent validation.

    Meta AI agents may contribute analysis and recommendations.
    Meta AI cannot admit its own output as permanent knowledge.
    """

    validation_id: UUID
    investigation_id: UUID
    hypothesis_id: UUID
    hypothesis_version: int
    outcome: ValidationOutcome
    reasoning_summary: str
    evidence_ids: tuple[UUID, ...]
    challenge_ids: tuple[UUID, ...]
    validator_ids: tuple[UUID, ...]
    rule_results: tuple[ValidationRuleResult, ...]
    policy_id: str
    policy_version: str
    created_at: datetime
    supersedes_validation_id: UUID | None = None

    MINIMUM_INDEPENDENT_VALIDATORS = 2

    def __post_init__(self) -> None:
        normalized_summary = self.reasoning_summary.strip()
        normalized_policy_id = self.policy_id.strip()
        normalized_policy_version = self.policy_version.strip()

        if self.hypothesis_version < 1:
            raise ValueError(
                "Hypothesis version must be at least 1."
            )

        if not normalized_summary:
            raise ValueError(
                "Validation reasoning summary cannot be empty."
            )

        if not normalized_policy_id:
            raise ValueError(
                "Validation policy ID cannot be empty."
            )

        if not normalized_policy_version:
            raise ValueError(
                "Validation policy version cannot be empty."
            )

        if len(self.evidence_ids) != len(set(self.evidence_ids)):
            raise ValueError(
                "Validation evidence references must be unique."
            )

        if len(self.challenge_ids) != len(set(self.challenge_ids)):
            raise ValueError(
                "Validation Challenge references must be unique."
            )

        if len(self.validator_ids) != len(set(self.validator_ids)):
            raise ValueError(
                "Validation reviewers must be unique."
            )

        rule_ids = tuple(
            result.rule_id
            for result in self.rule_results
        )

        if len(rule_ids) != len(set(rule_ids)):
            raise ValueError(
                "Validation rule results must use unique rule IDs."
            )

        object.__setattr__(
            self,
            "reasoning_summary",
            normalized_summary,
        )
        object.__setattr__(
            self,
            "policy_id",
            normalized_policy_id,
        )
        object.__setattr__(
            self,
            "policy_version",
            normalized_policy_version,
        )

    @classmethod
    def decide(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        hypothesis_version: int,
        outcome: ValidationOutcome,
        reasoning_summary: str,
        evidence_ids: tuple[UUID, ...],
        challenge_ids: tuple[UUID, ...],
        validator_ids: tuple[UUID, ...],
        proposing_actor_id: UUID,
        rule_results: tuple[ValidationRuleResult, ...],
        policy_id: str,
        policy_version: str,
        supersedes_validation_id: UUID | None = None,
    ) -> ValidationDecision:
        """
        Create an immutable Validation Decision.

        This method verifies structural validation requirements.
        Persistence must separately verify that referenced records exist
        and that Evidence, Challenge and reviewer states are eligible.
        """

        normalized_summary = reasoning_summary.strip()
        normalized_policy_id = policy_id.strip()
        normalized_policy_version = policy_version.strip()

        unique_evidence_ids = tuple(
            dict.fromkeys(evidence_ids)
        )
        unique_challenge_ids = tuple(
            dict.fromkeys(challenge_ids)
        )
        unique_validator_ids = tuple(
            dict.fromkeys(validator_ids)
        )

        if hypothesis_version < 1:
            raise ValueError(
                "Hypothesis version must be at least 1."
            )

        if not normalized_summary:
            raise ValueError(
                "Validation reasoning summary cannot be empty."
            )

        if not normalized_policy_id:
            raise ValueError(
                "Validation policy ID cannot be empty."
            )

        if not normalized_policy_version:
            raise ValueError(
                "Validation policy version cannot be empty."
            )

        if not unique_validator_ids:
            raise ValueError(
                "Validation requires at least one independent reviewer."
            )

        if proposing_actor_id in unique_validator_ids:
            raise ValueError(
                "The proposing actor cannot independently validate "
                "the same Hypothesis."
            )

        cls._validate_rule_results(rule_results)

        if outcome == ValidationOutcome.ACCEPTED:
            cls._validate_acceptance_requirements(
                evidence_ids=unique_evidence_ids,
                validator_ids=unique_validator_ids,
                rule_results=rule_results,
            )

        if (
            outcome == ValidationOutcome.REVALIDATION_REQUIRED
            and supersedes_validation_id is None
        ):
            raise ValueError(
                "Revalidation requires a previous Validation Decision."
            )

        now = datetime.now(timezone.utc)

        return cls(
            validation_id=uuid4(),
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            hypothesis_version=hypothesis_version,
            outcome=outcome,
            reasoning_summary=normalized_summary,
            evidence_ids=unique_evidence_ids,
            challenge_ids=unique_challenge_ids,
            validator_ids=unique_validator_ids,
            rule_results=rule_results,
            policy_id=normalized_policy_id,
            policy_version=normalized_policy_version,
            created_at=now,
            supersedes_validation_id=supersedes_validation_id,
        )

    @classmethod
    def accept(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        hypothesis_version: int,
        reasoning_summary: str,
        evidence_ids: tuple[UUID, ...],
        challenge_ids: tuple[UUID, ...],
        validator_ids: tuple[UUID, ...],
        proposing_actor_id: UUID,
        rule_results: tuple[ValidationRuleResult, ...],
        policy_id: str,
        policy_version: str,
        supersedes_validation_id: UUID | None = None,
    ) -> ValidationDecision:
        """
        Accept a Hypothesis as eligible for Memory Admission.

        This method does not create permanent knowledge.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            hypothesis_version=hypothesis_version,
            outcome=ValidationOutcome.ACCEPTED,
            reasoning_summary=reasoning_summary,
            evidence_ids=evidence_ids,
            challenge_ids=challenge_ids,
            validator_ids=validator_ids,
            proposing_actor_id=proposing_actor_id,
            rule_results=rule_results,
            policy_id=policy_id,
            policy_version=policy_version,
            supersedes_validation_id=supersedes_validation_id,
        )

    @classmethod
    def reject(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        hypothesis_version: int,
        reasoning_summary: str,
        evidence_ids: tuple[UUID, ...],
        challenge_ids: tuple[UUID, ...],
        validator_ids: tuple[UUID, ...],
        proposing_actor_id: UUID,
        rule_results: tuple[ValidationRuleResult, ...],
        policy_id: str,
        policy_version: str,
        supersedes_validation_id: UUID | None = None,
    ) -> ValidationDecision:
        """
        Reject a Hypothesis after documented independent review.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            hypothesis_version=hypothesis_version,
            outcome=ValidationOutcome.REJECTED,
            reasoning_summary=reasoning_summary,
            evidence_ids=evidence_ids,
            challenge_ids=challenge_ids,
            validator_ids=validator_ids,
            proposing_actor_id=proposing_actor_id,
            rule_results=rule_results,
            policy_id=policy_id,
            policy_version=policy_version,
            supersedes_validation_id=supersedes_validation_id,
        )

    @classmethod
    def record_insufficient_evidence(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        hypothesis_version: int,
        reasoning_summary: str,
        evidence_ids: tuple[UUID, ...],
        challenge_ids: tuple[UUID, ...],
        validator_ids: tuple[UUID, ...],
        proposing_actor_id: UUID,
        rule_results: tuple[ValidationRuleResult, ...],
        policy_id: str,
        policy_version: str,
        supersedes_validation_id: UUID | None = None,
    ) -> ValidationDecision:
        """
        Record that evidence cannot responsibly support acceptance
        or rejection.

        Insufficient evidence is a complete and honest outcome.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            hypothesis_version=hypothesis_version,
            outcome=ValidationOutcome.INSUFFICIENT_EVIDENCE,
            reasoning_summary=reasoning_summary,
            evidence_ids=evidence_ids,
            challenge_ids=challenge_ids,
            validator_ids=validator_ids,
            proposing_actor_id=proposing_actor_id,
            rule_results=rule_results,
            policy_id=policy_id,
            policy_version=policy_version,
            supersedes_validation_id=supersedes_validation_id,
        )

    @classmethod
    def require_revalidation(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        hypothesis_version: int,
        reasoning_summary: str,
        evidence_ids: tuple[UUID, ...],
        challenge_ids: tuple[UUID, ...],
        validator_ids: tuple[UUID, ...],
        proposing_actor_id: UUID,
        rule_results: tuple[ValidationRuleResult, ...],
        policy_id: str,
        policy_version: str,
        supersedes_validation_id: UUID,
    ) -> ValidationDecision:
        """
        Require revalidation after material new evidence, criticism
        or dependency invalidation.

        The earlier Validation Decision remains preserved.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            hypothesis_version=hypothesis_version,
            outcome=ValidationOutcome.REVALIDATION_REQUIRED,
            reasoning_summary=reasoning_summary,
            evidence_ids=evidence_ids,
            challenge_ids=challenge_ids,
            validator_ids=validator_ids,
            proposing_actor_id=proposing_actor_id,
            rule_results=rule_results,
            policy_id=policy_id,
            policy_version=policy_version,
            supersedes_validation_id=supersedes_validation_id,
        )

    @staticmethod
    def _validate_rule_results(
        rule_results: tuple[ValidationRuleResult, ...],
    ) -> None:
        if not rule_results:
            raise ValueError(
                "Validation requires explicit rule results."
            )

        rule_ids = tuple(
            result.rule_id
            for result in rule_results
        )

        if len(rule_ids) != len(set(rule_ids)):
            raise ValueError(
                "Validation rule IDs must be unique."
            )

    @classmethod
    def _validate_acceptance_requirements(
        cls,
        *,
        evidence_ids: tuple[UUID, ...],
        validator_ids: tuple[UUID, ...],
        rule_results: tuple[ValidationRuleResult, ...],
    ) -> None:
        if not evidence_ids:
            raise ValueError(
                "Accepted validation requires evidence."
            )

        if (
            len(validator_ids)
            < cls.MINIMUM_INDEPENDENT_VALIDATORS
        ):
            raise ValueError(
                "Accepted validation requires at least "
                f"{cls.MINIMUM_INDEPENDENT_VALIDATORS} "
                "independent validators."
            )

        failed_rules = tuple(
            result.rule_id
            for result in rule_results
            if result.status == ValidationRuleStatus.FAILED
        )

        if failed_rules:
            failed_list = ", ".join(failed_rules)

            raise ValueError(
                "Accepted validation cannot contain failed rules: "
                f"{failed_list}"
            )

        passed_rules = tuple(
            result
            for result in rule_results
            if result.status == ValidationRuleStatus.PASSED
        )

        if not passed_rules:
            raise ValueError(
                "Accepted validation requires at least one "
                "passed rule."
            )
