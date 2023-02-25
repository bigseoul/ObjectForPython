from ticketOffice_ import TicketOffice


class TicketSeller:
    """
    판매원은 매표소에서 초대장을 티켓으로 교환해 주거나 티켓을 판매하는 역할을 수행.
    판매원을 구현한 TicketSeller 클래스는 자신이 일하는 tiketOffice를 알고 있어야 한다.
    """

    def __init__(self, office: TicketOffice) -> None:
        self.__office = office

    def get_ticket_office(self) -> TicketOffice:
        return self.__office

    # 뭣이 들어오는지 보자. 백만원과 ticket 객체들이 들어옴.
    # def show_ticket_office(self):
    #     print(self.__ticketOffice)

    # def sell_to(self, audience):
    #     print("sellTo")
