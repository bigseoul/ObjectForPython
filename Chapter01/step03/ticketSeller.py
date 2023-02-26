from audience import Audience
from ticket import Ticket
from ticketOffice import TicketOffice


class TicketSeller:
    """ticketSeller에서 getTicketOffice가 제거됨.
    TicketOffice에 대한 접근은 TicketSeller만 가능.
    step01에선 Theater가 했음."""

    def __init__(self, ticket_office: TicketOffice) -> None:
        self.__ticket_office = ticket_office

    def sell_to(self, audience: Audience):
        self.__ticket_office.sell_to(audience)
