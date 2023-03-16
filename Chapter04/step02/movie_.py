from datetime import datetime, time
from typing import List

from discount_condition_ import DiscountCondition
from discount_condition_type_ import DiscountConditionType
from money_ import Money
from movie_type_ import MovieType


class Movie:
    """
    첫번째 질문, 무비가 어떤 데이터를 포함해야 하는가?
    두번째 질문, 무비가 이 데이터를 처리하기 위해 어떤 오퍼레리션을 필요한 지 묻는 것.

    Movie는 할인 정책의 종류를 인터페이스에 노출시키고 있음
    이번에는 메서드의 시그니처가 아닌, 메서드의 이름을 통해 3가지 할인 정책이 존재한다는 사실을 노출한다.
    calculateAmountDiscountedFee, calculatePercentDIscountedFee, calculateNoneDiscountedFee
    3개의 메서드는 할인 정책에 금액할인, 비율할인, 미적용 총 3가지가 존재한다는 사실을 노출함
    """

    def __init__(
        self,
        movie_type: "MovieType",
        title: str,
        running_time: time,
        fee: "Money",
        discount_amount: "Money",
        discount_percent: "float",
        discount_conditions: List["DiscountCondition"] = None,  # type: ignore
    ) -> None:
        self.__movie_type = movie_type
        self.__title = title
        self.__running_time = running_time
        self.__fee = fee
        self.__discount_amount = discount_amount
        self.__discount_percent = discount_percent
        self.__discount_conditions = discount_conditions or []

    def __str__(self) -> str:
        return f"{self.__title} ({self.__running_time}) - {self.__fee}"

    # movie객체에서 생성자 오버로드 여러 개 해줘야 함.
    # @classmethod 데코레이터 이용함.
    # 각 생성자에 맞는 클래스메서드명 붙이기

    @classmethod
    def from_movie_for_discount_percent(
        cls,
        cls_title: str,
        cls_running_time: time,
        cls_fee: "Money",
        cls_discount_percent: float,
        *cls_discount_conditions: "DiscountCondition",
    ):
        return cls(
            movie_type=MovieType.PERCENT_DISCOUNT,
            title=cls_title,
            running_time=cls_running_time,
            fee=cls_fee,
            discount_percent=cls_discount_percent,
            discount_amount=Money.from_wons(0),
            discount_conditions=list(cls_discount_conditions),
        )

    @classmethod
    def from_movie_for_discount_amount(
        cls, title, running_time, fee, discount_amount, *discount_conditions
    ):
        return cls(
            movie_type=MovieType.AMOUNT_DISCOUNT,
            title=title,
            running_time=running_time,
            fee=fee,
            discount_percent=0.0,
            discount_amount=discount_amount,
            discount_conditions=list(discount_conditions),
        )

    @classmethod
    def from_movie_for_non_discount(
        cls,
        cls_title: str,
        cls_running_time: time,
        cls_fee: "Money",
    ):
        return cls(
            movie_type=MovieType.NONE_DISCOUNT,  # movie type을 여기서 넣어줌.
            title=cls_title,
            running_time=cls_running_time,
            fee=cls_fee,
            discount_percent=0.0,
            discount_amount=Money.from_wons(0),
            discount_conditions=[],
        )

    # """할인정책 리턴, 정책별 요금 계산 메서드"""

    def get_movie_type(self) -> "MovieType":
        return self.__movie_type

    def calculate_amount_discounted_fee(self) -> "Money":
        if self.__movie_type != MovieType.AMOUNT_DISCOUNT:
            raise ValueError("This is not AMOUNT_DISCOUNT")
        if self.__fee is None:
            raise ValueError("Fee is None")
        return self.__fee - self.__discount_amount

    def calculate_percent_discounted_fee(self) -> "Money":
        if self.__movie_type != MovieType.PERCENT_DISCOUNT:
            raise ValueError("This is not PERCENT_DISCOUNT")
        if self.__fee is None:
            raise ValueError("Fee is None")
        return self.__fee - (self.__fee * self.__discount_percent)

    def calculate_none_discounted_fee(self) -> "Money":
        if self.__movie_type != MovieType.NONE_DISCOUNT:
            raise ValueError("This is not NONE_DISCOUNT")
        if self.__fee is None:
            raise ValueError("Fee is None")
        return self.__fee

    def is_discountable(self, when_screened: datetime, sequence: int) -> bool:
        """
        할인조건 목록을 가지고 있으므로 할인 여부를 판단하는 오퍼레이션이 필요
        when_screened를 통해 요일 알아내서, 받은 개별 요일이랑 비교하기
        """
        for condition in self.__discount_conditions:
            discount_condition: DiscountCondition = condition
            if discount_condition.get_type() == DiscountConditionType.PERIOD:
                if discount_condition.is_discountable(
                    when_screened.weekday(), when_screened  # type: ignore
                ):
                    return True
            elif discount_condition.is_discountable(sequence):
                return True
        return False
