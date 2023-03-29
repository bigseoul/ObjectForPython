  screening2 = Screening(the_book_of_fish2, 3, datetime(2023, 2, 18, 1, 00, 00))
    reservation2 = screening2.reserve(Customer("daegyung", 124), 2)
    reservation2.check_reservation()
