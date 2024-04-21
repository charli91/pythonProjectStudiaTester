from colors import Bcolors

# Defining methods used in Calculator
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
        # printing instructions for user
        print(f"Choose your operation:\n"
              f"{Bcolors.OKBLUE}1.Addition\n"
              f"{Bcolors.OKCYAN}2.Subtraction\n"
              f"{Bcolors.OKGREEN}3.Multiplication\n"
              f"{Bcolors.FAIL}4.Division\n{Bcolors.ENDC}"
              f"{Bcolors.BOLD}5.Quit program{Bcolors.ENDC}")

        # User is choosing one option at the time for doing operation
        choice = int(input(f"Your choice ({Bcolors.OKBLUE}1{Bcolors.ENDC}/"
                           f"{Bcolors.OKCYAN}2{Bcolors.ENDC}/"
                           f"{Bcolors.OKGREEN}3{Bcolors.ENDC}/"
                           f"{Bcolors.FAIL}4{Bcolors.ENDC}/"
                           f"{Bcolors.BOLD}5{Bcolors.ENDC}): "))

        # Quiting program as it is in instructions
        if choice == 5:
            print(f"{Bcolors.HEADER}Thank you for using calculator{Bcolors.ENDC}")
            # break przerywa działanie pętli while użytej na górze
            break

        # Defining numbers for operation that user chose
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
        # as e: to może być dowolna nazwa zmiennej
        except Exception as exceptionMessage:
            print(exceptionMessage)


# ten if powoduje wyłączenie uruchomienia tego pliku przy uruchamianiu plików, które mają go zaimportowanego
if __name__ == '__main__':
    main()
