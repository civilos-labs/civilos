from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CompoundingMetrics:
    """
    Measures whether CivilOS is creating cumulative
    knowledge instead of isolated information.

    CivilOS does not optimise answer generation.

    CivilOS optimises knowledge survival,
    knowledge reuse and knowledge compounding.
    """

    knowledge_records_created: int
    knowledge_records_reused: int
    investigations_influenced: int
    duplicate_work_avoided: int

    @property
    def reuse_rate(self) -> float:
        if self.knowledge_records_created == 0:
            return 0.0

        return (
            self.knowledge_records_reused
            / self.knowledge_records_created
        ) * 100

    @property
    def compounding_factor(self) -> float:
        if self.knowledge_records_created == 0:
            return 0.0

        return (
            self.knowledge_records_created
            + self.knowledge_records_reused
        ) / self.knowledge_records_created

    @property
    def influence_factor(self) -> float:
        if self.knowledge_records_created == 0:
            return 0.0

        return (
            self.investigations_influenced
            / self.knowledge_records_created
        )


class KnowledgeCompoundingEngine:
    """
    Core CivilOS differentiator.

    Most systems measure generation.

    CivilOS measures whether validated knowledge
    improves future investigations.

    Knowledge Compounding exists only when
    knowledge demonstrably influences future work.
    """

    @staticmethod
    def calculate(
        *,
        knowledge_records_created: int,
        knowledge_records_reused: int,
        investigations_influenced: int,
        duplicate_work_avoided: int,
    ) -> CompoundingMetrics:

        return CompoundingMetrics(
            knowledge_records_created=
            knowledge_records_created,

            knowledge_records_reused=
            knowledge_records_reused,

            investigations_influenced=
            investigations_influenced,

            duplicate_work_avoided=
            duplicate_work_avoided,
        )
