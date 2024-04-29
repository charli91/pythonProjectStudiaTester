# Zadanie 1:
# Utwórz klasę Account do zarządzania kontem bankowym z operacjami wpłaty i wypłaty. Napisz testy jednostkowe.
#
# Kroki:
# Utwórz szkielet klasy:
# Metody: __init__, deposit, withdraw, get_balance.
# Napisz testy jednostkowe:
# Test dla inicjalizacji konta z określoną kwotą początkową.
# Test dla wpłaty środków na konto.
# Test dla wypłaty środków z konta.
# Test dla próby wypłaty więcej środków niż jest dostępnych (powinien wyrzucić błąd).
# Implementuj metody klasy:
# Uzupełnij metody klasy, aby wszystkie testy przeszły pomyślnie.

class Account:
    def __init__(self, balance, accountNumber):
        self.balance = balance
        self.accountNumber = accountNumber

    def deposit(self, PaymentTransferValue):
        finalBalance = self.balance + PaymentTransferValue
        return finalBalance

    def withdraw(self, PaymentTransferValue):
        if PaymentTransferValue > self.balance:
            raise Exception("There is no enough money on your account")
        else:
            finalBalance = self.balance - PaymentTransferValue
            return finalBalance

    def get_balance(self):
        return f'Balance: {self.balance} PLN, IBAN: {self.accountNumber}'

