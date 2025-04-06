from money_ import Money
from call_ import Call
from rate_policy_ import RatePolicy
from basic_rate_policy_ import BasicRatePolicy


class Phone:
    """
    이 챕터의 핵심 클래스.
    핵심 중에 핵심은 calculate_fee 메서드. 이 메스가 rate_policy 메서드를 호출하는 것이 핵심.
    RatePolicy의 참조자가 있다. 이것이 합성. 의존성 주입
    """

    def __init__(self, rate_policy: RatePolicy) -> None:
        self.__rate_policy = rate_policy
        self.__calls = []

    def call(self, call):
        self.__calls.append(call)

    def get_calls(self) -> tuple:
        return tuple(self.__calls)

    """
    Phone 객체는 RatePolicy 인터페이스를 통해 요금 계산을 요청하며,
    자신(self)을 전달하여 정책이 통화 기록에 접근할 수 있게 함
    """

    def calculate_fee(self) -> Money:
        return self.__rate_policy.calculate_fee(self)
