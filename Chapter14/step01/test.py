from datetime import datetime, time, timedelta, date

td1 = timedelta(seconds=10)
td2 = timedelta(seconds=20)
date1 = datetime(2023, 1, 28, 10, 00, 00)

print(date1 + td2)
