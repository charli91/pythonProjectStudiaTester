class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9 / 5 + 32
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit + 459.67) * 5 / 9
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return kelvin * 9 / 5 - 459.67


    # static method: uruchomienie metody bez tworzenia obiektu