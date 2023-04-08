import unittest
from check_even_odd import is_even, is_integer


class TestCheckEvenOdd(unittest.TestCase):
    def test_is_even(self):
        sut_1 = is_even(2)
        self.assertTrue(sut_1, "should return true if the input is equal to 2")
        sut_2 = is_even(34)
        self.assertTrue(sut_2, "should return true if the input is equal to 34")

    def test_not_even(self):
        sut_1 = is_even(3)
        self.assertFalse(sut_1, "should return false if the input is equal to 3")
        sut_2 = is_even(55)
        self.assertFalse(sut_2, "should return false if the input is equal to 55")


class TestIsInteger(unittest.TestCase):
    def test_integer(self):
        sut_1 = is_integer(2)
        self.assertTrue(sut_1, "should return 2 if the input is an integer")
        sut_2 = is_integer(100)
        self.assertTrue(sut_2, "should return 100 if the input is an integer")

    def test_not_integer(self):
        sut_1 = is_integer(2.1)
        self.assertFalse(sut_1, "should return None if the input is not an integer")
        sut_2 = is_integer(0.5)
        self.assertFalse(sut_2, "should return None if the input is not an integer")
