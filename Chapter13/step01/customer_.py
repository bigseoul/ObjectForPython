class Customer:
    def __init__(self, name: str, id: int) -> None:
        self.__name = name
        self.__id = id

    def check_customer(self):
        print("===customer===")
        print(self.__name, self.__id)
