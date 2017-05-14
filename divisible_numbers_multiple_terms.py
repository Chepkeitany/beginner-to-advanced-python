import unittest


def divisible_by_term(number, a_terms):
    divisible_nums = [term for term in a_terms if number % term == 0]
    return len(divisible_nums) == len(a_terms)

def divisible_numbers(a_list, a_list_of_terms):
    """

    :param a_list:
    :param a_list_of_terms:
    :return: a list of terms divisible by a list of terms
    """
    return [number for number in a_list
            if divisible_by_term(number, a_list_of_terms)]

class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_numbers(self):
        self.assertEqual(set(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])),
                         set([6, 12]))

    def test_one_divisible_numbers(self):
        self.assertEqual(divisible_numbers([16, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3, 4]), [12])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], [5, 7]),  [])

    def test_both_empty_lists(self):
        self.assertEqual(divisible_numbers([], []),  [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], [5, 7]),  [])

unittest.main()
