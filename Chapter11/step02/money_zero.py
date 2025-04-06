# https://www.clien.net/service/board/cm_app/17629739
# 이름 같은 클래스를 이용한 것.
# 나중에 싱글턴으로 구현해야 함.

from money_ import Money


class MoneyZero(Money):
    ZERO = Money.wons(0)
