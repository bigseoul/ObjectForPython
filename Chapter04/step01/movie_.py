from datetime import time
from typing import TYPE_CHECKING

from discount_condition_type_ import DiscountConditionType
from movie_type_ import MovieType

if TYPE_CHECKING:
    from money_ import Money


class Movie:
    def __init__(
        self,
        movie_type: "MovieType",
        title: str,
        running_time: time,
        fee=None,
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
        self.__discount_condition = discount_conditions

    @classmethod
    def from_Movie_for_discount_percent(
        cls,
        cls_title: str,
        cls_running_time: time,
        cls_fee: "Money",
        cls_discount_percent: float,
        *cls_discount_conditions: list[DiscountConditionType]
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
        cls_title: str,
        cls_running_time: time,
        cls_fee: "Money",
        cls_discount_amount: "Money",
        *cls_discount_conditions: list[DiscountConditionType]
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
        cls_title: str,
        cls_running_time: time,
        cls_fee: "Money",
    ):
        return cls(
            movie_type=MovieType.NONE_DISCOUNT,  # movie type을 여기서 넣어줌.
            title=cls_title,
            running_time=cls_running_time,
            fee=cls_fee,
        )

    # movie객체에서 생성자 오버로드 여러 개 해줘야 함.
    # @classmethod 데코레이터 이용함.
    # 각 생성자에 맞는 클래스메서드명 붙이기

    """https://bit.ly/3ds3FX7
        게터 세터, 파이썬 스럽지 않은 코드...자바스타일 """

    @property
    def movie_type(self):
        return self.__movie_type

    @movie_type.setter
    def movie_type(self, movie_type):
        self.__movie_type = movie_type

    """문제)게터/세터 캡슐화 위반. 
    -접근수정자가 Public; 머니타입의 fee라는 인스턴스변수가 있다는 사실을 외부 인터페이스에 드러냄. 
    -근본적인 원인은 객체가 수행할 책임이 아니라 내부에 저장할 데이터에 초점뒀기 때문.
    -설계할 때, 협력을 고민하지 않음녀, 과도한 접근자와 수정자를 가지게 되는 경향 있음.
    -이는 객체가 사용될 문맥을 추측할 수 밖에 없기에 어떤 상황에서도 해당 객체가 사용될 수 있게 
    최대한 많은 접근자/수정자를 추가하게 되는 것.
    """

    @property
    def fee(self):
        return self.__fee

    @fee.setter
    def fee(self, fee):
        self.__fee = fee

    @property
    def discount_conditions(self):
        return self.__discount_condition

    @discount_conditions.setter
    def discount_conditions(self, *discount_conditions):
        self.__discount_condition = list(discount_conditions)

    @property
    def discount_amount(self):
        return self.__discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        self.__discount_amount = discount_amount

    @property
    def discount_percent(self):
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, discount_percent):
        self.__discount_percent = discount_percent
