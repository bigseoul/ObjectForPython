from enum import Enum, auto


class MovieType(Enum):
    AMOUNT_DISCOUNT = auto()  # 금액 할인 정책
    PERCENT_DISCOUNT = auto()  # 비율 할인 정책
    NONE_DISCOUNT = auto()  # 미적용
