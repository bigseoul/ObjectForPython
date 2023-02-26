from audience import Audience
from ticket import Ticket


class TicketOffice:
    def __init__(self, amount, ticket_list: list) -> None:
        self.__amount = amount
        self.__ticket_list = ticket_list

    # 생성한 티켓을 윗장부터 없앰.
    def __get_ticket(self):
        a_ticket_sold = self.__ticket_list[0]
        del self.__ticket_list[0]
        return a_ticket_sold

    def __plus_amount(self, amount):
        self.__amount += amount
        print("office amount is-: ", self.__amount)

    def minus_amout(self, amount):
        self.__amount -= amount

    def sell_to(self, audience: Audience):
        """티켓오피스가 관객에게
        직접 표를 판매하기 때문에 의존성 추가됨

        따라서 기존 스탭02처럼 바꿔,
        관객에 대한 결합도를 낮춘다
        """
        self.__plus_amount(audience.buy(self.__get_ticket()))
