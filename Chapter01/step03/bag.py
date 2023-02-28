from invitation import Invitation
from ticket import Ticket


class Bag:
    def __init__(self, amount: int, invitation: Invitation) -> None:
        if invitation is None:
            self.__amount = amount
            self.__invitation = None
        else:
            self.__amount = amount
            self.__invitation = invitation

    def hold(self, ticket: Ticket) -> int:
        """
        step2 에서 추가, 가방 캡슐화
        초대장 없지 않으면 True반환
        """
        if self.__has_invitation():
            self.__set_ticket(ticket)
            return 0
        else:
            self.__set_ticket(ticket)
            self.__minus_amount(ticket.get_fee())
            return ticket.get_fee()

    def __has_invitation(self):
        return self.__invitation != None

    def __set_ticket(self, ticket: Ticket):
        self.__ticket = ticket

    def __minus_amount(self, amount):
        """티켓값이 빠져나간 거 확인 20000-5000 = 15000"""
        self.__amount -= amount
        # print("jisoo: ", self.__amount)

    def __plus_amount(self, amount):
        self.__amount += amount

    def has_ticket(self):
        """현재 필요 없는 기능: has_ticket"""
        pass
