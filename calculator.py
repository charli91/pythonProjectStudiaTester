class Calculator:
    def addition(self, a, b):
        c = a + b
        return c

    def subtraction(self, a, b):
        c = a - b
        return c

    def multiplication(self, a, b):
        c = a * b
        return c

    def division(self, a, b):
        if b == 0:
            # return "Can't divide by zero"
            raise ValueError("Can't divide by 0")
        else:
            c = a / b
            return c


def main():
    print("Calculator")
    print("Choose your operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

    choice = int(input("Your choice (1/2/3/4): "))

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    calculator = Calculator()

    if choice == 1:
        result = calculator.addition(number1, number2)
        print("Your result: ", result)


# ten if powoduje wyłączenie uruchomienia tego pliku przy uruchamianiu plików, które mają go zaimportowanego
if __name__ == '__main__':
    main()
