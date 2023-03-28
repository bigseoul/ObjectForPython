from regular_phone_ import RegularPhone
from money_ import Money
from datetime import time


class TaxableRegularPhone(RegularPhone):
    def __init__(self, amount: Money, seconds: time, tax_rate: float) -> None:
        super().__init__(amount, seconds)
        self.__tax_rate = tax_rate

    #Override
    def calculate_fee(self) -> Money:
        fee: Money = super().calculate_fee()
        return fee.plus(fee.times(self.__tax_rate))
