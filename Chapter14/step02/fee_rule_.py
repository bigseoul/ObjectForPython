from fee_condition_ import FeeCondition
from fee_per_duration_ import FeePerDuration
from money_ import Money
from call_ import Call


class FeeRule:
    """FeeCondition은 요금조건, FeePerDuration은 단위시간"""

    def __init__(
        self, fee_conditon: FeeCondition, fee_per_duration: FeePerDuration
    ) -> None:
        self.__fee_conditon = fee_conditon
        self.__fee_per_duration = fee_per_duration

    def calculate_fee(self, call: Call) -> Money:
        intervals = self.__fee_conditon.find_time_interval(call)

        # list comprehension
        # expression(x) for x in x_list 일때, for x in x_list부터 작성
        # https://shoark7.github.io/programming/python/about-list-comprehension-python
        fees = [self.__fee_per_duration.calculate(interval) for interval in intervals]
        result = Money.wons(0)
        for fee in fees:
            result = result.plus(fee)
        return result
