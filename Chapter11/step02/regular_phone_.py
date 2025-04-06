from datetime import time
from typing import TYPE_CHECKING, List
from phone_ import Phone
from call_ import Call
from money_ import Money


"""
super().__init__()으로 부모의 __init__() 생성자 호출필요.
그래야 __calls 쓸 수 있음.
자바는 인스턴스 변수를 생성자 밖에서 선언할 수 있으나
파이썬은 생성자 밖에 선언하면 클래스 변수(공용)가 됨. 
따라서 생성자를 만들수 밖에 없음.

자식 생성자에서 부모 생성자를 호출하지 않으면, 
부모의 인스턴스 __call변수를 쓸 수 없음 

https://supermemi.tistory.com/178
"""


class RegularPhone(Phone):
    def __init__(self, amount: "Money", seconds: "time") -> None:
        self.__amount = amount
        self.__seconds = seconds
        super().__init__()

    """일반 요금제 통화 한건 계산"""
    # Override
    def _calculate_call_fee(self, call: "Call") -> "Money":

        unit_time = (
            self.__seconds.second
            + self.__seconds.minute * 60
            + self.__seconds.hour * 3600
        )

        return self.__amount.times(call.get_duration() / (unit_time))
