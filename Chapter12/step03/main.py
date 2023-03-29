from lecture_ import Lecture
from grade_lecture_ import GradeLecture
from grade_ import Grade
from professor_ import Professor

if __name__ == "__main__":
    lecture = GradeLecture(
        "객체지향 프로그래밍",
        70,
        [
            Grade("A", 100, 95),
            Grade("B", 94, 80),
            Grade("C", 79, 70),
            Grade("D", 69, 50),
            Grade("F", 49, 0),
        ],
        [81, 95, 97, 50, 45],
    )

    """
    결과// Title: 객체지향 프로그래밍, Evaluation Method: Grade
    Lecture의 get_evaluation_method()가 아닌
    GradeLecture의 get_evaluation_method()가 실행
    메시지 탐색이 GradeLecture부터 다시 시작
    """
    #
    #
    print(lecture.stats())
