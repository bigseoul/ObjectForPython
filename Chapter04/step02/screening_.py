from datetime import datetime

from money_ import Money
from movie_ import Movie
from movie_type_ import MovieType


# This is a class definition for Screening
class Screening:
    """
    무비가 금액 할인 정책이나 비율 할인 정책을 지원할 경우, 무비의 is_discountable()메서드를
    호출해서 할인이 가능하지 여부를 판단한 뒤, 적절한 무비의 메서드를 호출해 요금을 계산한 다.
    할인이 불가능하거나 할인 정책이 적용되지 않은 영화는 calculate_none_discounted_fee()호출해서 계산

    # 자바처럼 디폴트 생성자를 만들어주지 않으니, 만드는데
    # None으로 해도 되나?
    # https://gongmeda.tistory.com/12

    DiscountCondition이 할인 여부를 판단하는데 필요한 정보가 변경되면,
    Movie의 isDiscountable 메서드로 전달되는 인자의 종류를 변경해야 하고,
    이로 인해 Screening에서 Movie.isDiscountable()을 호출할때 넘기는 인자도 바뀌게 된다.
    DiscountCondition에 새롭게 나이할인 추가
    => Movie.isDiscountable 메서드 인자로 나이를 추가
    => Movie를 사용하는 Screening의 isDiscountable 메서드의 인자로 나이 추가

    하나의 변경을 수용하기 위해 여러 곳을 동시에 변경해야 한다면 설계의 응집도가 낮다는 증거이다.
    """

    # Constructor for Screening class which takes movie, sequence and when_screened as input parameters
    def __init__(self, movie: Movie, sequence: int, when_screened: datetime) -> None:
        # Private instance variable __movie which stores the movie object
        self.__movie = movie
        # Private instance variable __sequence which stores the sequence number
        self.__sequence = sequence
        # Private instance variable __when_screened which stores the datetime object for when the screening is scheduled
        self.__when_screened = when_screened

    # Method to return the string representation of the Screening object
    def __str__(self) -> str:
        return f"{self.__movie}, {self.__sequence}, {self.__when_screened}"

    # Method to calculate the fee for the screening based on the audience count
    def calculate_fee(self, audience_count: int) -> Money:  # type: ignore
        # Get the movie type from the movie object
        movie_type = self.__movie.get_movie_type()
        # If the movie type is AMOUNT_DISCOUNT
        if movie_type == MovieType.AMOUNT_DISCOUNT:
            # Check if the movie is discountable for the given screening time and sequence
            if self.__movie.is_discountable(self.__when_screened, self.__sequence):
                # Calculate the amount discounted fee and return the total fee for the audience count
                return self.__movie.calculate_amount_discounted_fee() * audience_count
        # If the movie type is PERCENT_DISCOUNT
        elif movie_type == MovieType.PERCENT_DISCOUNT:
            # Calculate the percent discounted fee and return the total fee for the audience count
            return self.__movie.calculate_percent_discounted_fee() * audience_count
        # If the movie type is NONE_DISCOUNT
        else:
            # Calculate the none discounted fee and return the total fee for the audience count
            return self.__movie.calculate_none_discounted_fee() * audience_count
