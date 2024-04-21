import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()


    # kolejność wykonywania testów jest alfabetyczna, więc jeśli ma znaczenie kolejność
    # można dodać cyfry na początku np
    def test_add(self):
        self.assertEqual(self.calculator.add(10, 20), 30)

if __name__ == '__main__':
    unittest.main()