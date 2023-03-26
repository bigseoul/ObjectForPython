from datetime import time
from typing import TYPE_CHECKING, List
from money_zero import MoneyZero
from phone_type_ import PhoneType
from call_ import Call
from money_ import Money


class Phone:
    """
    1. 파이썬은 생성자 오버로드 없음.
    2. 클래스메서드 데코레이터 방식으로 오버로드함.
    3. PhoneType으로 나뉘어짐.
    """

    LATE_NIGHT_HOUR: int = 22

    def __init__(
        self,
        phone_type: PhoneType,
        amount: Money = None,  # type: ignore
        nightly_amount: Money = None,  # type: ignore
        regular_amount: Money = None,  # type: ignore
        seconds: time = None,  # type: ignore
        # tax_rate: "float" = 0.0,
    ) -> None:
        self.__phone_type = phone_type
        self.__amount = amount
        self.__nightly_amount = nightly_amount
        self.__regular_amount = regular_amount
        self.__seconds = seconds
        # self.__tax_rate = tax_rate
        self.__calls = []

    @classmethod
    def from_phone_for_regular(cls, cls_amount: Money, cls_seconds: time):
        return cls(phone_type=PhoneType.REGULAR, amount=cls_amount, seconds=cls_seconds)

    @classmethod
    def from_phone_for_nightly(
        cls,
        cls_nightly_amount: Money,
        cls_regular_amount: Money,
        cls_seconds: time,
    ):
        return cls(
            phone_type=PhoneType.NIGHTLY,
            nightly_amount=cls_nightly_amount,
            regular_amount=cls_regular_amount,
            seconds=cls_seconds,
        )

    def call(self, call: Call) -> None:
        self.__calls.append(call)

    def get_calls(self) -> List:
        return self.__calls

    def get_amount(self) -> Money:
        return self.__amount

    def get_seconds(self) -> time:
        return self.__seconds

    def calculate_fee(self) -> Money:
        result = MoneyZero.ZERO
        call: Call = None  # type: ignore

        unit_time = (
            self.__seconds.second
            + self.__seconds.minute * 60
            + self.__seconds.hour * 3600
        )
        """타입코드를 클래스는 낮은 응집도와 높은 결합도라는 문제 시달림."""
        for call in self.__calls:
            if self.__phone_type == PhoneType.REGULAR:
                result = result.plus(
                    self.__amount.times(call.get_duration() / (unit_time))
                )
            else:
                if call.start_time.hour >= Phone.LATE_NIGHT_HOUR:
                    result = result.plus(
                        self.__nightly_amount.times(call.get_duration() / (unit_time))
                    )
                else:
                    result = result.plus(
                        self.__regular_amount.times(call.get_duration() / (unit_time))
                    )
        return result
