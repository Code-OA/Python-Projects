from storage import load_json
import contact

def show_menu():
    contacts = load_json()

    while True:
        print("Welcome to contacts!")

        print("1. Add contact")
        print("2. View all")
        print("3. Search by name")
        print("4. Delete")
        print("Type 'exit' to quit")

        user_input = input("Choose any option to perform!\n")

        if user_input.lower() == "exit":
            exit()

        if user_input == "1":
            contact.add_contact(contacts)
        elif user_input == "2":
            contact.view_all(contacts)
        elif user_input == "3":
            contact.search_contact(contacts)
        elif user_input == "4":
            contact.delete_contact(contacts)
        else:
            print("No action found!")


if __name__ == "__main__":
    show_menu()