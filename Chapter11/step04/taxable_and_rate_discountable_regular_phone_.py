from call_ import Call
from datetime import datetime, time
from money_ import Money

from taxable_regular_phone_ import TaxableRegularPhone


class TaxableAndRateDiscountableRegularPhone(TaxableRegularPhone):
    def __init__(
        self, amount: Money, seconds: time, tax_rate: float, discount_amount: Money
    ) -> None:
        super().__init__(amount, seconds, tax_rate)
        self.__discount_amount = discount_amount

    def after_calculated(self, fee: Money) -> Money:
        return super().after_calculated(fee)
