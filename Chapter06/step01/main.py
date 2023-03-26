from constant_ import DAY_OF_WEEK
from datetime import datetime, time
from recurring_schedule_ import RecurringSchedule
from event_ import Event

if __name__ == "__main__":

    schedule = RecurringSchedule(
        "meeting", DAY_OF_WEEK.get("Wednesday"), time(10, 30), time(0, 30)
    )

    """월요일 0 14일이 수요일"""
    event = Event("meeting", datetime(2022, 12, 15, 10, 30, 0), time(1, 30))
    event.is_satisfied(schedule)
    event.is_satisfied(schedule)
