from typing import TYPE_CHECKING

from default_discount_policy import DefaultDiscountPolicy

if TYPE_CHECKING:
    from money_ import Money
    from screening_ import Screening


class PercentDiscountPolicy(DefaultDiscountPolicy):
    """
    아는 것: 할인 조건
    하는 것: 영화가 할인 조건에 맞으면 '영화요금 * 비율' 해서 할인 요금 전달

    discount_amount: float 타임도 *args로 들어옮
    """

    def __init__(self, *args) -> None:  # 인자들이 args에 패킹(튜플)되어 들어감. 인자로 들어갈 땐 패킹
        temp_args = list(args)  # 할인율만 따로 빼내기 위해, 튜플(변경안됨)을 리스트로 변환

        for arg in temp_args:  # *try~catch나 에러 검증 필요.
            if (str(type(arg))) == "<class 'float'>":  # 인자로 건너 온, 할인율(float)과 할인조건 분리하기
                self.__percent = arg
                del temp_args[0]
                args = temp_args

        super().__init__(*temp_args)  # AbsDiscountPolicy에 인자로 전할 땐 패킹된 것을 언패킹

    # override
    def _get_discount_amount(self, screening: "Screening") -> "Money":
        """
        비율할인 정책이 적용된 할인 요금 계산한다.
        screening.get_movie_fee()가 필요한 이유, 영화요금을 기준으로 비율할인 하기 때문
        10000원 * 0.1 = 1000원
        """
        return screening.get_movie_fee().times(self.__percent)  # type: ignore
