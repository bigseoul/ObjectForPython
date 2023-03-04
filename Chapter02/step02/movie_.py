from datetime import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discount_policy_ import AbsDiscountPolicy
    from money_ import Money
    from screening_ import Screening


class Movie:
    """
    아는 것: 타이틀, 영화길이, 요금, 할인정책(정보 전문가는 DiscountPolicy)
    하는 것: 할인 정책으로 할인 된 요금만큼 빠진 영화요금 계산.
    """

    def __init__(
        self,
        title: str,
        duration: time,
        fee: "Money",
        discount_policy: "AbsDiscountPolicy",
    ) -> None:
        self.__title = title
        self.__duration = duration  # 영화길이
        self.__fee = fee  # 영화가격
        self.__discount_policy = discount_policy #하나의 할인 정책만 받을 수 있음.

    def __str__(self) -> str:
        return f"영화이름: {self.__title}\n상영시간:{self.__duration}\n{self.__discount_policy}"

    def get_fee(self):
        return self.__fee

    def calculate_movie_fee(self, screening: "Screening") -> "Money":
        """
        추상 discountPolicy에 calculate_discount_amount() 메시지를 전송해 할인 요금을 받환 받는다.
        Movie는 영화가격에서 할인 요금을 차감.
        """
        return self.__fee.minus(
            self.__discount_policy.calculate_discount_amount(screening)
        )
