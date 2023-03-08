from datetime import datetime


class Screening:

    # 자바처럼 디폴트 생성자를 만들어주지 않으니, 만드는데
    # None으로 해도 되나?
    # https://gongmeda.tistory.com/12

    def __init__(self) -> None:
        self.__movie = None
        self.__sequence = None
        self.__when_screened: "datetime"

    @property
    def movie(self):
        return self.__movie

    @movie.setter
    def movie(self, movie):
        self.__movie = movie

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, sequence):
        self.__sequence = sequence

    @property
    def when_screened(self) -> datetime:
        return self.__when_screend

    @when_screened.setter
    def when_screened(self, when_screend):
        self.__when_screend = when_screend
