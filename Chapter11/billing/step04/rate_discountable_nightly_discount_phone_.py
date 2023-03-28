from money_ import Money
from datetime import time
from nightly_discount_phone_ import NightlyDiscountPhone


class RateDiscountableNightlyDiscountPhone(NightlyDiscountPhone):
    def __init__(
        self,
        nightly_amount: Money,
        regular_amount: Money,
        seconds: time,
        discount_amount: Money,
    ) -> None:
        super().__init__(nightly_amount, regular_amount, seconds)
        self.__discount_amount = discount_amount

    def after_calculated(self, fee: Money) -> Money:
        return fee.minus(self.__discount_amount)
