"""
1. 영화 비용을 계산할 책임이 있음.
2. 영화 정보, 가격, 할인 정책, 할인 비용 정도 가지고 있음.
"""
from typing import TYPE_CHECKING, Optional

from movie_type_ import MovieType

if TYPE_CHECKING:
    from discount_condition_ import DiscountCondition
    from screening_ import Screening


class Movie:
    """DC에게 할인 조건이 있는 지 파악하기. 정책 적용은 그 뒤에 함.
        1. 순번조건 또는 기간 조건 둘 중에 하나라도 매칭하는 지 확인하기 위함.
        2. conditon이 여러개 일 수 있음.

        q. 왜 movie(Self)가 있는데, screening을 던지는 걸까?
        - DiscountCondtion은 할인 조건을 판단하기 위해 Screening의
        상영시간과 상영 순번을 아야야 한다. 그래서 screening을 따로 던지는 것

        자바의 스트림
        private boolean isDiscountable(Screening screening) {
            return discountConditions.stream()
                .anyMatch(condition -> condition.isSatisfiedBy(screening));
    }
    """

    def __init__(
        self,
        title: str,
        fee: int,
        discount_amount: int = 0,
        movie_type: Optional[MovieType] = None,
        *,  # *, 구문은 다음의 모든 인수가 위치 인수가 아닌 키워드 인수로 전달되어야 함을 나타내는 데 사용됩니다
        discount_conditions,
    ) -> None:
        self.__title = title
        self.__fee = fee
        self.__discount_amount = discount_amount
        self.__movie_type = movie_type
        self.__discount_conditions = list(discount_conditions)

    def __str__(self) -> str:
        return (
            f"Title: {self.__title}\n"
            f"Fee: {self.__fee}\n"
            f"Discount Amount: {self.__discount_amount}\n"
            f"Movie Type: {self.__movie_type}\n"
            f"Discount Conditions: {self.__discount_conditions}"
        )

    def calculate_movie_fee(self, screening):
        print("4. Movie: sending a is_Discountable() to interal")

        # DC에게 screen 정보가 할인 조건에 부합하는 지 확인해야 함. 일단 인터널 is_discountable에게 보내기
        if self.__is_discountable(screening):
            return self.__fee - self.__discount_amount  # Money타입으로 리턴할 거임.

    def __is_discountable(self, screening: "Screening") -> bool:
        for condition in self.__discount_conditions:
            if condition.is_satisfied_by(screening):
                return True
        return False
