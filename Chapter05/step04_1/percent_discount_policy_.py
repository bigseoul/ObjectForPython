from typing import TYPE_CHECKING

from discount_condition_ import AbsDiscountCondition
from discount_policy_ import DiscountPolicy
from money_ import Money

if TYPE_CHECKING:
    from screening_ import Screening


class PercentDiscountPolicy(DiscountPolicy):
    def __init__(
        self, discount_rate: float, *discount_conditions: AbsDiscountCondition
    ) -> None:
        super().__init__(*discount_conditions)
        self.__discount_rate = discount_rate

    # override
    def _get_discount_amount(self, screening: "Screening") -> Money:
        return screening.get_movie_fee() * self.__discount_rate

    def __str__(self) -> str:
        discount_conditions_str = ", ".join(map(str, self._discount_condtions))
        return f"PercentDiscountPolicy(discount_ratet={self.__discount_rate}, discount_conditions=[{discount_conditions_str}])"
