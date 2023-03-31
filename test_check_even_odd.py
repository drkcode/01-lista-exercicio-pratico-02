import unittest
from check_even_odd import check_even_odd, check_is_integer


class TestCheckEvenOdd(unittest.TestCase):
    def test_is_even(self):
        sut_1 = check_even_odd(2)
        self.assertEqual(sut_1, "PAR", "should return PAR if the input is equal to 2")
        sut_2 = check_even_odd(34)
        self.assertEqual(sut_2, "PAR", "should return PAR if the input is equal to 34")

    def test_is_odd(self):
        sut_1 = check_even_odd(3)
        self.assertEqual(
            sut_1, "IMPAR", "should return IMPAR if the input is equal to 3"
        )
        sut_2 = check_even_odd(55)
        self.assertEqual(
            sut_2, "IMPAR", "should return IMPAR if the input is equal to 55"
        )


class TestIsInteger(unittest.TestCase):
    def test_integer(self):
        sut_1 = check_is_integer(2)
        self.assertEqual(sut_1, 2, "should return 2 if the input is an integer")
        sut_2 = check_is_integer(100)
        self.assertEqual(sut_2, 100, "should return 100 if the input is an integer")

    def test_not_integer(self):
        sut_1 = check_is_integer(2.1)
        self.assertIsNone(sut_1, "should return None if the input is not an integer")
        sut_2 = check_is_integer(0.5)
        self.assertIsNone(sut_2, "should return None if the input is not an integer")
