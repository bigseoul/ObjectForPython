import logging

logging.basicConfig(level=logging.INFO)
from typing import TYPE_CHECKING, List, Optional

from discount_condition_ import DiscountCondition
from money_ import Money
from movie_type_ import MovieType

if TYPE_CHECKING:
    from screening_ import Screening


class Movie:
    """
    1. 영화 비용을 계산할 책임이 있음.
    2. 영화 정보, 가격, 할인 정책, 할인 비용 정도 가지고 있음."""

    def __init__(
        self,
        title: str,
        fee: Money,
        discount_amount: Money = Money.from_wons(0),
        discount_percent: float = 0.0,
        movie_type: Optional[MovieType] = None,
        *,  # *, 구문은 다음의 모든 인수가 위치 인수가 아닌 키워드 인수로 전달되어야 함을 나타내는 데 사용됩니다
        discount_conditions: Optional[List[DiscountCondition]] = None,
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__discount_amount = discount_amount
        self.__discount_percent = discount_percent
        self.__movie_type = movie_type
        self.__discount_conditions = discount_conditions if discount_conditions else []

    def __str__(self) -> str:
        return (
            f"Title: {self.__title}\n"
            f"Fee: {self.__fee}\n"
            f"Discount Amount: {self.__discount_amount}\n"
            f"Movie Type: {self.__movie_type}\n"
            f"Discount Conditions: {self.__discount_conditions}"
        )

    def calculate_movie_fee(self, screening) -> Money:
        # DC에게 screen 정보가 할인 조건에 부합하는 지 확인해야 함. 일단 인터널 is_discountable에게 보내기
        # 4-1
        if self.__is_discountable(screening) == True:
            logging.info(
                "res Movie: sending a result from __calculate_discount_amount()"
            )
            return self.__fee - self.__calculate_discount_amount()
        else:
            return self.__fee

    def __is_discountable(self, screening: "Screening") -> bool:
        for condition in self.__discount_conditions:
            temp: "DiscountCondition" = condition
            if temp.is_satisfied_by(screening):
                return True
        return False

    def __calculate_discount_amount(self) -> Money:
        # if self.__movie_type == MovieType.AMOUNT_DISCOUNT:
        #     return self.__calculate_amount_discount_amount()
        # elif self.__movie_type == MovieType.PERCENT_DISCOUNT:
        #     return self.__calculate_percent_discount_amount()
        # elif self.__movie_type == MovieType.NONE_DISCOUNT:
        #     return self.__calculate_none_discount_amount()
        # else:
        #     raise ValueError("Wrong DC type")

        """
        This code maps each MovieType to its corresponding discount calculation method in the discount_calculators dictionary.
        The get() method is then used to retrieve the appropriate discount calculation method based on self.__movie_type.
        If no matching method is found, a ValueError is raised.
        Finally, the selected discount calculation method is called and its result is returned.
        """
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
