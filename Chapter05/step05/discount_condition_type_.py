from enum import Enum, auto

class DiscountConditionType(Enum):
    SEQUENCE = auto()  # 순번조건
    PERIOD = auto()  # 기간조건
