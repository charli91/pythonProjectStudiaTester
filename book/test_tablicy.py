# tablica = []
# for a in range(3):
#     name_of_variable = input("What is your name? ")
#     name_of_variable2 = input("What is your last name? ")
#     tablica.insert(a, name_of_variable)
#
# for a in range(3):
#     print(tablica[a])
from book import Book

number_of_books_to_add = int(input("How many books you want to add?: "))
library = []

# trzeba by stworzyć tablicę tablic?
for a in range(number_of_books_to_add):
    new_book = Book(
        title=input(f"What's the title of {a+1} book?: "),
        author=input(f"What's the author of {a+1} book?: "),
        year=input(f"What's the year of {a+1} book?: ")
    )
    library.insert(a-1, new_book)

print(library)
#
# for a in range(number_of_books_to_add):
#     library[a-1] = Book()
#     print(library[a-1].get_info())
