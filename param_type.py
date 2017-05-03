import unittest


def what_is_this(param):
    """
    
    Write a function that receives one single param,
    and returns a String explaining which type of object the param is.
    If given param is not instance of any of the basic data types,
    say you don't know what it is.
    
    :param param: 
    :return: string describing type of param
    
    NB: isinstance(bool, int) is True i.e isinstance(True, int) is True,
    ensure you evaluate for bool before evaluating for integer
    """
    if (isinstance(param, bool)):
        return "This is a Boolean."
    if (isinstance(param, int)):
        return "This is an Integer."
    elif (isinstance(param, str)):
        return "This is a String."
    else:
        return "I have no idea what this is"


class WhatIsThisTestCase(unittest.TestCase):

    def test_what_is_this_integer(self):
        self.assertEqual(what_is_this(10), "This is an Integer.")

    def test_what_is_this_string(self):
        self.assertEqual(what_is_this("Hello"), "This is a String.")

    def test_what_is_this_boolean(self):
        self.assertEqual(what_is_this(True), "This is a Boolean.")

    def test_what_is_this_float(self):
        self.assertEqual(what_is_this(10.92), "This is a Float.")

    def test_what_is_this_float(self):
        self.assertEqual(what_is_this(object()), "I have no idea what this is")

unittest.main()