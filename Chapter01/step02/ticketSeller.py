from audience import Audience
from ticketOffice import TicketOffice


class TicketSeller:
    """ticketSeller에서 getTicketOffice가 제거됨.
    TicketOffice에 대한 접근은 TicketSeller만 가능.
    step01에선 Theater가 했음."""

    def __init__(self, ticket_office: TicketOffice) -> None:
        self.__ticket_office = ticket_office

    # def get_ticket_office(self):
    #     return self.__office

    def sell_to(self, audience: Audience):

        self.__ticket_office.plus_amount(
            audience.buy(self.__ticket_office.get_ticket())
        )
        # """초대장이 있는 경우와 없는 경우로 나눔"""
        # if audience.get_bag().has_invitation():  # True/False
        #     # Ticket 생성
        #     ticket: Ticket = self.__ticket_office.get_ticket()
        #     # 오디언스에게 티켓 주기
        #     audience.get_bag().set_ticket(ticket)
        # else:
        #     # Ticket 생성
        #     ticket: Ticket = self.__ticket_office.get_ticket()
        #     # 오디언스 지갑에서 티켓값 빼기
        #     audience.get_bag().minus_amount(ticket.get_fee())
        #     # 극장 계좌에 티켓값 넣기
        #     self.__ticket_office.plus_amount(ticket.get_fee())
        #     # 오디언스에게 티켓 주기
        #     audience.get_bag().set_ticket(ticket)
