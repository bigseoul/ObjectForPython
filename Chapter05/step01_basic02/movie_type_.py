from enum import Enum, auto


class MovieType(Enum):
    """https://docs.python.org/ko/3/library/enum.html
    https://www.daleseo.com/python-enum/

    auto() 선언된 순서대로 정수값 1, 2 ,3...

    list(MovieType) ->
    [<MovieType.AMOUNT_DISCOUNT: 1>,
    <MovieType.PERCENT_DISCOUNT: 2>,
    <MovieType.NONE_DISCOUNT: 3>]"""

    AMOUNT_DISCOUNT = auto()  # 금액 할인 정책
    PERCENT_DISCOUNT = auto()  # 비율 할인 정책
    NONE_DISCOUNT = auto()  # 미적용
