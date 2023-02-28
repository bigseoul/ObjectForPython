from bag_ import Bag


class Audience:
    """
    관램객은 소지품을 보관하기 위해 가방을 가질 수 있다
    """

    def __init__(self, bag: Bag) -> None:
        self.__bag = bag

    def get_bag(self) -> Bag:
        """외부에서 직접 가방에 접근할 수 있음. 노캡슐화"""
        return self.__bag
