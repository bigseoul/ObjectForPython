import calendar

"""https://stackoverflow.com/questions/38629754/python-datetime-weekday-number-code-dynamically"""
# DAY_OF_WEEKS = dict(zip(calendar.day_name, range(7)))
# DAY_OF_WEEK.get("Monday") -> 0 of integer

"""
이 코드는 파이썬에서 작성된 코드로, DAY_OF_WEEKS라는 딕셔너리를 생성하고 있습니다. 
이 딕셔너리는 키로 요일의 이름을 사용하고 값으로 요일에 해당하는 숫자를 사용합니다. 
코드는 calendar 모듈의 day_name을 사용하여 요일의 이름과 해당 인덱스를 가져옵니다.

여기 코드의 각 부분에 대한 설명입니다:

DAY_OF_WEEKS: 요일 이름을 키로, 요일에 해당하는 숫자를 값으로 하는 딕셔너리를 생성하는 변수입니다.

{day: num for num, day in enumerate(calendar.day_name)}: 이 부분은 딕셔너리 컴프리헨션(Dictionary Comprehension)이라고 불리는 구문입니다. 
이 구문을 사용하여 딕셔너리를 간결하게 생성할 수 있습니다.

enumerate(calendar.day_name): enumerate() 함수는 입력받은 iterable 객체(여기서는 calendar.day_name)의 각 요소와 해당 요소의 인덱스를 반환합니다. 
이 경우, calendar.day_name은 요일의 이름 목록을 포함하고 있습니다.

day: calendar.day_name에서 가져온 요일 이름입니다.

num: enumerate() 함수를 사용하여 얻은 요일에 해당하는 인덱스(숫자)입니다.

결과적으로, 이 코드는 요일의 이름과 해당하는 숫자를 매핑한 딕셔너리를 생성합니다. 예를 들어, 딕셔너리는 다음과 같이 표현될 수 있습니다.
"""

DAY_OF_WEEKS = {day: num for num, day in enumerate(calendar.day_name)}
