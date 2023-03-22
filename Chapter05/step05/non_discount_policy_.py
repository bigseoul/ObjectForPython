from discount_policy_ import DiscountPolicy
from money_ import Money


class NoneDiscountPolicy(DiscountPolicy):
    # override
    def _get_discount_amount(self, screening) -> Money:
        return Money.from_wons(0)
