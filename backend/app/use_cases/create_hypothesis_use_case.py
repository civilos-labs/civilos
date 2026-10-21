from uuid import UUID

from app.models.hypothesis import Hypothesis


class CreateHypothesisUseCase:
    """
    Create a new Hypothesis inside an existing
    Investigation.

    This use case does not validate hypotheses.

    This use case does not admit knowledge.

    This use case does not create Knowledge Records.

    It only creates a valid Hypothesis that can
    later enter the CivilOS validation process.
    """

    @staticmethod
    def execute(
        *,
        investigation_id: UUID,
        statement: str,
        proposed_by: UUID,
    ) -> Hypothesis:
        return Hypothesis.propose(
            investigation_id=investigation_id,
            statement=statement,
            proposed_by=proposed_by,
        )
