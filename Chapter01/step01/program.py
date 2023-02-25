from datetime import datetime

from audience_ import Audience
from bag_ import Bag
from invitation_ import Invitation
from theater_ import Theater
from ticket_ import Ticket
from ticketOffice_ import TicketOffice
from ticketSeller_ import TicketSeller

if __name__ == "__main__":

    # 티켓 2장 만들기, 자바의 배열을 파이썬의 리스트 등으로 이해해야
    ticket_list = list()  # = []
    for i in range(2):
        ticket_list.append(Ticket())

    # 티켓셀러 -> 티켓 오피스 -> 티켓(위에서 만든)
    ticket_seller = TicketSeller(TicketOffice(1000000, ticket_list))

    # No invitation Case
    jisoo = Audience(Bag(20000))

    # Invitation Case
    jennie = Audience(Bag(0, Invitation(datetime(2022, 12, 8))))

    # 극장1 객체 생성, init class
    theater1 = Theater(ticket_seller)

    # 극장1 객체에 관객 객체 인자로 전달
    theater1.enter(jisoo)  # ticket
    theater1.enter(jennie)  # invitation

    # 테스트 코드 : 뭣이 들어오는지 보자. 백만원과 ticket 객체들이 들어옴.

    # ticket_seller.show_ticket_office()
    # print(ticket_list[1].getFee())

    # ticketOffice_1 = ticketOffice.TicketOffice(20000, ticket_list)
    # ticketSeller_1 = ticketSeller.TicketSeller(ticketOffice_1)
    # theater_1 = theater.Theater(ticketSeller_1)

    # bag_1 = bag.Bag(10000)
    # audience_1 = audience.Audience(bag_1)

    # # 관객 입장
    # theater_1.enter(audience_1)
