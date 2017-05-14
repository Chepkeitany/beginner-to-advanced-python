import unittest

def divisible_numbers(a_list, term):
    """

    :param a_list:
    :param term:
    :return: a list of numbers divisible by term
    """
    return [i for i in a_list if i % term == 0]

class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_number(self):
        self.assertEqual(
            divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), [9, 6, 3])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], 2), [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], 5), [])

unittest.main()
