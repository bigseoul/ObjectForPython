from enum import Enum, auto


class DiscountConditionType(Enum):
    SEQUENCE_DISCOUNT = auto()  # 순번조건
    PERIOD_DISCOUNT = auto()  # 기간조건
    NONE_DISCOUNT = auto()  # 미적용
