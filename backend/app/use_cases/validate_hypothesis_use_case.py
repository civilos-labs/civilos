from app.models.validation import ValidationDecision


class ValidateHypothesisUseCase:
    """
    Register a completed Validation Decision.

    This use case does not perform validation.

    This use case does not create Evidence.

    This use case does not create Knowledge Records.

    This use case does not admit knowledge.

    Validation rules, reviewers and outcomes
    must already exist before this use case
    is executed.
    """

    @staticmethod
    def execute(
        decision: ValidationDecision,
    ) -> ValidationDecision:
        return decision
