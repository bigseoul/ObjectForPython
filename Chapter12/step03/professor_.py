from lecture_ import Lecture


class Professor:
    def __init__(self, name, lecture: Lecture) -> None:
        self.__name = name
        self.__lecture = lecture

    def compile_statistics(self, grade_name):
        """
        1. 메서드 인자에 Grade_name을 안넣을 경우
        -인터프리터 왈, GradeLecture.average() missing 1 required positional argument: 'grade_name'
        -self가 GradeLecture를 가리키고 있음.
        -Lecture.average()를 위해 self가 타고 올라가지 않음.
        -파이썬은 상속 오버로딩이던 같은 클래스 오버로딩이던 지원 안함.

        2. 인자와 _lecture.average(grade_name) 넣을 경우
        - mypy에서 에러 띄우나 실행은 됨.
        - Expected 0 positional

        3. 재밌는게 ,
        1)에 따르면 self참조는 GradeLecture를 가리키고 있다. 런타임이 에러 뱉음.
        2)에 따르면, Self가 Lecture를 가리키고 있는듯 보인다.
        이것은 mypy가 잘못 체킹했기 때문으로 보인다.
        인자를 넣고 실행하면 GradeLecture.average(grade_name)을 실행함.
        """
        string = "[{0}] {1}, {2:0.1f}".format(
            self.__name, self.__lecture.evaluate(), self.__lecture.average()
        )
        return string
