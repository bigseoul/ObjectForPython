from discount_policy_ import AbsDiscountPolicy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from screening_ import Screening


class AmountDiscountPolicy(AbsDiscountPolicy):
    # 인자들이 args에 패킹(튜플)되어 들어감. 인자로 들어갈 땐 패킹
    def __init__(self, *args) -> None:
        temp_args = list(args)

        # SequenceCondition 객체만 걸러내기
        for arg in temp_args:
            if (str(type(arg))) == "<class 'money_.Money'>":
                self.__discount_amount = arg
                del temp_args[0]
                args = temp_args #앤 뭐야?
            # super. 이라고 하면, descriptor '__init__' requires a 'super' object but received
            super().__init__(*temp_args)

    def get_discount_amount(self, screening: "Screening"):
        return self.__discount_amount
