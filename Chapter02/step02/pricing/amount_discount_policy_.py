from typing import TYPE_CHECKING

from default_discount_policy import DefaultDiscountPolicy

if TYPE_CHECKING:
    from money_ import Money
    from screening_ import Screening


class AmountDiscountPolicy(DefaultDiscountPolicy):
    """정액 할인 정책"""

    def __init__(self, *args) -> None:
        temp_args = list(args)

        for arg in temp_args:
            if (str(type(arg))) == "<class 'money_.Money'>":
                self.__discount_amount = arg
                del temp_args[0]
                args = temp_args
            super().__init__(*temp_args)

    # override 4-1 내부 구현,(AmountDiscountPolicy, Percent~)에게 할인정도 계산해달라고 메시지 전달
    def _get_discount_amount(self, screening: "Screening") -> "Money":
        return self.__discount_amount  # type: ignore
