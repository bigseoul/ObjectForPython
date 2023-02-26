from bag import Bag
from ticket import Ticket


class Audience:
    def __init__(self, bag: Bag) -> None:
        self.__bag = bag

    # Bag 자료형
    def get_bag(self):
        return self.__bag


    def buy(self, ticket: Ticket):
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
