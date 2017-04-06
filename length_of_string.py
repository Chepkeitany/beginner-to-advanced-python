import unittest

def length(a_string):
    """
    Define a function that computes the length of a given list or string
    You can't use the builtin len function, you must use a for loop.
    :param a_string: 
    :return length of a string
    """
    counter = 0
    for i in a_string:
        counter += 1
    return counter


class LengthTestCase(unittest.TestCase):
    def test_length_multiple_words(self):
        self.assertEqual(length('hello world'), 11)

    def test_length_single_word(self):
        self.assertEqual(length('hello'), 5)

    def test_length_empty_string(self):
        self.assertEqual(length(''), 0)

unittest.main()