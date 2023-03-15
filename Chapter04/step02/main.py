from datetime import datetime, time
from constant_ import DAY_OF_WEEKS
from customer_ import Customer
from discount_condition_ import DiscountCondition
from money_ import Money
from movie_ import Movie
from reservation_agency_ import ReservationAgency
from screening_ import Screening

def main():
    discount_condition = DiscountCondition.from_DC_for_peried(
        DAY_OF_WEEKS.get("Friday"),
        datetime(2023, 3, 17, 0, 0, 0),
        datetime(2023, 3, 17, 23, 59, 59),
    )
    base_price = Money.from_wons(10000)
    discount_price = Money.from_wons(1000)
    movie = Movie.from_movie_for_discount_amount(
        "Free guy",
        time(hour=1, minute=55),
        base_price,
        discount_price,
        discount_condition,
    )
    screening = Screening(movie, 1, datetime(2023, 3, 17, 18, 00, 00))
    agency = ReservationAgency()
    reservation = agency.reserve(screening, Customer("bigseoul", 1), 2)
    print(reservation)

if __name__ == "__main__":
    main()
