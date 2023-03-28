from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
from call_ import Call
from step02.rate_policy_ import RatePolicy
from money_ import Money
from money_zero import MoneyZero

if TYPE_CHECKING:
    from phone_ import Phone


class AdditionalRatePolicy(RatePolicy, metaclass=ABCMeta):
    def __init__(self, following: RatePolicy) -> None:
        """
        following은 RatePolicy 인스턴스를 받는 변수
        생성자 내부에서 following에 전달된 인스턴스에 대한 의존성 주입
        """
        self.__following = following

    def calculate_fee(self, phone: "Phone") -> Money:
        """
        1. following이 참고하는 인스턴스에게 calculate_fee()메시지 전달
        2. 1이 리턴되고 나서, 요금에 부가 정책을 적용하기 위해 _after_calculated() 메시지 전달
        """
        fee = self.__following.calculate_fee(phone)
        return self._after_calculated(fee)

    @abstractmethod
    def _after_calculated(self, fee: Money) -> Money:
        ...
