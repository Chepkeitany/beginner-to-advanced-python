"""
Write a function `hello_world` which should return the string "Hello World".

Include test cases
"""

import unittest

# Function that returns a string "Hello World"
def hello_world():
    return "Hello World"

# Test cases
class FirstAssignmentTestCase(unittest.TestCase):
    def test_hello_world_function(self):
        "Should return the string 'Hello World'"
        self.assertEqual(hello_world(), "Hello World")

unittest.main()