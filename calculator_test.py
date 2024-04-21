import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()


    # kolejność wykonywania testów jest alfabetyczna, więc jeśli ma znaczenie kolejność
    # można dodać cyfry na początku np
    def test_1_add(self):
        self.assertEqual(self.calculator.addition(10, 20), 30)


    def test_2_subtract(self):
        self.assertEqual(self.calculator.subtraction(25, 10), 15)


    def test_3_multiply(self):
        self.assertEqual(self.calculator.multiplication(4, 6), 24)


    def test_4_divide(self):
        self.assertEqual(self.calculator.division(30, 10), 3)

if __name__ == '__main__':
    unittest.main()