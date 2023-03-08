from typing import TYPE_CHECKING
from discount_condition_type_ import DiscountConditionType
from movie_type_ import MovieType
from datetime import date, time, datetime


if TYPE_CHECKING:
    from money_ import Money
    from discount_condition_ import DiscountCondition


class Movie:
    def __init__(
        self,
        movie_type: "MovieType",
        title,
        running_time,
        fee: "Money",
        discount_amount=None,
        discount_percent=None,
        discount_conditions=None,
    ) -> None:
        self.__movie_type = movie_type
        self.__title = title
        self.__running_time = running_time
        self.__fee = fee
        self.__discount_amount = discount_amount
        self.__discount_percent = discount_percent
        # from_Movie_**에서 args를 list()받아서 보내줌. 패킹할 필요 없음.
        self.__discount_conditions = discount_conditions

    """
    movie객체에서 생성자 오버로드 여러 개 해줘야 함.
    @classmethod 데코레이터 이용함.
    각 생성자에 맞는 클래스메서드명 붙이기
    """

    @classmethod
    def from_Movie_for_discount_percent(
        cls,
        cls_title,
        cls_running_time,
        cls_fee: "Money",
        cls_discount_percent,
        *cls_discount_conditions
    ):
        return cls(
            movie_type=MovieType.PERCENT_DISCOUNT,
            title=cls_title,
            running_time=cls_running_time,
            fee=cls_fee,
            discount_percent=cls_discount_percent,
            discount_conditions=list(cls_discount_conditions),
        )

    @classmethod
    def from_Movie_for_discount_amount(
        cls,
        cls_title,
        cls_running_time,
        cls_fee: "Money",
        cls_discount_amount,
        *cls_discount_conditions
    ):
        return cls(
            movie_type=MovieType.AMOUNT_DISCOUNT,
            title=cls_title,
            running_time=cls_running_time,
            fee=cls_fee,
            discount_amount=cls_discount_amount,
            discount_conditions=list(cls_discount_conditions),
        )

    @classmethod
    def from_Movie_for_non_discount(
        cls,
        cls_title,
        cls_running_time,
        cls_fee: "Money",
    ):
        return cls(
            movie_type=MovieType.NONE_DISCOUNT,  # movie type을 여기서 넣어줌.
            title=cls_title,
            running_time=cls_running_time,
            fee=cls_fee,
        )

    """할인정책 리턴, 정책별 요금 계산 메서드"""

    def get_Movie_type(self) -> "MovieType":
        return self.__movie_type

    def calculate_amount_discounted_fee(self) -> "Money":
        if self.__movie_type != MovieType.AMOUNT_DISCOUNT:
            raise ValueError("This is not AMOUNT_DISCOUNT")
        return self.__fee.minus(self.__discount_amount)

    def calculate_percent_discounted_fee(self) -> "Money":
        if self.__movie_type != MovieType.PERCENT_DISCOUNT:
            raise ValueError("This is not PERCENT_DISCOUNT")
        return self.__fee.minus(self.__fee.times(self.__discount_percent))

    def calculate_none_discounted_fee(self) -> "Money":
        if self.__movie_type != MovieType.NONE_DISCOUNT:
            raise ValueError("This is not NONE_DISCOUNT")
        return self.__fee

    """할인조건 목록을 가지고 있으므로 할인 여부를 판단하는 오퍼레이션이 필요
        when_screened를 통해 요일 알아내서, 받은 개별 요일이랑 비교하기
    """

    def is_discountable(self, when_screened: datetime, sequence) -> bool:
        for condition in self.__discount_conditions:
            temp_condition: "DiscountCondition" = condition
            if temp_condition.get_type() == DiscountConditionType.PERIOD:
                if temp_condition.is_discountable(
                    when_screened.weekday(), when_screened
                ):
                    return True
            else:
                if temp_condition.is_discountable(sequence):
                    return True
        return False
