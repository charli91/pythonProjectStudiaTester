from TemperatureConverter import TempConverter
import unittest


class TestTempConverter(unittest.TestCase):
    def setUp(self):
        self.temperature = TempConverter()

    def test_1_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(self.temperature.celsius_to_fahrenheit(32), 89.6)
        self.assertAlmostEqual(self.temperature.celsius_to_fahrenheit(-19), -2.2)

    def test_2_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(self.temperature.fahrenheit_to_celsius(-2.2), -19)

    def test_3_celsius_to_kelvin(self):
        self.assertAlmostEqual(self.temperature.celsius_to_kelvin(-273), 0)

    def test_4_kelvin_to_celsius(self):
        self.assertAlmostEqual(self.temperature.kelvin_to_celsius(0), -273)

    def test_5_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(self.temperature.fahrenheit_to_kelvin(int(0)), 0)

    def test_6_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(self.temperature.kelvin_to_fahrenheit(0), 0)


if __name__ == '__main__':
    unittest.main()
