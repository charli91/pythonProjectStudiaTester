# Zadanie 2:
# Utwórz klasę TemperatureConverter do konwersji temperatur między stopniami Celsjusza, Fahrenheita i Kelvina.
# Napisz testy jednostkowe.
#
# Kroki:
# Utwórz szkielet klasy:
# Metody: celsius_to_fahrenheit, fahrenheit_to_celsius, celsius_to_kelvin, kelvin_to_celsius, fahrenheit_to_kelvin,
# kelvin_to_fahrenheit.
# Napisz testy jednostkowe:
# Test dla konwersji temperatury z Celsjusza na Fahrenheita.
# Test dla konwersji temperatury z Fahrenheita na Celsjusza.
# Test dla konwersji temperatury z Celsjusza na Kelvina.
# Test dla konwersji temperatury z Kelvina na Celsjusza.
# Test dla konwersji temperatury z Fahrenheita na Kelvina.
# Test dla konwersji temperatury z Kelvina na Fahrenheita.
# Implementuj metody klasy:
# Uzupełnij metody konwersji temperatur w taki sposób, aby wszystkie testy przeszły pomyślnie.

class TempConverter:
    def celsius_to_fahrenheit(self, temperature_from):
        temperature_from: float
        fahrenheit: float = temperature_from * 9 / 5 + 32
        return fahrenheit
        pass

    def fahrenheit_to_celsius(self, temperature_from):
        pass

    def kelvin_to_celsius(self, temperature_from):
        pass

    def celsius_to_kelvin(self, temperature_from):
        pass

    def fahrenheit_to_kelvin(self, temperature_from):
        pass

    def kelvin_to_fahrenheit(self, temperature_from):
        pass
