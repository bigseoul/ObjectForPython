from invitation import Invitation
from ticket import Ticket


class Bag:
    """
    Audience jisoo = new Audience(new Bag(20000));만 고려
    따라서, 매개변수에 20000만 들어옮. invitation과 ticket 않넣음
    파이썬은 생성자 오버로드가 없으나 if-elif로 만들 수 있음.

    생성자 오버로딩이 안되므로, if-else로 분기
    """

    def __init__(self, amount, invitation: Invitation = None) -> None:  # type: ignore
        if invitation is None:
            self.__amount = amount
            self.__invitation = None
        else:
            self.__amount = amount
            self.__invitation = invitation

    def has_invitation(self):
        """초대장 없지 않으면 True반환"""
        return self.__invitation != None

    def has_ticket(self):
        """현재 필요 없는 기능"""
        pass

    def set_ticket(self, ticket: Ticket):
        self.__ticket = ticket

    def check_amount(self):
        print(self.__amount)

    def minus_amount(self, amount):
        """티켓값이 빠져나간 거 확인 20000-5000 = 15000"""
        self.__amount -= amount
        # print("jisoo: ", self.__amount)

    def plus_amount(self, amount):
        self.__amount += amount
