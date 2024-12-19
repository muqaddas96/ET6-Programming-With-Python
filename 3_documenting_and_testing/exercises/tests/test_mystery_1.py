import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """ """

    def test_minimal_input(self):
        """"""
        self.assertEqual(mystery_1(0, 0), 0)

    def test_0(self):
        """It should evaluate 3"""
        self.assertEqual(mystery_1(1,2), 3)

    def test_1(self):
        """It should evaluate -8]"""
        self.assertEqual(mystery_1(-5, -3), -8)

    def test_integer(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_1("a", "b")
