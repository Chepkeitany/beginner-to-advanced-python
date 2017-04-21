import unittest


def camel_case(a_string):
    """Write a function that receives a string and returns
   a camel case version of it
   """
    # Use Python's built in title() method for strings
    return a_string.title()


class CamelCaseTestCase(unittest.TestCase):
    def test_word_with_spaces(self):
        self.assertEqual(camel_case("testing 123 hello"), 'Testing 123 Hello')

    def test_single_word(self):
        self.assertEqual(camel_case("testing"), 'Testing')

    def test_empty_string(self):
        self.assertEqual(camel_case(""), '')


unittest.main()
