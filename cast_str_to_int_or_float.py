import unittest


def string2number(a_string):
    """
    Write a function string2number(a_string), that converts given String into
    either an Integer or a Float depending on which of them is possible.
    
    :param a_string: 
    :return: an int or float or raise Exception
    """
    # Check if the param passed is not string

    if not isinstance(a_string, (str)):
        raise ValueError

    # Check that the string contains the dot operator
    # in order to determine whether it is an int or float
    # Convert to a float or raise a ValueError
    elif '.' in a_string:
        try:
            num = float(a_string)
        except:
            raise ValueError

    # Convert to an int or raise ValueError
    else:
        try:
            num = int(a_string)
        except:
            raise ValueError

    return num


class String2NumberTestCase(unittest.TestCase):
    def test_cast_string_into_integer(self):
        self.assertEqual(string2number('2'), 2)

    def test_cast_string_into_float(self):
        self.assertEqual(string2number('2.8'), 2.8)

    def test_cast_invalid_string_value(self):
        with self.assertRaises(ValueError):
            string2number('invalid-value')

    def test_cast_invalid_data_type(self):
        with self.assertRaises(ValueError):
            string2number(True)


unittest.main()