from book import Book


# To change/ add / modify: show list of options with showing library (empty at first), adding new book without
# deleting previous, changing only some parameters (title, author, year)
def main():
    while True:
        # Defining if user needs library and if he read any book lately
        if_read_answer = str(input("This will be your new book library. Did you read any book lately? (y/n): "))
        if_read_answer = if_read_answer.lower()

        if if_read_answer == "n":
            print("That's sad. So I guess you won't need new library.")
            break
        # if he did read sth proposition to add to library
        elif if_read_answer == "y":
            # while, makes it possible to repeat adding
            while True:
                print("That's great. Let's add this book to library")
                number_of_books_to_add = int(input("How many books you want to add?: "))
                # part to be modified based on results get on training file test_tablicy
                for a in range(number_of_books_to_add):
                    library = []
                    new_book = Book(
                        title=input(f"What's the title of {a}this book?: "),
                        author=input("What's the author of this book?: "),
                        year=input("What's the year of this book?: ")
                    )
                    library.insert(new_book)
                    # show_library = new_book.get_info()
                # print(f"This is your library:\n{show_library}")
                print(f"This is your library:\n{library}")
                break

        # Condition for invalid answer for if_read_answer
        else:
            print("You were supposed to enter value y/n")


if __name__ == '__main__':
    main()
