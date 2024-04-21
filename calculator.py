from colors import Bcolors
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

    while True:
        print("Choose your operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Quit program")

        choice = int(input("Your choice (1/2/3/4/5): "))

        if choice == 5:
            print("Thank you for using calculator")
            # break przerywa działanie pętli while użytej na górze
            break

        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))

        calculator = Calculator()

        try:
            if choice == 1:
                result = calculator.addition(number1, number2)
                print("Your result: ", result)
            elif choice == 2:
                result = calculator.subtraction(number1, number2)
                print("Your result : ", result)
            elif choice == 3:
                result = calculator.multiplication(number1, number2)
                print("Your result : ", result)
            elif choice == 4:
                result = calculator.division(number1, number2)
                print("Your result : ", result)
            else:
                print("Invalid number provided")
        # ExceptionMessage: to może być dowolna nazwa zmiennej
        except Exception as ExceptionMessage:
            print(ExceptionMessage)


# ten if powoduje wyłączenie uruchomienia tego pliku przy uruchamianiu plików, które mają go zaimportowanego
if __name__ == '__main__':
    main()
