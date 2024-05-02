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
    def __init__(self, balance, account_number):
        self.balance = balance
        self.accountNumber = account_number

    def deposit(self, payment_transfer_value):
        final_balance = self.balance + payment_transfer_value
        return final_balance

    def withdraw(self, payment_transfer_value):
        if payment_transfer_value > self.balance:
            raise Exception("There is no enough money on your account")
        else:
            final_balance = self.balance - payment_transfer_value
            return final_balance

    def get_balance(self):
        return f'Balance: {self.balance} PLN, IBAN: {self.accountNumber}'