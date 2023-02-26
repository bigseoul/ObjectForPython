"""모듈명과 객체 변수의 이름이 같으면 안됨. 이건 연습이니 지나간다 ㅋ"""
from datetime import datetime

from audience import Audience
from bag import Bag
from invitation import Invitation
from theater import Theater
from ticket import Ticket
from ticketOffice import TicketOffice
from ticketSeller import TicketSeller

if __name__ == "__main__":

    # """티켓 2장 만들기, 자바의 배열을 파이썬의 리스트 등으로 이해해야"""
    ticket_list = list()  # = []
    for i in range(2):
        ticket_list.append(Ticket())

    # """티켓셀러 -> 티켓 오피스 -> 티켓(위에서 만든)"""
    ticket_seller = TicketSeller(TicketOffice(1000000, ticket_list))

    """No invitation Case"""
    jisoo = Audience(Bag(20000, None))  # type: ignore

    """Invitation Case"""
    jennie = Audience(Bag(0, Invitation(datetime(2022, 12, 8))))

    """극장1 객체 생성"""
    theater1 = Theater(ticket_seller)

    """극장1 객체에 관객 객체 인자로 전달"""
    theater1.enter(jisoo)  # ticket
    theater1.enter(jennie)  # invitation
