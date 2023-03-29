from datetime import date, datetime, time, timedelta

date1 = datetime(2023, 1, 19, 1, 10, 00)
date2 = datetime.combine(date.today(), datetime.max.time())
date3 = date1.max
cmp_time = time(5, 59)
# _time = datetime.combine(date1, time.min) + timedelta(days=1)
closed_time = time(23, 59)
open_time = time(6, 00)

# if cmp_time < from_time and cmp_time > to_time:
#     print("종료시간 이전")
# else:
#     print("종료시간")

assert cmp_time <= closed_time and cmp_time >= open_time, "영업시간 종료"
