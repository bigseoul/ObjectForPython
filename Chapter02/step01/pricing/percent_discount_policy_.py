from typing import TYPE_CHECKING

from discount_policy_ import AbsDiscountPolicy

if TYPE_CHECKING:
    from money_ import Money
    from screening_ import Screening


class PercentDiscountPolicy(AbsDiscountPolicy):
    """discount_amount: float 타임도 *args로 들어옮"""

    # 인자들이 args에 패킹(튜플)되어 들어감. 인자로 들어갈 땐 패킹
    def __init__(self, *args) -> None:
        # 할인율만 따로 빼내기 위해, 튜플을 리스트로 변환
        temp_args = list(args)

        # 할인율을 건지기 위해, 타입 비교해서 args에서 없앰.
        # 포문 안에 있더라도 self.__이면 인스턴스 변수라서 안사라지나?
        # *try~catch나 에러 검증 필요.

        for arg in temp_args:
            # type메서드의 결과값?(얘는 자료형이 뭔데?)을 string 객체로 만듦
            if (str(type(arg))) == "<class 'float'>":
                self.__percent = arg
                del temp_args[0]
                args = temp_args
        # 인자로 전해질 땐 패킹된 것을 언패킹
        super().__init__(*temp_args)

    # self._percent는 float, screening.get_movie_fee()는 money 객체이므로 연산 안됨.
    # 따라서, money안에 있는 decimal을 끄집어 내줘야 하는데....
    # Money 객체안에 times()가 있었네 ;;
    def get_discount_amount(self, screening: "Screening") -> "Money":
        return screening.get_movie_fee().times(self.__percent)  # type: ignore
