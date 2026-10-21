from app.models.investigation import (
    Investigation,
    InvestigationStatus,
)
from app.models.hypothesis import Hypothesis


class InvestigationWorkflow:
    """
    First executable CivilOS workflow.

    This workflow coordinates Investigation and
    Hypothesis lifecycles without replacing
    domain model rules.

    Domain models remain the source of truth.

    The workflow exists to make the lifecycle
    explicit and auditable.
    """

    @staticmethod
    def plan(
        investigation: Investigation,
    ) -> Investigation:
        return investigation.change_status(
            InvestigationStatus.PLANNED
        )

    @staticmethod
    def start(
        investigation: Investigation,
        hypothesis: Hypothesis,
    ) -> tuple[Investigation, Hypothesis]:
        return (
            investigation.change_status(
                InvestigationStatus.INVESTIGATING
            ),
            hypothesis.start_investigation(),
        )

    @staticmethod
    def submit_for_review(
        investigation: Investigation,
    ) -> Investigation:
        return investigation.change_status(
            InvestigationStatus.UNDER_REVIEW
        )

    @staticmethod
    def request_validation(
        investigation: Investigation,
    ) -> Investigation:
        return investigation.change_status(
            InvestigationStatus.AWAITING_VALIDATION
        )

    @staticmethod
    def complete(
        investigation: Investigation,
    ) -> Investigation:
        return investigation.change_status(
            InvestigationStatus.COMPLETED
        )

    @staticmethod
    def insufficient_evidence(
        investigation: Investigation,
    ) -> Investigation:
        return investigation.change_status(
            InvestigationStatus.INSUFFICIENT_EVIDENCE
        )

    @staticmethod
    def require_revalidation(
        investigation: Investigation,
    ) -> Investigation:
        return investigation.change_status(
            InvestigationStatus.REVALIDATION_REQUIRED
        )
