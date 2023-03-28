from fixed_fee_policy_ import FixedFeePolicy
from money_ import Money
from datetime import time, timedelta
from call_ import Call
from phone_ import Phone


class DurationDiscountRule(FixedFeePolicy):
    """
    초기 A분 동안 B초당 C원
    A분~D분까지 B초당 D원
    D분 초과시 B초당 E원

    ex) 초기 1분동안 10초당 50원, 초기 1분 이후 10초당 20원

    from_time과 to_time에 뭐가 들어가는 거야?
    https://dataonair.or.kr/db-tech-reference/d-lounge/technical-data/?mod=document&uid=236591

    """

    def __init__(
        self, amount: Money, seconds: time, from_time: timedelta, to_time: timedelta
    ) -> None:
        super().__init__(amount, seconds)
        self.__from_time = from_time
        self.__to_time = to_time

    def calculate(self, call: Call) -> Money:
        if call.get_duration() > self.__to_time:
            print(call.get_duration(), " ", self.__to_time)
            return Money.wons(0)

        if call.get_duration() < self.__from_time:
            print(call.get_duration(), " ", self.__from_time)
            return Money.wons(0)

        # 부모 클래스의 calculateFee(phone)은 Phone 클래스를 파라미터로 받는다.
        # calculateFee(phone)을 재사용하기 위해 데이터를 전달할 용도로 임시 Phone을 만든다.

        # 왜 켓프롬에 self.__시간들을 더하는 거지?
        phone = Phone(None)  # type: ignore
        phone.call(
            Call(
                (call.get_from() + self.__from_time),
                (call.get_from() + self.__to_time)
                if (call.get_duration() > self.__to_time)
                else (call.get_to()),
            )
        )

        return super().calculate_fee(phone)
