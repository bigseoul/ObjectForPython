from money_ import Money
from call_ import Call
from step02.rate_policy_ import RatePolicy
from basic_rate_policy_ import BasicRatePolicy


class Phone:
    """
    RatePolicy의 참조자가 있다. 이것이 합성. 의존성 주입
    다양한 종류의 객체와 협력하기 위해 합성 관계를 사용하는 경우,
    합성되는 객체의 타입을 인터페이스나 추상 클래스로 선언하고 의존성 주입해
    런타임에 필요한 객체를 설정할 수 있도록 구현하는 것이 일반적
    """

    """
    rate_policy는 최상위 클래스, 여기에 자식 RegularPolicy 레퍼런드 연결
    이걸 업캐스팅으로 이해해도 되려나?
    """

    def __init__(self, rate_policy: RatePolicy) -> None:
        self.__rate_policy = rate_policy
        self.__calls = []

    def call(self, call: Call):
        self.__calls.append(call)

    def get_calls(self) -> tuple:
        return tuple(self.__calls)

    """RegularPolicy의 BasicPolicy에 phone객체 주소(self)를 넘김"""

    def calculate_fee(self) -> Money:
        return self.__rate_policy.calculate_fee(self)
