from datetime import datetime

date1 = datetime(2022, 8, 27, 11, 50, 00)
date2 = datetime(2022, 8, 27, 12, 50, 00)

assert date1 < datetime.now()
