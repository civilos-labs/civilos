from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class KnowledgeType(StrEnum):
    FACT = "fact"
    DISCOVERY = "discovery"
    STRATEGY = "strategy"
    FAILURE = "failure"


class KnowledgeStatus(StrEnum):
    ACTIVE = "active"
    CHALLENGED = "challenged"
    UPDATED = "updated"
    DEPRECATED = "deprecated"
    MERGED = "merged"
    REVALIDATION_REQUIRED = "revalidation_required"


@dataclass(frozen=True, slots=True)
class KnowledgeRecord:
    """
    Primary persistent asset of CivilOS.

    A KnowledgeRecord can be created only after:
    1. A hypothesis has completed validation.
    2. The validation decision accepted the hypothesis.
    3. The Memory Admission Gate admitted the result.
    4. Supporting evidence remains traceable.

    Agents create contributions.
    CivilOS creates KnowledgeRecords.
    """

    knowledge_id: UUID
    investigation_id: UUID
    source_hypothesis_id: UUID
    validation_id: UUID
    memory_admission_id: UUID
    knowledge_type: KnowledgeType
    title: str
    content: str
    status: KnowledgeStatus
    version: int
    evidence_ids: tuple[UUID, ...]
    created_at: datetime
    updated_at: datetime
    deprecated_at: datetime | None = None
    merged_into_id: UUID | None = None

    @classmethod
    def admit(
        cls,
        *,
        investigation_id: UUID,
        source_hypothesis_id: UUID,
        validation_id: UUID,
        memory_admission_id: UUID,
        knowledge_type: KnowledgeType,
        title: str,
        content: str,
        evidence_ids: tuple[UUID, ...],
    ) -> KnowledgeRecord:
        """
        Create the first admitted version of validated knowledge.

        This method does not perform validation itself.
        It requires references proving that validation and
        Memory Admission already occurred.
        """

        normalized_title = title.strip()
        normalized_content = content.strip()
        unique_evidence_ids = tuple(dict.fromkeys(evidence_ids))

        if not normalized_title:
            raise ValueError("Knowledge title cannot be empty.")

        if not normalized_content:
            raise ValueError("Knowledge content cannot be empty.")

        if not unique_evidence_ids:
            raise ValueError(
                "A KnowledgeRecord requires at least one evidence reference."
            )

        now = datetime.now(timezone.utc)

        return cls(
            knowledge_id=uuid4(),
            investigation_id=investigation_id,
            source_hypothesis_id=source_hypothesis_id,
            validation_id=validation_id,
            memory_admission_id=memory_admission_id,
            knowledge_type=knowledge_type,
            title=normalized_title,
            content=normalized_content,
            status=KnowledgeStatus.ACTIVE,
            version=1,
            evidence_ids=unique_evidence_ids,
            created_at=now,
            updated_at=now,
        )

    def challenge(self) -> KnowledgeRecord:
        """
        Mark active or updated knowledge as challenged.

        A challenge does not erase knowledge and does not
        automatically prove that the knowledge is false.
        """

        if self.status not in {
            KnowledgeStatus.ACTIVE,
            KnowledgeStatus.UPDATED,
        }:
            raise ValueError(
                f"Knowledge in status '{self.status.value}' "
                "cannot be challenged."
            )

        return self._copy_with(
            status=KnowledgeStatus.CHALLENGED,
        )

    def require_revalidation(self) -> KnowledgeRecord:
        """
        Require a new validation process before the knowledge
        can return to active use.
        """

        if self.status not in {
            KnowledgeStatus.ACTIVE,
            KnowledgeStatus.CHALLENGED,
            KnowledgeStatus.UPDATED,
        }:
            raise ValueError(
                f"Knowledge in status '{self.status.value}' "
                "cannot require revalidation."
            )

        return self._copy_with(
            status=KnowledgeStatus.REVALIDATION_REQUIRED,
        )

    def revise(
        self,
        *,
        validation_id: UUID,
        memory_admission_id: UUID,
        title: str,
        content: str,
        evidence_ids: tuple[UUID, ...],
    ) -> KnowledgeRecord:
        """
        Create the next version after successful revalidation
        and Memory Admission.

        Persistence must store the previous version before
        saving this returned version.
        """

        if self.status not in {
            KnowledgeStatus.CHALLENGED,
            KnowledgeStatus.REVALIDATION_REQUIRED,
        }:
            raise ValueError(
                "Knowledge must be challenged or require revalidation "
                "before a new version can be created."
            )

        normalized_title = title.strip()
        normalized_content = content.strip()
        unique_evidence_ids = tuple(dict.fromkeys(evidence_ids))

        if not normalized_title:
            raise ValueError("Revised knowledge title cannot be empty.")

        if not normalized_content:
            raise ValueError("Revised knowledge content cannot be empty.")

        if not unique_evidence_ids:
            raise ValueError(
                "Revised knowledge requires at least one evidence reference."
            )

        return self._copy_with(
            validation_id=validation_id,
            memory_admission_id=memory_admission_id,
            title=normalized_title,
            content=normalized_content,
            status=KnowledgeStatus.UPDATED,
            version=self.version + 1,
            evidence_ids=unique_evidence_ids,
            deprecated_at=None,
            merged_into_id=None,
        )

    def activate(self) -> KnowledgeRecord:
        """
        Mark successfully revised knowledge as active.
        """

        if self.status != KnowledgeStatus.UPDATED:
            raise ValueError(
                "Only updated knowledge can return to active status."
            )

        return self._copy_with(
            status=KnowledgeStatus.ACTIVE,
        )

    def deprecate(self) -> KnowledgeRecord:
        """
        Deprecate knowledge without deleting its history.
        """

        if self.status in {
            KnowledgeStatus.DEPRECATED,
            KnowledgeStatus.MERGED,
        }:
            raise ValueError(
                f"Knowledge is already '{self.status.value}'."
            )

        now = datetime.now(timezone.utc)

        return self._copy_with(
            status=KnowledgeStatus.DEPRECATED,
            deprecated_at=now,
        )

    def merge_into(
        self,
        canonical_knowledge_id: UUID,
    ) -> KnowledgeRecord:
        """
        Merge this record into a canonical KnowledgeRecord
        while preserving this record's identity and history.
        """

        if canonical_knowledge_id == self.knowledge_id:
            raise ValueError(
                "Knowledge cannot be merged into itself."
            )

        if self.status in {
            KnowledgeStatus.DEPRECATED,
            KnowledgeStatus.MERGED,
        }:
            raise ValueError(
                f"Knowledge in status '{self.status.value}' "
                "cannot be merged."
            )

        return self._copy_with(
            status=KnowledgeStatus.MERGED,
            merged_into_id=canonical_knowledge_id,
        )

    def _copy_with(
        self,
        *,
        validation_id: UUID | None = None,
        memory_admission_id: UUID | None = None,
        title: str | None = None,
        content: str | None = None,
        status: KnowledgeStatus | None = None,
        version: int | None = None,
        evidence_ids: tuple[UUID, ...] | None = None,
        deprecated_at: datetime | None = None,
        merged_into_id: UUID | None = None,
    ) -> KnowledgeRecord:
        """
        Return a new immutable KnowledgeRecord state.

        Existing records are never modified silently.
        """

        return KnowledgeRecord(
            knowledge_id=self.knowledge_id,
            investigation_id=self.investigation_id,
            source_hypothesis_id=self.source_hypothesis_id,
            validation_id=validation_id or self.validation_id,
            memory_admission_id=(
                memory_admission_id or self.memory_admission_id
            ),
            knowledge_type=self.knowledge_type,
            title=title if title is not None else self.title,
            content=content if content is not None else self.content,
            status=status or self.status,
            version=version if version is not None else self.version,
            evidence_ids=(
                evidence_ids
                if evidence_ids is not None
                else self.evidence_ids
            ),
            created_at=self.created_at,
            updated_at=datetime.now(timezone.utc),
            deprecated_at=deprecated_at,
            merged_into_id=merged_into_id,
        )
