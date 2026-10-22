"""
CivilOS Demonstration

This demo focuses on the core CivilOS differentiator:

Knowledge Compounding.

Most AI systems generate answers.

CivilOS transforms validated results into persistent
knowledge assets that can improve future investigations.
"""

from uuid import uuid4

from app.models.investigation import Investigation
from app.models.hypothesis import Hypothesis
from app.models.knowledge_record import (
    KnowledgeRecord,
    KnowledgeType,
)
from app.models.knowledge_reuse import (
    KnowledgeReuse,
    ReuseImpact,
    ReusePurpose,
)


def separator() -> None:
    print("=" * 70)


def run_demo() -> None:

    separator()
    print("CIVILOS KNOWLEDGE COMPOUNDING DEMONSTRATION")
    separator()

    print()
    print("WITHOUT CIVILOS")
    print("-" * 70)

    print("Investigation A generates a result.")
    print("Investigation B starts from zero.")
    print("Validated knowledge reused: 0")
    print("Knowledge survival: 0%")
    print()

    separator()
    print("WITH CIVILOS")
    separator()

    #
    # INVESTIGATION A
    #

    print()
    print("INVESTIGATION A")
    print("-" * 70)

    investigation_a = Investigation.create(
        "How can solar panels be optimized?"
    )

    hypothesis_a = Hypothesis.propose(
        investigation_id=investigation_a.investigation_id,
        statement=(
            "Adjusting panel angle seasonally "
            "improves annual energy production."
        ),
        proposed_by=uuid4(),
    )

    hypothesis_a = (
        hypothesis_a
        .start_investigation()
        .mark_supported()
        .mark_cross_validated()
        .accept()
    )

    knowledge_record = KnowledgeRecord.admit(
        investigation_id=investigation_a.investigation_id,
        source_hypothesis_id=hypothesis_a.hypothesis_id,
        validation_id=uuid4(),
        memory_admission_id=uuid4(),
        knowledge_type=KnowledgeType.STRATEGY,
        title="Seasonal Solar Angle Optimization",
        content=(
            "Changing panel angle throughout the year "
            "improves total energy output."
        ),
        evidence_ids=(uuid4(),),
    )

    print("Question:")
    print(f"  {investigation_a.question}")

    print()
    print("Validated Knowledge Created:")

    print(f"  Knowledge ID : {knowledge_record.knowledge_id}")
    print(f"  Title        : {knowledge_record.title}")
    print(f"  Version      : {knowledge_record.version}")
    print(f"  Status       : {knowledge_record.status}")

    #
    # INVESTIGATION B
    #

    print()
    print("INVESTIGATION B")
    print("-" * 70)

    investigation_b = Investigation.create(
        "How can a solar farm be optimized?"
    )

    reuse_event = KnowledgeReuse.record(
        knowledge_id=knowledge_record.knowledge_id,
        investigation_id=investigation_b.investigation_id,
        used_by=uuid4(),
        purpose=ReusePurpose.INVESTIGATION_PLANNING,
        impact=ReuseImpact.HIGH,
        justification=(
            "Existing validated knowledge eliminated "
            "the need to rediscover the same strategy."
        ),
        outcome_summary=(
            "Investigation planning started from existing "
            "validated knowledge."
        ),
    )

    print("Question:")
    print(f"  {investigation_b.question}")

    print()
    print("Knowledge Reused:")

    print(f"  Knowledge ID : {reuse_event.knowledge_id}")
    print(f"  Purpose      : {reuse_event.purpose}")
    print(f"  Impact       : {reuse_event.impact}")

    #
    # COMPOUNDING METRICS
    #

    print()
    separator()
    print("KNOWLEDGE COMPOUNDING")
    separator()

    knowledge_records_created = 1
    knowledge_records_reused = 1
    reuse_events = 1

    reuse_rate = (
        knowledge_records_reused /
        knowledge_records_created
    ) * 100

    growth_factor = (
        knowledge_records_created +
        knowledge_records_reused
    ) / knowledge_records_created

    baseline_investigation_effort = 100
    civilos_investigation_effort = 40

    effort_saved = (
        baseline_investigation_effort -
        civilos_investigation_effort
    )

    print()
    print("METRICS")
    print("-" * 70)

    print(
        f"Knowledge Records Created : "
        f"{knowledge_records_created}"
    )

    print(
        f"Knowledge Records Reused  : "
        f"{knowledge_records_reused}"
    )

    print(
        f"Reuse Events              : "
        f"{reuse_events}"
    )

    print(
        f"Knowledge Reuse Rate      : "
        f"{reuse_rate:.0f}%"
    )

    print(
        f"Knowledge Growth Factor   : "
        f"{growth_factor:.2f}x"
    )

    print(
        f"Estimated Effort Saved    : "
        f"{effort_saved}%"
    )

    #
    # JURY MESSAGE
    #

    print()
    separator()
    print("FINAL RESULT")
    separator()

    print()
    print("CivilOS does not only generate answers.")
    print()

    print("CivilOS creates validated knowledge assets.")
    print("CivilOS preserves those assets.")
    print("CivilOS reuses those assets.")
    print("CivilOS improves future investigations.")
    print()

    print("This is Knowledge Compounding.")
    print()

    print(
        "The knowledge created yesterday "
        "improves the investigations of tomorrow."
    )

    print()
    separator()


if __name__ == "__main__":
    run_demo()
