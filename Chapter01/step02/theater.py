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

    step02
    수정된 영화관 클래스 어디서도 티켓오피스에 접근하지 않는다.
    영화관은 티켓오피스가 티켓셀러 내부에 있다는 사실을 모른다.
    영화관은 티켓셀러가 sellTo메시지를 이해하고 응답한다는 사실만 안다.

    영화관은 티켓셀러의 sellTo 인터페이스에만 의존.
    티켓셀러가 내부에 티켓오피스 인스턴스를 포함한고 있는 것은 구현 영역.
    """

    def __init__(self, ticket_seller: TicketSeller) -> None:
        self.__ticket_seller = ticket_seller

    # 1 단계: 영화관과 티켓오피스와 의존관계 끊기
    def enter(self, audience: Audience):
        self.__ticket_seller.sell_to(audience)
