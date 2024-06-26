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
