from nightly_discount_phone_ import NightlyDiscountPhone
from money_ import Money
from datetime import time


class TaxableNightlyDiscountPhone(NightlyDiscountPhone):
    def __init__(
        self,
        nightly_amount: Money,
        regular_amount: Money,
        seconds: time,
        tax_rate: float,
    ) -> None:
        super().__init__(nightly_amount, regular_amount, seconds)
        self.__tax_rate = tax_rate

    # Override
    def after_calculated(self, fee: Money) -> Money:
        return fee.plus(fee.times(self.__tax_rate))
