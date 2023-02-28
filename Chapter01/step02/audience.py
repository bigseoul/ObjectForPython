from bag import Bag
from ticket import Ticket


class Audience:
    """
    관객이 Bag을 직접 처리하기 때문에 외부에서는
    더이상 관객이 가방을 소유하고 있다는 사실을 알필요가 없다.

    관객 클래스에서 getBag메서드를 제거할 수 있고 결과적으로
    Bag의 존재를 캡슐화 할 수 있다.
    """

    def __init__(self, bag: Bag) -> None:
        self.__bag = bag

    # def get_bag(self) -> Bag:
    #     return self.__bag

    def buy(self, ticket: Ticket) -> int:
        """초대장이 있는 경우와 없는 경우로 나눔"""
        if self.__bag.has_invitation():
            self.__bag.set_ticket(ticket)
            # 초대장이니 넘길 돈이 빵원
            return 0
        else:
            self.__bag.set_ticket(ticket)
            # 가장에서 돈 뺌
            self.__bag.minus_amount(ticket.get_fee())
            # 오피스에게 넘겨줄 돈, 리턴
            return ticket.get_fee()
