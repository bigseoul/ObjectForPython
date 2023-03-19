from typing import TYPE_CHECKING

from discount_condition_ import AbsDiscountCondition

if TYPE_CHECKING:
    from screening_ import Screening


class SequenceCondition(AbsDiscountCondition):
    def __init__(self, sequence: int) -> None:
        self._sequence = sequence

    def is_satisfied_by(self, screening: "Screening") -> bool:
        return self._sequence == screening.get_sequence()
