from typing import TYPE_CHECKING

from discount_condition_ import AbsDiscountCondition

"""
    from screening_ import Screening 그냥 박아 넣으면 circular error 생김
    
    Python typing으로 인한 순환 참조 대응책
    https://item4.blog/2017-12-03/Resolve-Circular-Dependency-on-Python-Typing/

    typing 모듈의 TYPE_CHECKING 상수는 runtime에는 False 값을 갖고 있습니다. 
    mypy 등의 정적 타입 검사기를 돌릴 때만 True가 됩니다. 
    이렇게 하면 순환 참조 문제를 해결할 수 있습니다.
"""
if TYPE_CHECKING:
    from screening_ import Screening


class SequenceCondition(AbsDiscountCondition):
    """
    아는 것: 할인조건이 적용될 회차
    하는 것: 상영조건이 할인조건에 맞는 지 확인해 bool로 리턴

    """

    def __init__(self, sequence: int) -> None:
        self.__sequence = sequence

    def __str__(self) -> str:
        return f"상영순번: {self.__sequence}"

    # override
    def is_satisfied_by(self, screening: "Screening"):
        """몇 번째 상영 순서인지에 따라 True 반환."""
        return screening.is_sequence(self.__sequence)
