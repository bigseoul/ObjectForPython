""" 
    decimal 사용법
    https://www.daleseo.com/python-float-decimal/
    
    생성자에 문자열 대신에 숫자를 넘기면 float 타입을 
    사용했을 때와 동일한 문제가 발생하게 된다는 것입니다           

    정적 메서드는 유틸리티 메서드를 구현할 때 많이 사용됩니다.

    https://www.daleseo.com/python-class-methods-vs-static-methods/
    예를 들어, 위의 StringUtils 클래스는 2개의 정적 메서드로 
    이루어져 있습니다. toCamelcase 메서드는 
    뱀 스타일(snake_case)의 문자열을 
    낙타 스타일로(CamelCase)로 변환해주며, 
    toSnakecase는 그 역방향의 변환을 해줍니다. 
    이 두 개의 메서드는 매개 변수로 넘어온 문자열에만 의존하는 
    순수한(pure) 함수이기 때문에 굳이 클래스의 일부로 선언할 
    필요는 없지만, 이렇게 비슷한 류의 여러 유틸리티 메서드를 
    하나의 클래스의 묶어두고 싶을 때 정적 메서드로 선언할 수 있습니다.
"""
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money_ import Money


class Money:
    # ZERO = Money.wons(0) #

    @staticmethod
    def wons(amount: int):
        return Money(Decimal(str(amount)))

    # 위에 있는 static wons에서 Money객체를 만들고 인자로 Decimal을 던져
    # 여기서 math.trunc(amount)로 소수점 이하 버리기하면, int로 변환되는데... 흠.
    # 그렇다고 다시한번 변환하는 것도 웃긴데...won에서 Decimal로 변환해서 던졌는데
    def __init__(self, amount: Decimal) -> None:
        self.__amount = amount

    def plus(self, amount: "Money"):
        return Money(self.__amount + amount.__amount)

    # 영화 가격(Money amount.__amount)에서
    # 일정 금액(amount_discount_policy객채의 self.__amount) 만큼 할인해준다.
    def minus(self, amount: "Money"):
        # print("movie: ", type(self.__amount))
        # __은 private인데, 이렇게 직접 접근하면 안될텐데?!
        # print("amount_disPol: ", type(amount.__amount))
        # print(self.__amount - amount.__amount)
        return Money(self.__amount - amount.__amount)

    def times(self, percent: float):
        return Money(self.__amount * Decimal(str(percent)))

    def is_less_than(self, other: "Money"):
        return self.__amount < other.__amount

    def is_greater_than_or_equal(self, other: "Money"):
        return self.__amount >= other.__amount

    def check_amount(self):
        print("===movie_amount====")
        print(self.__amount)
