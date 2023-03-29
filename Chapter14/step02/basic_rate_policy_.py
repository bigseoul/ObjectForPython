from abc import ABCMeta, abstractmethod
from rate_policy_ import RatePolicy
from phone_ import Phone
from money_ import Money
from call_ import Call
from fee_rule_ import FeeRule
from functools import reduce


class BasicRatePolicy(RatePolicy):
    """FeeRule 컬랙션을 이용해 전체 통화 요금 계산"""

    """main에서 처음 소환 되는 애, 물론 이 녀석을 실체화 녀석이 불리겠지만"""

    def __init__(self, *fee_rules: FeeRule) -> None:
        self.__fee_rules = list(fee_rules) #tuple to list

    # override

    def calculate_fee(self, phone: Phone) -> Money:
        """
        1st 호출 되는 메서드
        폰에서 call 리스트를 받는다.
        콜 하나를 빼서 __calculate 전달 -->
        """
        calls = phone.get_calls()
        fees = [self.__calculate(call) for call in calls]
        result = Money.wons(0)
        for fee in fees:
            result = result.plus(fee)
  
        return result

    def __calculate(self, call: Call) -> Money:
        """윗 메서드에서 전달받은 call을 FeeRule객체의 calculate_fee()에 전달"""
        fees = [rule.calculate_fee(call) for rule in self.__fee_rules]
        result = Money.wons(0)
        for fee in fees:
            result = result.plus(fee)
        return result
