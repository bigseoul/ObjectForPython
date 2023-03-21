from discount_condition_ import AbsDiscountCondition
from discount_policy_ import DiscountPolicy
from money_ import Money


class AmountDiscountPolicy(DiscountPolicy):
    def __init__(
        self, discount_amount, *discount_conditions: AbsDiscountCondition
    ) -> None:
        super().__init__(*discount_conditions)
        self.__discount_amount = discount_amount

    # override
    def _get_discount_amount(self, screening) -> Money:
        return self.__discount_amount

    def __str__(self) -> str:
        discount_conditions_str = ", ".join(map(str, self._discount_condtions))
        return f"AmountDiscountPolicy(discount_amount={self.__discount_amount}, discount_conditions=[{discount_conditions_str}])"
