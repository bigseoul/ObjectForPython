from money_ import Money
from additional_rate_policy_ import AdditionalRatePolicy, RatePolicy


class RateDiscountablePolicy(AdditionalRatePolicy):
    def __init__(self, discount_amount, following: RatePolicy) -> None:
        super().__init__(following)
        self.__discount_amount = discount_amount

    def _after_calculated(self, fee: Money) -> Money:
        return fee.minus(self.__discount_amount)
