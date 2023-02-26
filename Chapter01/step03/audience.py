from bag import Bag
from ticket import Ticket


class Audience:
    def __init__(self, bag: Bag) -> None:
        self.__bag = bag

    # Bag 자료형
    def get_bag(self):
        return self.__bag

    def buy(self, ticket: Ticket):
        return self.__bag.hold(ticket)
