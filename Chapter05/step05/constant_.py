import calendar

"""https://stackoverflow.com/questions/38629754/python-datetime-weekday-number-code-dynamically"""
DAY_OF_WEEK = dict(zip(calendar.day_name, range(7)))
# DAY_OF_WEEK.get("Monday") -> 0 of integer
