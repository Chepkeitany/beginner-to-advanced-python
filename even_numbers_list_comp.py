import unittest

def even_numbers(a_list):
    """
    Write a function that receives a list of numbers
    and returns only the even elements using List comprehensions.

    :param a_list:
    :return: a_list of even numbers
    """
    return [i for i in a_list if i % 2 == 0]

class EvenNumberTestCase(unittest.TestCase):
    def test_multiple_even_numbers(self):
        self.assertEqual(even_numbers([5, 4, 3, 2, 1]), [4, 2])

    def test_one_even_numbers(self):
        self.assertEqual(even_numbers([5, 4, 3, 7, 9, 1]), [4])

    def test_no_even_numbers(self):
        self.assertEqual(even_numbers([5, 3, 7, 9, 1]), [])

    def test_empty_list_even_numbers(self):
        self.assertEqual(even_numbers([]), [])

unittest.main()
