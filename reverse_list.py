import unittest

def reverse_list(a_list):
    """
    
    :param a_list: 
    :return: a reversed a_list
    """
    return a_list[::-1]

# Test cases
class ReverseListTestCase(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(reverse_list([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_reverse_list_with_empty_list(self):
        self.assertEqual(reverse_list([]), [])

unittest.main()