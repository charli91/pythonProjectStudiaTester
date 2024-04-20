def hello(name): #zmienna lokalna - tylko w tej funkcji
    print(f"Hello {name}")

name = input("What is your name? ") #zmienna globalna
hello(name)

def task_instruction(time_left):
    if time_left == 'whole week':
        print("Well, you will make it")
    elif time_left == 'whole day':
        print("Well, you will have to hurry up")
    elif time_left == 'not enough':
        print("Sorry, you will probably fail")
    else:
        print("You were supposed to tell me how much time do you have!")
        # rekurencja - wywołanie funkcji przez samą siebie
        task_instruction(input("How much time do you have? (whole week/whole day/not enough): "))

task_instruction(input("How much time do you have? (whole week/whole day/not enough): "))