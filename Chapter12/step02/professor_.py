from lecture_ import Lecture


class Professor:
    def __init__(self, name, lecture: Lecture) -> None:
        self.__name = name
        self.__lecture = lecture

    def compile_statistics(self, grade_name):
        """
        1. 메서드 인자에 Grade_name을 안넣을 경우
        -런타임 인터프리터 왈, GradeLecture.average() missing 1 required positional argument: 'grade_name'
        -self가 GradeLecture를 가리키고 있음.
        -Lecture.average()를 위해 self가 타고 올라가지 않음.
        -파이썬은 상속 오버로딩이던 같은 클래스 오버로딩이던 지원 안함.

        2. 인자와 _lecture.average(grade_name) 넣을 경우
        - mypy에서 에러 띄우나 실행은 됨.
        - mypy는 정적타입 검사기이기 때문에 타입힌트를 기준해 판단.
        - Expected 0 positional

        """
        string = "[{0}] {1}, {2:0.1f}".format(
            self.__name, self.__lecture.evaluate(), self.__lecture.average(grade_name)
        )
        return string
