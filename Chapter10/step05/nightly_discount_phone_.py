from datetime import time
from typing import TYPE_CHECKING, List
from money_zero import MoneyZero
from phone_ import Phone
from call_ import Call
from money_ import Money


class NightlyDiscountPhone(Phone):

    LATE_NIGHT_HOUR = 22

    def __init__(
        self,
        nightly_amount: Money,
        regular_amount: Money,
        seconds: time,
        tax_rate: float,
    ) -> None:
        super().__init__(regular_amount, seconds, tax_rate)
        self.__nightly_amount = nightly_amount

    """
    상속을 이용해 코드를 재사용하기 위해서는 
    부모 클래스의 개발자가 세웠던 가정이나 추론을 정확히 알고 있어야 한다.
    코드가 복잡하거나 직관적이지 않으면 수정하기 어렵다.
    """

    def calculate_fee(self) -> Money:
        # 부모 클래스의 calculate_fee 호출, 22시 이전의 통화요금
        result = super().calculate_fee()
        nightly_fee = MoneyZero.ZERO
        call: Call = None  # type: ignore

        for call in self.get_calls():

            if call.start_time.hour >= NightlyDiscountPhone.LATE_NIGHT_HOUR:
                nightly_fee = nightly_fee.plus(
                    self.get_amount()
                    .minus(self.__nightly_amount)
                    .times(call.get_duration() / self.get_seconds())
                )
        return result.minus(nightly_fee.plus(nightly_fee.times(self.get_tax_rate())))
