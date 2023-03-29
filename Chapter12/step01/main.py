from lecture_ import Lecture
from grade_lecture_ import GradeLecture
from grade_ import Grade

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
    # print(lecture.average()) 오버로드 안됨.
    print(lecture.average("A"))
