from ticket_ import Ticket


class TicketOffice:
    """
    티켓오피스는 판매하거나 교환해줄 티켓의 목록과 판매 금액을 인스턴스 변수로 포함한다.
    """

    def __init__(self, amount: int, ticket_list: list[Ticket]) -> None:
        self.__amount = amount
        self.__ticket_list = ticket_list

    # 생성한 티켓을 윗장부터 없앰.
    def get_ticket(self) -> Ticket:
        a_ticket_sold = self.__ticket_list[0]
        del self.__ticket_list[0]
        return a_ticket_sold

    def minus_amout(self, amount: int):
        self.__amount -= amount

    def plus_amount(self, amount: int):
        self.__amount += amount
        print("office amount is: ", self.__amount)
