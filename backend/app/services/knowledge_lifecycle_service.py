from uuid import UUID

from app.models.investigation import Investigation
from app.models.hypothesis import Hypothesis
from app.models.knowledge_record import KnowledgeRecord
from app.models.knowledge_reuse import KnowledgeReuse


class KnowledgeLifecycleService:
    """
    CivilOS lifecycle orchestration service.

    This service does not fabricate evidence,
    validation decisions, memory admission decisions
    or knowledge records.

    Every stage must provide real validated inputs.

    If it is not real, it is not shown.
    """

    @staticmethod
    def start_investigation(
        question: str,
    ) -> Investigation:
        """
        Create a new Investigation.
        """

        return Investigation.create(
            question=question
        )

    @staticmethod
    def propose_hypothesis(
        *,
        investigation_id: UUID,
        statement: str,
        proposed_by: UUID,
    ) -> Hypothesis:
        """
        Register a new Hypothesis.

        A Hypothesis is not knowledge.
        """

        return Hypothesis.propose(
            investigation_id=investigation_id,
            statement=statement,
            proposed_by=proposed_by,
        )

    @staticmethod
    def admit_knowledge(
        knowledge_record: KnowledgeRecord,
    ) -> KnowledgeRecord:
        """
        Accept an already created KnowledgeRecord.

        This method exists only to make the lifecycle
        explicit and auditable.

        Creation of the KnowledgeRecord must already
        have passed:

        Evidence
        Challenge
        Validation
        Memory Admission
        """

        return knowledge_record

    @staticmethod
    def register_reuse(
        knowledge_reuse: KnowledgeReuse,
    ) -> KnowledgeReuse:
        """
        Register an existing KnowledgeReuse event.

        Reuse must already be independently created
        and documented.

        Reading knowledge is not reuse.
        """

        return knowledge_reuse

    @staticmethod
    def explain_lifecycle() -> tuple[str, ...]:
        """
        Human-readable representation of the
        CivilOS lifecycle.
        """

        return (
            "Investigation",
            "Hypothesis",
            "Source",
            "Evidence",
            "Challenge",
            "Validation",
            "Memory Admission",
            "Knowledge Record",
            "Knowledge Reuse",
            "Knowledge Compounding",
        )
