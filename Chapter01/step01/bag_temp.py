class Bag:
    def __init__(self, amount, invitation=None) -> None:
        self.__amount = amount
        if invitation == None:
            self.__invitation = None
        else:
            self.__invitation = invitation
