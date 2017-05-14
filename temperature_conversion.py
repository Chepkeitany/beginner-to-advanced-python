import unittest


def to_fahrenheit(temp_value):
    return (temp_value * 1.8) + 32


def to_celsius(temp_value):
    return (temp_value - 32) / 1.8


def convert_temperature(temp_value, to='celsius'):
    """
    Write a function convert_temperature that receives two parameters,
    a number (indicating degrees of temperature) and an optional
    second parameter indicating if it should convert the temperature to Celsius
    or Fahrenheit (default is Celsius).
    The function should have two inner functions to_celsius and to_fahrenheit
    that receive NO parameters and must be used to return the expected result.

    :param temp_value:
    :param to:
    :return: converted temperature
    """
    if to == 'celsius':
        return to_celsius(temp_value)
    else:
        return to_fahrenheit(temp_value)


class ConvertTemperatureTestCase(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert_temperature(32, to='celsius'), 0)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert_temperature(40, to='fahrenheit'), 104)

    def test_default_parameter_is_celsius(self):
        self.assertEqual(convert_temperature(32), 0)


unittest.main()
