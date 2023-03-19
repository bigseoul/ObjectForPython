"""
1. 영화 비용을 계산할 책임이 있음.
2. 영화 정보, 가격, 할인 정책, 할인 비용 정도 가지고 있음.
"""
import logging

logging.basicConfig(level=logging.INFO)
from typing import TYPE_CHECKING, List, Optional

from money_ import Money
from movie_type_ import MovieType
from period_condition_ import PeriodCondition
from sequence_condition_ import SequenceCondition

if TYPE_CHECKING:
    from screening_ import Screening


class Movie:
    def __init__(
        self,
        title: str,
        fee: Money,
        discount_amount: Money = Money.from_wons(0),
        discount_percent: float = 0.0,
        movie_type: Optional[MovieType] = None,
        sequence_conditions: Optional[List[SequenceCondition]] = None,
        period_conditions: Optional[List[PeriodCondition]] = None,
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__discount_amount = discount_amount
        self.__discount_percent = discount_percent
        self.__movie_type = movie_type
        self.__period_conditions = period_conditions or []
        self.__sequence_conditions = sequence_conditions or []

    def __str__(self) -> str:
        return (
            f"Title: {self.__title}\n"
            f"Fee: {self.__fee}\n"
            f"Discount Amount: {self.__discount_amount}\n"
            f"Discount Percent: {self.__discount_percent}\n"
            f"Movie Type: {self.__movie_type}\n"
            f"Sequence Conditions: {', '.join(map(str, self.__sequence_conditions))}\n"
            f"Period Conditions: {', '.join(map(str, self.__period_conditions))}"
        )

    def calculate_movie_fee(self, screening) -> Money:
        # DC에게 screen 정보가 할인 조건에 부합하는 지 확인해야 함. 일단 인터널 is_discountable에게 보내기
        # 4-1
        if self.__is_discountable(screening) == True:
            return self.__fee - self.__calculate_discount_amount()
        else:
            return self.__fee

    """step02 해결방법 1. 목록을 따로 유지한다."""

    def __is_discountable(self, screening: "Screening") -> bool:
        return self.__check_period_conditions(
            screening
        ) or self.__check_sequence_conditions(screening)

    def __check_period_conditions(self, screening) -> bool:
        return any(
            condition.is_satisfied_by(screening)
            for condition in self.__period_conditions
        )

    def __check_sequence_conditions(self, screening) -> bool:
        return any(
            condition.is_satisfied_by(screening)
            for condition in self.__sequence_conditions
        )

    def __calculate_discount_amount(self) -> Money:
        # if self.__movie_type == MovieType.AMOUNT_DISCOUNT:
        #     return self.__calculate_amount_discount_amount()
        # elif self.__movie_type == MovieType.PERCENT_DISCOUNT:
        #     return self.__calculate_percent_discount_amount()
        # elif self.__movie_type == MovieType.NONE_DISCOUNT:
        #     return self.__calculate_none_discount_amount()
        # else:
        #     raise ValueError("Wrong DC type")

        if self.__movie_type is None:
            raise ValueError("Wrong DC type")

        discount_calculators = {
            MovieType.AMOUNT_DISCOUNT: self.__calculate_amount_discount_amount,
            MovieType.PERCENT_DISCOUNT: self.__calculate_percent_discount_amount,
            MovieType.NONE_DISCOUNT: self.__calculate_none_discount_amount,
        }

        discount_calculator = discount_calculators.get(self.__movie_type)

        if discount_calculator is None:
            raise ValueError("Wrong DC type")

        return discount_calculator()

    def __calculate_amount_discount_amount(self) -> Money:
        return self.__discount_amount

    def __calculate_percent_discount_amount(self) -> Money:
        return self.__fee * self.__discount_percent

    def __calculate_none_discount_amount(self) -> Money:
        return Money.from_wons(0)
