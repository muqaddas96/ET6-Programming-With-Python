import unittest

from ..mystery_2 import mystery_2

class TestMystery2(unittest.TestCase):
    """ """

    def test_minimal_list_input(self):
        """Should count to 8"""
        self.assertEqual(mystery_2("Muqaddas"), 8)

    def test_minimal_string_input(self):
        """Should count to none"""
        self.assertEqual(mystery_2(""), None)

    def test_string(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            mystery_2(2)
