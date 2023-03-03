from typing import TYPE_CHECKING
from datetime import time

if TYPE_CHECKING:
    from money_ import Money
    from discount_policy_ import AbsDiscountPolicy
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

    def check_movie(self):
        print("===movie===")
        print(self.__title)
        print(self.__duration)
        # self.__fee.check_amount() #18000원, 원래 영화값.
        print("dPolicy: ", self.__discount_policy)

    def get_fee(self):
        return self.__fee

    # 추상discountPolicy에 calculateDiscoutAmout 메시지를 전송해
    # 할인 요금을 받환 받는다.
    # Movie는 기본요금인 fee에서 반환된 할인 요금을 차감.
    def calculate_movie_fee(self, screening: "Screening"):
        return self.__fee.minus(
            self.__discount_policy.calculate_discount_amount(screening)
        )

    # 실행시간 때, 정책 변경
    def change_discount_policy(self, discount_policy: "AbsDiscountPolicy"):
        self.__discount_policy = discount_policy
