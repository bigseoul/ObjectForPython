import calendar

"""
https://stackoverflow.com/questions/38629754/python-datetime-weekday-number-code-dynamically

 zip 함수는 동일한 개수로 이루어진 자료형들을 1개로 묶어 준다. 
 zip 함수의 입력 매개변수는 iterable이어야 한다.
"""
# DAY_OF_WEEKS = dict(zip(calendar.day_name, range(7)))
# DAY_OF_WEEK.get("Monday") -> 0 of integer

"""
enumerate(calendar.day_name)는 인덱스와 요일명을 반환.
day를 키로, num을 키로 해서 딕셔너리를 만듦.
"""

DAY_OF_WEEKS = {day: num for num, day in enumerate(calendar.day_name)}
