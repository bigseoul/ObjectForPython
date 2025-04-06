from regular_phone_ import RegularPhone
from money_ import Money
from datetime import time


class RateDiscountableRegularPhone(RegularPhone):
    def __init__(self, amount: Money, seconds: time, discount_amount: Money) -> None:
        super().__init__(amount, seconds)
        self.__discount_amount = discount_amount

    def after_calculated(self, fee: Money) -> Money:
        return fee.minus(self.__discount_amount)
    
    