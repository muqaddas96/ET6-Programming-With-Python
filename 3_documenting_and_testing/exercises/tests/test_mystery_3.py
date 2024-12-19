import unittest

from ..mystery_3 import mystery_3

class TestMystery3(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """It should return 0"""
        self.assertEqual(mystery_3(0, 0), 0)

    def test_0(self):
        """It should evaluate 1"""
        self.assertEqual(mystery_3(1,2), 1)

    def test_1(self):
        """It should evaluate -5]"""
        self.assertEqual(mystery_3(-5, -3), -5)

    def test_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_3("a", "b")
