from datetime import datetime


class Invitation:

    # when is a Datetime type
    # __when = None  __ 더블언더스코어는 접근제한자 private

    def __init__(self, when: datetime) -> None:
        """when은 datetime 자료형"""
        self.__when = when
