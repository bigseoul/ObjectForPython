from datetime import time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from discount_policy_ import AbsDiscountPolicy
    from money_ import Money
    from screening_ import Screening


class Movie:
    # Movie("고질라VS콩", time(1, 53), Money.wons(18000), adp)
    def __init__(
        self,
        title: str,
        duration: time,
        fee: "Money",
        discount_policy: "AbsDiscountPolicy",
    ) -> None:
        self.__title = title
        self.__duration = duration  # 상영시간
        self.__fee = fee  # 영화가격
        self.__discount_policy = discount_policy

    def __str__(self) -> str:
        return f"영화이름: {self.__title}\n상영시간:{self.__duration}\n{self.__discount_policy}"

    def get_fee(self):
        return self.__fee

    # 추상discountPolicy에 calculateDiscoutAmout 메시지를 전송해
    # 할인 요금을 받환 받는다.
    # Movie는 기본요금인 fee에서 반환된 할인 요금을 차감.
    def calculate_movie_fee(self, screening: "Screening") -> "Money":
        return self.__fee.minus(
            self.__discount_policy.calculate_discount_amount(screening)
        )
