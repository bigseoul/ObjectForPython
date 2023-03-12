from typing import List


class Test:
    def __init__(self, *args: int) -> None:
        self.args = args

    def __str__(self) -> str:
        return f"Test({', '.join(str(arg) for arg in self.args)})"


test = Test(1, 2, 3)

print(test)
