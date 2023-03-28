from datetime import time

from money_ import Money
from regular_phone_ import RegularPhone


class TaxableRegularPhone(RegularPhone):
    def __init__(self, amount: Money, seconds: time, tax_rate: float) -> None:
        super().__init__(amount, seconds)
        self.__tax_rate = tax_rate

    # Override
    def calculate_fee(self) -> Money:
        fee: Money = super().calculate_fee()  # 슈퍼호출로 결합도 증가
        return fee.plus(fee.times(self.__tax_rate))
