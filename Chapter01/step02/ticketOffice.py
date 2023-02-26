class TicketOffice:
    def __init__(self, amount, ticket_list: list) -> None:
        self.__amount = amount
        self.__ticket_list = ticket_list

    # 생성한 티켓을 윗장부터 없앰.
    def get_ticket(self):
        a_ticket_sold = self.__ticket_list[0]
        del self.__ticket_list[0]
        return a_ticket_sold

    def minus_amout(self, amount):
        self.__amount -= amount

    def plus_amount(self, amount):
        self.__amount += amount
        print("office amount is: ", self.__amount)
