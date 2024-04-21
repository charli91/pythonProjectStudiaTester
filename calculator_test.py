import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    # kolejność wykonywania testów jest alfabetyczna, więc jeśli ma znaczenie kolejność
    # można dodać cyfry na początku np
    def test_1_add(self):
        self.assertEqual(self.calculator.addition(10, 20), 30)
        self.assertEqual(self.calculator.addition(10, -2), 8)
        self.assertEqual(self.calculator.addition(10, 0), 10)

    def test_2_subtract(self):
        self.assertEqual(self.calculator.subtraction(25, 10), 15)
        self.assertEqual(self.calculator.subtraction(-10, -20), 10)
        self.assertEqual(self.calculator.subtraction(24, -10), 34)
        self.assertEqual(self.calculator.subtraction(-5, 10), -15)

    def test_3_multiply(self):
        self.assertEqual(self.calculator.multiplication(4, 6), 24)
        self.assertEqual(self.calculator.multiplication(10, -2), -20)
        self.assertEqual(self.calculator.multiplication(10, 0), 0)
        self.assertEqual(self.calculator.multiplication(-3, -5), 15)

    def test_4_divide(self):
        self.assertEqual(self.calculator.division(30, 10), 3)
        self.assertEqual(self.calculator.division(-10, 2), -5)
        self.assertEqual(self.calculator.division(3, 2), 1.5)

    def test_5_divide_by_zero(self):
        self.assertEqual(self.calculator.division(10, 0), "Can't divide by 0")


if __name__ == '__main__':
    unittest.main()
