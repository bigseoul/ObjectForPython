from audience import Audience
from bag import Bag
from ticket import Ticket
from ticketSeller import TicketSeller


class Theater:
    """
    극장이 직접 티켓셀러를 통해 티켓과 돈을 다룰 수 없음
    극장은 티켓오피스가 티켓 셀러 안에 있는지 알 수 없음.
    극장은 그저 티켓셀러가 sellTo를 통해 메시지(인터페이스)를 이해하고 응답한다는 사실만 앎.
    관객 객체 내용이 바뀌더라도 극장 객체를 바꿀 필요가 없음.
    """

    def __init__(self, ticket_seller: TicketSeller) -> None:
        self.__ticket_seller = ticket_seller

    def enter(self, audience: Audience):
        """
        step01: 극장은 관람객 가방에 초대장이 있는지 없는 지 확인

         문제는 극장이 매표소에 함부로 접근하고,
         더 큰 문제는 극장이 고객의 가방에 직접 접근한다.
         상식과 다른 수행 방식이라 이해하기 힘든 코드.

         enter 메서드를 이해하기 위해선 많은 것을 한 번에 알아야 한다.
         관람객이 가방(돈과 티켓)을 가지고,
         티켓셀러가 티켓오피스에서 티켓을 판매하고
         티켓오피스에는 돈과 티켓 있다는 사실을 알아야 함.

         또한 관람객과 티켓셀러를 변경하면 아래 코드도 변경해야 함.
         의존성이 높은 코드.
        """
        self.__ticket_seller.sell_to(audience)

    # def enter(self, audience: Audience):
    #     """초대장이 있는 경우와 없는 경우로 나눔"""
    #     if audience.get_bag().has_invitation():  # True/False
    #         # Ticket 생성
    #         ticket: Ticket = self.__ticket_seller.get_ticket_office().get_ticket()
    #         # 오디언스에게 티켓 주기
    #         audience.get_bag().set_ticket(ticket)
    #     else:
    #         # Ticket 생성
    #         ticket: Ticket = self.__ticket_seller.get_ticket_office().get_ticket()
    #         # 오디언스 지갑에서 티켓값 빼기
    #         audience.get_bag().minus_amount(ticket.get_fee())
    #         # 극장 계좌에 티켓값 넣기
    #         self.__ticket_seller.get_ticket_office().plus_amount(ticket.get_fee())
    #         # 오디언스에게 티켓 주기
    #         audience.get_bag().set_ticket(ticket)
