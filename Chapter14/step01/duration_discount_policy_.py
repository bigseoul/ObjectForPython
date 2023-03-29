from basic_rate_policy_ import BasicRatePolicy
from duration_discount_rule_ import DurationDiscountRule
from money_ import Money
from call_ import Call


class DurationDiscountPolicy(BasicRatePolicy):
    def __init__(self, rules: list[DurationDiscountRule]) -> None:
        self.__rules = rules

    # override
    def _calculate_call_fee(self, call: Call) -> Money:
        result = Money.wons(0)
        for rule in self.__rules:
            result = result.plus(rule.calculate(call))

        return result
