import unittest

def sum_multiple_terms(*args):
    """
    Write a function that receives multiple arguments
    and returns the sum of them.
    :param args:
    :return:
    """

    if len(args) == 0:
        raise AttributeError
    else:
       return sum(args)

class MultipleSumTestCase(unittest.TestCase):

    def test_sum_multiple_terms(self):
        self.assertEqual(sum_multiple_terms(2, 3), 5)
        self.assertEqual(sum_multiple_terms(2, 3, 5, 7), 17)

    def test_sum_with_no_elements_raises_error(self):
        with self.assertRaises(AttributeError):
            sum_multiple_terms()

unittest.main()
