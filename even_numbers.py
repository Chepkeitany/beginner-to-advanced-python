import unittest


def even_numbers(list_of_numbers, limit):
    """
    Write a function that receives a list of Integer values as a param,
    and returns a filtered list containing only even numbers.
    A second Integer param is given to be used
    as limit for the returned list of numbers.

    :param list_of_numbers:
    :param limit:
    :return: a limited number of even numbers

    Note: List comprehensions must not be used.
    Only loops and their related statements are allowed.
    """

    even_numbers_list = []

    if limit > 0:
        for i in list_of_numbers:
            if i % 2 == 0:
                even_numbers_list.append(i)
        return even_numbers_list[0:limit]
    else:
        return []


class EvenNumbersTestCase(unittest.TestCase):

    def test_even_numbers(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 3), [2,4,6])

    def test_even_numbers_limit_exceeded(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 30),
                         [2,4,6,8,10])

    def test_even_numbers_limit_zero(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 0), [])

    def test_even_numbers_limit_one(self):
        self.assertEqual(even_numbers([1,2,3,4,5,6,7,8,9,10], 1), [2])

unittest.main()
