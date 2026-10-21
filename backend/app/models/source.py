from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID, uuid4


class SourceType(StrEnum):
    RESEARCH_PAPER = "research_paper"
    DATASET = "dataset"
    GOVERNMENT_RECORD = "government_record"
    OFFICIAL_DOCUMENT = "official_document"
    ARTICLE = "article"
    BOOK = "book"
    WEBSITE = "website"
    TOOL_RESULT = "tool_result"
    OBSERVATION = "observation"
    INTERNAL_KNOWLEDGE = "internal_knowledge"


class SourceStatus(StrEnum):
    REGISTERED = "registered"
    AVAILABLE = "available"
    UNDER_REVIEW = "under_review"
    VERIFIED = "verified"
    CHALLENGED = "challenged"
    UNAVAILABLE = "unavailable"
    INVALIDATED = "invalidated"
    SUPERSEDED = "superseded"


@dataclass(frozen=True, slots=True)
class Source:
    """
    Origin record for information used inside CivilOS.

    A Source identifies where information came from.

    A Source is not Evidence.

    Evidence represents the specific source material used to support,
    contradict or contextualise a Hypothesis.

    Registration does not establish reliability.

    Meta AI may discover or recommend a candidate Source, but a model
    output cannot certify its own origin, availability or reliability.
    """

    source_id: UUID
    source_type: SourceType
    title: str
    locator: str
    status: SourceStatus
    created_at: datetime
    updated_at: datetime
    publisher: str | None = None
    canonical_identifier: str | None = None
    published_at: datetime | None = None
    retrieved_at: datetime | None = None
    content_fingerprint: str | None = None
    original_source_id: UUID | None = None
    parent_source_id: UUID | None = None
    tool_receipt_id: UUID | None = None
    reviewed_by: UUID | None = None
    review_reason: str | None = None
    superseded_by_id: UUID | None = None

    @classmethod
    def register(
        cls,
        *,
        source_type: SourceType,
        title: str,
        locator: str,
        publisher: str | None = None,
        canonical_identifier: str | None = None,
        published_at: datetime | None = None,
        retrieved_at: datetime | None = None,
        content_fingerprint: str | None = None,
        original_source_id: UUID | None = None,
        parent_source_id: UUID | None = None,
        tool_receipt_id: UUID | None = None,
    ) -> Source:
        """
        Register a candidate information source.

        Registration does not verify the Source and does not create
        Evidence or validated knowledge.
        """

        normalized_title = title.strip()
        normalized_locator = locator.strip()
        normalized_publisher = cls._normalize_optional_text(publisher)
        normalized_identifier = cls._normalize_optional_text(
            canonical_identifier
        )
        normalized_fingerprint = cls._normalize_optional_text(
            content_fingerprint
        )

        if not normalized_title:
            raise ValueError("Source title cannot be empty.")

        if not normalized_locator:
            raise ValueError("Source locator cannot be empty.")

        if original_source_id is not None and (
            original_source_id == parent_source_id
        ):
            raise ValueError(
                "Original source and parent source must represent "
                "distinct relationships when both are provided."
            )

        if (
            source_type == SourceType.TOOL_RESULT
            and tool_receipt_id is None
        ):
            raise ValueError(
                "A tool-result Source requires a Tool Receipt."
            )

        if (
            source_type != SourceType.TOOL_RESULT
            and tool_receipt_id is not None
        ):
            raise ValueError(
                "Only a tool-result Source may reference a Tool Receipt."
            )

        now = datetime.now(timezone.utc)

        return cls(
            source_id=uuid4(),
            source_type=source_type,
            title=normalized_title,
            locator=normalized_locator,
            status=SourceStatus.REGISTERED,
            created_at=now,
            updated_at=now,
            publisher=normalized_publisher,
            canonical_identifier=normalized_identifier,
            published_at=published_at,
            retrieved_at=retrieved_at,
            content_fingerprint=normalized_fingerprint,
            original_source_id=original_source_id,
            parent_source_id=parent_source_id,
            tool_receipt_id=tool_receipt_id,
        )

    def mark_available(
        self,
        *,
        retrieved_at: datetime,
        content_fingerprint: str,
    ) -> Source:
        """
        Record successful retrieval and content integrity information.

        Availability does not establish reliability.
        """

        if self.status not in {
            SourceStatus.REGISTERED,
            SourceStatus.UNAVAILABLE,
        }:
            raise ValueError(
                f"Source in status '{self.status.value}' "
                "cannot be marked available."
            )

        normalized_fingerprint = content_fingerprint.strip()

        if not normalized_fingerprint:
            raise ValueError(
                "Available Source requires a content fingerprint."
            )

        return self._copy_with(
            status=SourceStatus.AVAILABLE,
            retrieved_at=retrieved_at,
            content_fingerprint=normalized_fingerprint,
            reviewed_by=None,
            review_reason=None,
        )

    def start_review(
        self,
        *,
        reviewer_id: UUID,
    ) -> Source:
        """
        Begin an independent review of source identity and provenance.
        """

        if self.status not in {
            SourceStatus.REGISTERED,
            SourceStatus.AVAILABLE,
            SourceStatus.CHALLENGED,
        }:
            raise ValueError(
                f"Source in status '{self.status.value}' "
                "cannot enter review."
            )

        return self._copy_with(
            status=SourceStatus.UNDER_REVIEW,
            reviewed_by=reviewer_id,
            review_reason=None,
        )

    def verify(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Source:
        """
        Verify source identity, provenance and availability.

        Verification does not prove that every claim in the Source
        is correct and does not validate a Hypothesis.
        """

        if self.status != SourceStatus.UNDER_REVIEW:
            raise ValueError(
                "Source must be under review before verification."
            )

        normalized_reason = self._normalize_required_reason(reason)

        return self._copy_with(
            status=SourceStatus.VERIFIED,
            reviewed_by=reviewer_id,
            review_reason=normalized_reason,
        )

    def challenge(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Source:
        """
        Record a material concern about source identity, provenance,
        availability or integrity.
        """

        if self.status in {
            SourceStatus.INVALIDATED,
            SourceStatus.SUPERSEDED,
        }:
            raise ValueError(
                f"Source in status '{self.status.value}' "
                "cannot be challenged."
            )

        normalized_reason = self._normalize_required_reason(reason)

        return self._copy_with(
            status=SourceStatus.CHALLENGED,
            reviewed_by=reviewer_id,
            review_reason=normalized_reason,
        )

    def mark_unavailable(
        self,
        *,
        reason: str,
    ) -> Source:
        """
        Record that the Source cannot currently be retrieved.

        Unavailability does not silently delete previously retrieved
        material or its historical provenance.
        """

        if self.status in {
            SourceStatus.INVALIDATED,
            SourceStatus.SUPERSEDED,
        }:
            raise ValueError(
                f"Source in status '{self.status.value}' "
                "cannot be marked unavailable."
            )

        normalized_reason = self._normalize_required_reason(reason)

        return self._copy_with(
            status=SourceStatus.UNAVAILABLE,
            review_reason=normalized_reason,
        )

    def invalidate(
        self,
        *,
        reviewer_id: UUID,
        reason: str,
    ) -> Source:
        """
        Invalidate a Source after documented review.

        Dependent Evidence and Knowledge must be located and reviewed
        by their responsible CivilOS components.
        """

        if self.status == SourceStatus.SUPERSEDED:
            raise ValueError(
                "A superseded Source cannot be invalidated."
            )

        if self.status == SourceStatus.INVALIDATED:
            raise ValueError(
                "Source is already invalidated."
            )

        normalized_reason = self._normalize_required_reason(reason)

        return self._copy_with(
            status=SourceStatus.INVALIDATED,
            reviewed_by=reviewer_id,
            review_reason=normalized_reason,
        )

    def supersede(
        self,
        *,
        replacement_source_id: UUID,
        reason: str,
    ) -> Source:
        """
        Replace this Source with a newer or canonical Source while
        preserving this Source and its history.
        """

        if replacement_source_id == self.source_id:
            raise ValueError(
                "Source cannot supersede itself."
            )

        if self.status == SourceStatus.SUPERSEDED:
            raise ValueError(
                "Source is already superseded."
            )

        normalized_reason = self._normalize_required_reason(reason)

        return self._copy_with(
            status=SourceStatus.SUPERSEDED,
            review_reason=normalized_reason,
            superseded_by_id=replacement_source_id,
        )

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None

    @staticmethod
    def _normalize_required_reason(
        reason: str,
    ) -> str:
        normalized_reason = reason.strip()

        if not normalized_reason:
            raise ValueError(
                "Source review reason cannot be empty."
            )

        return normalized_reason

    def _copy_with(
        self,
        *,
        status: SourceStatus | None = None,
        retrieved_at: datetime | None = None,
        content_fingerprint: str | None = None,
        reviewed_by: UUID | None = None,
        review_reason: str | None = None,
        superseded_by_id: UUID | None = None,
    ) -> Source:
        """
        Return a new immutable Source state.

        Persistence must create Domain Events and Audit Records for
        material transitions.
        """

        return Source(
            source_id=self.source_id,
            source_type=self.source_type,
            title=self.title,
            locator=self.locator,
            status=status or self.status,
            created_at=self.created_at,
            updated_at=datetime.now(timezone.utc),
            publisher=self.publisher,
            canonical_identifier=self.canonical_identifier,
            published_at=self.published_at,
            retrieved_at=(
                retrieved_at
                if retrieved_at is not None
                else self.retrieved_at
            ),
            content_fingerprint=(
                content_fingerprint
                if content_fingerprint is not None
                else self.content_fingerprint
            ),
            original_source_id=self.original_source_id,
            parent_source_id=self.parent_source_id,
            tool_receipt_id=self.tool_receipt_id,
            reviewed_by=reviewed_by,
            review_reason=review_reason,
            superseded_by_id=superseded_by_id,
        )
