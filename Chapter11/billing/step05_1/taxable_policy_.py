from money_ import Money
from rate_policy_ import RatePolicy
from additional_rate_policy_ import AdditionalRatePolicy


class TaxablePolicy(AdditionalRatePolicy):
    def __init__(self, tax_ratio: float, following: RatePolicy) -> None:
        """상위 클래스에 의존성 전달"""
        super().__init__(following)
        self.__tax_ratio = tax_ratio

    def _after_calculated(self, fee: Money) -> Money:
        return fee.plus(fee.times(self.__tax_ratio))
