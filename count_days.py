import unittest
from datetime import date


def count_days(d1, d2):
    """
    Write a function that receives two date objects,
    and returns the amount of days that have past from one date to the other.
    The second date should be either greater or equal to the first date passed.
    If the second date is smaller than the first one, a ValueError should be raised.
    """
    if d1 > d2:
        raise ValueError
    else:
        return abs((d2 - d1).days)


class CountDaysTestCase(unittest.TestCase):
    def test_count_days_year(self):
        days = count_days(date(2015, 1, 1),
                          date(2016, 1, 1))
        self.assertEqual(days, 365)

    def test_count_days_month(self):
        days = count_days(date(2016, 1, 1),
                          date(2016, 2, 1))
        self.assertEqual(days, 31)

    def test_count_days_one_day(self):
        days = count_days(date(2016, 2, 1),
                          date(2016, 2, 2))
        self.assertEqual(days, 1)

    def test_count_days_no_difference(self):
        days = count_days(date(2016, 1, 1),
                          date(2016, 1, 1))
        self.assertEqual(days, 0)

    def test_count_days_invalid_order(self):
        with self.assertRaises(ValueError):
            days = count_days(date(2016, 1, 1),
                              date(2015, 1, 1))


unittest.main()