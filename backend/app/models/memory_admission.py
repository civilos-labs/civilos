from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class MemoryAdmissionOutcome(StrEnum):
    ADMITTED = "admitted"
    REJECTED = "rejected"
    MERGE_REQUIRED = "merge_required"
    REVALIDATION_REQUIRED = "revalidation_required"


class AdmissionCheckStatus(StrEnum):
    PASSED = "passed"
    FAILED = "failed"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True, slots=True)
class AdmissionCheckResult:
    """
    Result of applying one explicit Memory Admission rule.

    A check result is not a complete Memory Admission Decision.
    """

    check_id: str
    status: AdmissionCheckStatus
    reason: str

    def __post_init__(self) -> None:
        normalized_check_id = self.check_id.strip()
        normalized_reason = self.reason.strip()

        if not normalized_check_id:
            raise ValueError(
                "Memory Admission check ID cannot be empty."
            )

        if not normalized_reason:
            raise ValueError(
                "Memory Admission check reason cannot be empty."
            )

        object.__setattr__(
            self,
            "check_id",
            normalized_check_id,
        )
        object.__setattr__(
            self,
            "reason",
            normalized_reason,
        )


@dataclass(frozen=True, slots=True)
class MemoryAdmissionDecision:
    """
    Immutable decision controlling entry into persistent CivilOS memory.

    An accepted Validation Decision creates eligibility.

    It does not create a KnowledgeRecord automatically.

    Memory Admission verifies that the validated result remains
    traceable, complete, non-duplicative and suitable for persistent
    storage.

    Meta AI may create contributions and recommendations.

    Meta AI cannot admit its own output into permanent memory.
    """

    memory_admission_id: UUID
    investigation_id: UUID
    hypothesis_id: UUID
    validation_id: UUID
    decided_by: UUID
    outcome: MemoryAdmissionOutcome
    reason: str
    evidence_ids: tuple[UUID, ...]
    check_results: tuple[AdmissionCheckResult, ...]
    policy_id: str
    policy_version: str
    created_at: datetime
    existing_knowledge_id: UUID | None = None
    supersedes_admission_id: UUID | None = None

    def __post_init__(self) -> None:
        normalized_reason = self.reason.strip()
        normalized_policy_id = self.policy_id.strip()
        normalized_policy_version = self.policy_version.strip()

        if not normalized_reason:
            raise ValueError(
                "Memory Admission reason cannot be empty."
            )

        if not normalized_policy_id:
            raise ValueError(
                "Memory Admission policy ID cannot be empty."
            )

        if not normalized_policy_version:
            raise ValueError(
                "Memory Admission policy version cannot be empty."
            )

        if len(self.evidence_ids) != len(set(self.evidence_ids)):
            raise ValueError(
                "Memory Admission evidence references must be unique."
            )

        check_ids = tuple(
            result.check_id
            for result in self.check_results
        )

        if len(check_ids) != len(set(check_ids)):
            raise ValueError(
                "Memory Admission checks must use unique IDs."
            )

        if (
            self.outcome == MemoryAdmissionOutcome.MERGE_REQUIRED
            and self.existing_knowledge_id is None
        ):
            raise ValueError(
                "Merge-required admission must reference "
                "existing knowledge."
            )

        if (
            self.outcome != MemoryAdmissionOutcome.MERGE_REQUIRED
            and self.existing_knowledge_id is not None
        ):
            raise ValueError(
                "Existing knowledge may be referenced only "
                "for a merge-required decision."
            )

        if (
            self.outcome
            == MemoryAdmissionOutcome.REVALIDATION_REQUIRED
            and self.supersedes_admission_id is None
        ):
            raise ValueError(
                "Revalidation-required admission must reference "
                "a previous Memory Admission Decision."
            )

        object.__setattr__(
            self,
            "reason",
            normalized_reason,
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
        validation_id: UUID,
        decided_by: UUID,
        validating_actor_ids: tuple[UUID, ...],
        validation_was_accepted: bool,
        outcome: MemoryAdmissionOutcome,
        reason: str,
        evidence_ids: tuple[UUID, ...],
        check_results: tuple[AdmissionCheckResult, ...],
        policy_id: str,
        policy_version: str,
        existing_knowledge_id: UUID | None = None,
        supersedes_admission_id: UUID | None = None,
    ) -> MemoryAdmissionDecision:
        """
        Create an immutable Memory Admission Decision.

        Structural checks occur here.

        Persistence must additionally verify that referenced
        Investigation, Hypothesis, Validation, Evidence and Knowledge
        records exist and are eligible.
        """

        unique_validating_actor_ids = tuple(
            dict.fromkeys(validating_actor_ids)
        )
        unique_evidence_ids = tuple(
            dict.fromkeys(evidence_ids)
        )

        normalized_reason = reason.strip()
        normalized_policy_id = policy_id.strip()
        normalized_policy_version = policy_version.strip()

        if not validation_was_accepted:
            raise ValueError(
                "Only an accepted Validation Decision is eligible "
                "for Memory Admission."
            )

        if decided_by in unique_validating_actor_ids:
            raise ValueError(
                "A Validation reviewer cannot independently make "
                "the Memory Admission Decision for the same result."
            )

        if not normalized_reason:
            raise ValueError(
                "Memory Admission reason cannot be empty."
            )

        if not normalized_policy_id:
            raise ValueError(
                "Memory Admission policy ID cannot be empty."
            )

        if not normalized_policy_version:
            raise ValueError(
                "Memory Admission policy version cannot be empty."
            )

        cls._validate_check_results(check_results)

        if outcome == MemoryAdmissionOutcome.ADMITTED:
            cls._validate_admission_requirements(
                evidence_ids=unique_evidence_ids,
                check_results=check_results,
            )

        if (
            outcome == MemoryAdmissionOutcome.MERGE_REQUIRED
            and existing_knowledge_id is None
        ):
            raise ValueError(
                "Merge-required admission must reference "
                "existing knowledge."
            )

        if (
            outcome
            == MemoryAdmissionOutcome.REVALIDATION_REQUIRED
            and supersedes_admission_id is None
        ):
            raise ValueError(
                "Revalidation-required admission must reference "
                "a previous admission."
            )

        return cls(
            memory_admission_id=uuid4(),
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            validation_id=validation_id,
            decided_by=decided_by,
            outcome=outcome,
            reason=normalized_reason,
            evidence_ids=unique_evidence_ids,
            check_results=check_results,
            policy_id=normalized_policy_id,
            policy_version=normalized_policy_version,
            created_at=datetime.now(timezone.utc),
            existing_knowledge_id=existing_knowledge_id,
            supersedes_admission_id=supersedes_admission_id,
        )

    @classmethod
    def admit(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        validation_id: UUID,
        decided_by: UUID,
        validating_actor_ids: tuple[UUID, ...],
        validation_was_accepted: bool,
        reason: str,
        evidence_ids: tuple[UUID, ...],
        check_results: tuple[AdmissionCheckResult, ...],
        policy_id: str,
        policy_version: str,
    ) -> MemoryAdmissionDecision:
        """
        Admit validated material as eligible for KnowledgeRecord
        creation.

        Persistence must create the KnowledgeRecord atomically with
        this decision, the Domain Event and the Audit Record.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            validation_id=validation_id,
            decided_by=decided_by,
            validating_actor_ids=validating_actor_ids,
            validation_was_accepted=validation_was_accepted,
            outcome=MemoryAdmissionOutcome.ADMITTED,
            reason=reason,
            evidence_ids=evidence_ids,
            check_results=check_results,
            policy_id=policy_id,
            policy_version=policy_version,
        )

    @classmethod
    def reject(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        validation_id: UUID,
        decided_by: UUID,
        validating_actor_ids: tuple[UUID, ...],
        validation_was_accepted: bool,
        reason: str,
        evidence_ids: tuple[UUID, ...],
        check_results: tuple[AdmissionCheckResult, ...],
        policy_id: str,
        policy_version: str,
    ) -> MemoryAdmissionDecision:
        """
        Reject persistent storage without changing the earlier
        Validation Decision.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            validation_id=validation_id,
            decided_by=decided_by,
            validating_actor_ids=validating_actor_ids,
            validation_was_accepted=validation_was_accepted,
            outcome=MemoryAdmissionOutcome.REJECTED,
            reason=reason,
            evidence_ids=evidence_ids,
            check_results=check_results,
            policy_id=policy_id,
            policy_version=policy_version,
        )

    @classmethod
    def require_merge(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        validation_id: UUID,
        decided_by: UUID,
        validating_actor_ids: tuple[UUID, ...],
        validation_was_accepted: bool,
        reason: str,
        evidence_ids: tuple[UUID, ...],
        check_results: tuple[AdmissionCheckResult, ...],
        policy_id: str,
        policy_version: str,
        existing_knowledge_id: UUID,
    ) -> MemoryAdmissionDecision:
        """
        Record that candidate knowledge overlaps existing knowledge
        and requires a controlled merge instead of duplication.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            validation_id=validation_id,
            decided_by=decided_by,
            validating_actor_ids=validating_actor_ids,
            validation_was_accepted=validation_was_accepted,
            outcome=MemoryAdmissionOutcome.MERGE_REQUIRED,
            reason=reason,
            evidence_ids=evidence_ids,
            check_results=check_results,
            policy_id=policy_id,
            policy_version=policy_version,
            existing_knowledge_id=existing_knowledge_id,
        )

    @classmethod
    def require_revalidation(
        cls,
        *,
        investigation_id: UUID,
        hypothesis_id: UUID,
        validation_id: UUID,
        decided_by: UUID,
        validating_actor_ids: tuple[UUID, ...],
        validation_was_accepted: bool,
        reason: str,
        evidence_ids: tuple[UUID, ...],
        check_results: tuple[AdmissionCheckResult, ...],
        policy_id: str,
        policy_version: str,
        supersedes_admission_id: UUID,
    ) -> MemoryAdmissionDecision:
        """
        Stop admission when a material contradiction, missing
        dependency or integrity concern requires revalidation.
        """

        return cls.decide(
            investigation_id=investigation_id,
            hypothesis_id=hypothesis_id,
            validation_id=validation_id,
            decided_by=decided_by,
            validating_actor_ids=validating_actor_ids,
            validation_was_accepted=validation_was_accepted,
            outcome=MemoryAdmissionOutcome.REVALIDATION_REQUIRED,
            reason=reason,
            evidence_ids=evidence_ids,
            check_results=check_results,
            policy_id=policy_id,
            policy_version=policy_version,
            supersedes_admission_id=supersedes_admission_id,
        )

    @staticmethod
    def _validate_check_results(
        check_results: tuple[AdmissionCheckResult, ...],
    ) -> None:
        if not check_results:
            raise ValueError(
                "Memory Admission requires explicit check results."
            )

        check_ids = tuple(
            result.check_id
            for result in check_results
        )

        if len(check_ids) != len(set(check_ids)):
            raise ValueError(
                "Memory Admission check IDs must be unique."
            )

    @staticmethod
    def _validate_admission_requirements(
        *,
        evidence_ids: tuple[UUID, ...],
        check_results: tuple[AdmissionCheckResult, ...],
    ) -> None:
        if not evidence_ids:
            raise ValueError(
                "Admitted knowledge requires evidence references."
            )

        failed_checks = tuple(
            result.check_id
            for result in check_results
            if result.status == AdmissionCheckStatus.FAILED
        )

        if failed_checks:
            failed_list = ", ".join(failed_checks)

            raise ValueError(
                "Knowledge cannot be admitted with failed checks: "
                f"{failed_list}"
            )

        passed_checks = tuple(
            result
            for result in check_results
            if result.status == AdmissionCheckStatus.PASSED
        )

        if not passed_checks:
            raise ValueError(
                "Knowledge Admission requires at least one "
                "passed check."
            )
