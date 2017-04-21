import unittest

def truncate_chars(a_string, num_of_chars):
    """
    In the Django web framework, there's a helper called truncate_chars 
    that allows you to limit the length of a string to a given number of
    characters, and adds ... prefix at the end of it.
    You must write a Python function that
    mimics the same logic using String slicing.

    :param a_string
    :param num_of_chars
    :return: truncated string
    """
    # If a_string is not a string, raise value error
    if not isinstance(a_string, (str)):
        raise ValueError
    else:
        # Get the length of the string
        string_length = len(a_string)
        # If the number of chars to be truncated is greater than the length
        # of the string, return the string as is
        if num_of_chars > string_length:
            return a_string
        # Slice the string from index 0 to number of chars
        # And concatenate with the three dots: '...'
        else:
            return a_string[:num_of_chars] + '...'


class TruncateCharsTestCase(unittest.TestCase):

    def setUp(self):
        self.s = "This is a wonderful world!"

    def test_truncate_chars(self):
        self.assertEqual(truncate_chars(self.s, 4), "This...")

    def test_truncate_chars_no_chars(self):
        self.assertEqual(truncate_chars(self.s, 0), "...")

    def test_truncate_chars_limit_exceeded(self):
        self.assertEqual(truncate_chars(self.s, 100), self.s)

    def test_truncate_chars_invalid_value(self):
        with self.assertRaises(ValueError):
            truncate_chars(False, 100)
unittest.main()
