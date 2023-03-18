"""
1. 영화 비용을 계산할 책임이 있음.
2. 영화 정보, 가격, 할인 정책, 할인 비용 정도 가지고 있음.
"""
import logging

logging.basicConfig(level=logging.INFO)
from money_ import Money
from money_zero import MoneyZero

from movie_type_ import MovieType
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from screening_ import Screening
    from discount_condition_ import AbsDiscountCondition
    from period_condition_ import PeriodCondition
    from sequence_condition_ import SquenceCondition


    """ 
    self.__period_conditions = period_conditions
    self.__squence_conditions = squence_conditions
    //메인에서 리스트로 던져서 보내야 하나?
    // [sq1, sq2] 이렇게 묶어서 보낸다. list(sq1, sq2) 아님
    """
class Movie:
    def __init__(
        self,
        title,
        fee: "Money",
        discount_amount=None,
        discount_percent=None,
        movie_type=None,
        *discount_conditions: "AbsDiscountCondition",
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__discount_amount = discount_amount
        self.__discount_percent = discount_percent
        self.__movie_type = movie_type
        self.__discount_conditions = list(discount_conditions)

    def calculate_movie_fee(self, screening) -> Money:
        logging.info("req Movie: sending a __is_Discountable()")

        # DC에게 screen 정보가 할인 조건에 부합하는 지 확인해야 함. 일단 인터널 is_discountable에게 보내기
        # 4-1
        if self.__is_discountable(screening) == True:
            logging.info("res Movie: sending a result from __calculate_discount_amount()")
            return self.__fee.minus(
                self.__calculate_discount_amount()
            )  # Money타입으로 리턴할 거임.

    """step03 """
    def __is_discountable(self, screening: "Screening") -> bool :
        result = False
        for condition in self.__discount_conditions:
            temp_condition: "AbsDiscountCondition" = condition
            if temp_condition.is_satisfied_by(screening) == True:
                result = True
        logging.info("res Movie: sending a result from __is_discountable()")
        return result

    def __calculate_discount_amount(self) -> Money:
        logging.info("res Movie: sending a result from __calculate_discount_amount()")
        if self.__movie_type == MovieType.AMOUNT_DISCOUNT:
            return self.__calculate_amount_discount_amount()
        elif self.__movie_type == MovieType.PERCENT_DISCOUNT:
            return self.__calculate_percent_discount_amount()
        elif self.__movie_type == MovieType.NONE_DISCOUNT:
            return self.__calculate_none_discount_amount()
        else:
            raise ValueError("Wrong DC type")


    def __calculate_amount_discount_amount(self) -> Money:
        return self.__discount_amount

    def __calculate_percent_discount_amount(self) -> Money:
        return self.__fee.times(self.__discount_percent)

    def __calculate_none_discount_amount(self) -> Money:
        return MoneyZero.ZERO
