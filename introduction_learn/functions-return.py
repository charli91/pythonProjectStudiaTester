def addition(a, b):
    c = a + b
    return c


def addition2(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Can't divide by zero"


first_number = int(input("Tell me your first number: "))
second_number = int(input("Tell me your second number: "))

resultOfAddition = addition(first_number, second_number)

print('addition: ', resultOfAddition)
print('addition2: ', addition2(first_number, second_number))
print('subtraction: ', subtraction(first_number, second_number))
print('multiplication:', multiplication(first_number, second_number))
print('division: ', division(first_number, second_number))
