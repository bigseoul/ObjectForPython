from money_ import Money
from datetime import time
from regular_phone_ import RegularPhone


class TaxableRegularPhone(RegularPhone):
    def __init__(self, amount: Money, seconds: time, tax_rate: float) -> None:
        super().__init__(amount, seconds)
        self.__tax_rate = tax_rate

    # Override
    def after_calculated(self, fee: Money) -> Money:
        return fee.plus(fee.times(self.__tax_rate))

    # #Override
    # def calculate_fee(self) -> Money:
    #     fee: Money = super().calculate_fee()
    #     return fee.plus(fee.times(self.__tax_rate))/
