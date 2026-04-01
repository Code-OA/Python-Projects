from storage import load_json
import books


def main ():
    library =  load_json()
    
    while True:
        print("Welcome to the Library!")

        print("Please select any of the below options")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search a Book")
        print("4. Borrow a Book")
        print("5.View Overdues")
        print("6. Return Book")
        print("\nType 'exit' to quit")

        user_input = input("Please type and enter any number shown in the above list\n")

        if user_input == "exit":
            exit()
        elif user_input == "1":
            books.add_book(library)
        elif user_input == "2":
            books.view_all(library)
        elif user_input == "3":
            books.search_book(library)
        elif user_input == "4":
            books.borrow_book(library)
        elif user_input == "5":
            books.view_overdues(library)
        elif user_input == "6":
            books.return_book(library)
        else:
            print("Please enter a valid command!")

if __name__ == "__main__":
    main()