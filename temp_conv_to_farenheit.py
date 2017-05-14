import unittest


def to_fahrenheit(a_list):
    """
    Write a function that combines list comprehensions and lambdas
    to transform temperatures given in celsius to fahrenheit

    :param a_list:
    :return: list of fahrenheit temperatures

    Example:
    to_fahrenheit([0, 10, 25, 30, 100]) == [32.0, 50.0, 77.0, 86.0, 212.0]

    """

    return [(a * 1.8) + 32 for a in a_list]

class ToFahrenheitTestCase(unittest.TestCase):
    def test_to_fahrenheit(self):
        self.assertEqual(to_fahrenheit([0, 10, 25, 30, 100]),
                         [32.0, 50.0, 77.0, 86.0, 212.0])

    def test_to_fahrenheit_repeated_values(self):
        self.assertEqual(to_fahrenheit([0, 10, 10, 100]),
                         [32.0, 50.0, 50.0, 212.0])

    def test_to_fahrenheit_empty_list(self):
        self.assertEqual(to_fahrenheit([]), [])

unittest.main()

