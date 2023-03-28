from basic_rate_policy_ import BasicRatePolicy
from day_of_week_discount_rule_ import DayOfWeekDiscountRule
from money_ import Money
from call_ import Call


class DayOfWeekDiscountPolicy(BasicRatePolicy):
    """요일별 할인을 하는 전문가"""

    def __init__(self, rules: list[DayOfWeekDiscountRule]) -> None:
        self.__rules = rules

    # override
    def _calculate_call_fee(self, call: Call) -> Money:
        result = Money.wons(0)
        for interval in call.get_interval().split_by_day():
            for rule in self.__rules:
                result = result.plus(rule.calculate(interval))

        return result
