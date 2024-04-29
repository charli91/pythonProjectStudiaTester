from TemperatureConverter import TempConverter
import unittest

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.temperature = Temperature(31)

    def test_1_celsius_to_fahrenheit(self):
        self.assertEqual(self.TempConverter.celsius_to_fahrenheit(temperature=32), 89.6)
        self.assertEqual(self.TempConverter.celsius_to_fahrenheit(temperaturet= -19), -2.2)

    def test_2_fahrenheit_to_celsius(self):
        pass

    def test_3_celsius_to_kelvin(self):
        pass

    def test4_kelvin_to_celsius(self):
        pass

    def test_5_fahreinheit_to_kelvin(self):
        pass

    def test_6_kelvin_to_fahrenheit(self):
        pass


if __name__ == '__main__':
    unittest.main()