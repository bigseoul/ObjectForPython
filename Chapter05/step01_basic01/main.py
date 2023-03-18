from movie_ import Movie
from screening_ import Screening


def main():
    the_batman = Movie("the batman", 18000, 10000, "DC_Amount")
    screening = Screening(the_batman, 1)

    print("1. 예매하라")
    reservation = screening.reserve("Steve", 2)
    print(reservation)


if __name__ == "__main__":
    main()
