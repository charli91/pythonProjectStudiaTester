def addition(a, b):
    c = a + b
    return c


def addition2(a, b):
    return a + b


resultOfAddition = addition(10, 20)
print('addition', resultOfAddition)

print('addition2: ', addition2(10, 20))


def subtraction(a, b):
    return a - b


print('subtraction: ', subtraction(10, 20))


def multiplication(a, b):
    return a * b


print('multiplication:', multiplication(10, 20))


def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Can't divide by zero")


print('division: ', division(10, 20))
