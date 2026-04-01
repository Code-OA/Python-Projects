from storage import write_json
from datetime import datetime , timedelta

# helper function
def alert_for_not ():
    print("\nNo books are added to the library\n")

def print_book(index ,  book):
    print("")
    print(f'{index}:-')
    print(f"Title : {book["title"]}")
    print(f"Author : {book["author"]}")
    print(f"Genre : {book["genre"]}")
    if book["due_date"]:
        print(f"Due Date : {book["due_date"]}")
    if book["date_of_borrow"]:
        print(f"Borrow Date : {book["date_of_borrow"]}")
    if book["is_available"]:
        print("Available : Yes")
    else:
        print("Available : No")
    print(f"Added Date : {book["added_date"]}")
    print("")

# main functions
def add_book(library):
    while True:
        title = input("Please enter the book name\n")
        if title:
            break

    while True:
        author = input("Please enter author name\n")
        if author:
            break

    while True:
        genre = input("Please enter the genre of the book\n")
        if genre:
            break

    library.append({
        "title":title.lower(),
        "author":author.lower(),
        "genre":genre.lower(),
        "due_date":None,
        "added_date": datetime.now().strftime("%d-%m-%Y"),
        "date_of_borrow":None,
        "is_available":True
    })

    write_json(library)

def view_all (library):
    if not library:
        alert_for_not()
        return

    for index, book in enumerate(library , 1):
        print_book(index , book)
    
def search_book(library):
    if not library:
        alert_for_not()
        return

    # it can either be title or author name
    while True:
        user_input = input("Please enter title or author name\n").lower()
        if user_input:
            break
    
    found = False

    for index , book in enumerate(library , 1):
        if user_input in book["author"] or user_input in book["title"]:
            print_book(index , book)
            found = True

    if not found:
        print("No book found!")


def borrow_book(library):
    if not library:
        alert_for_not()
        return
    
    while True:
        title = input("Please enter the title of the book want to borrow!\n")
        if title:
            break

    while True:
        author = input("Please enter the author name of the book want to borrow!\n")
        if author:
            break

    # if book is available
    is_found = False
    for index , book in enumerate(library , 0):
        if title.lower() == book["title"] and author.lower() == book["author"]:
            is_found = True
            book_index = index
            book_to_update = book
            today = datetime.now()

            if not book["is_available"]:
                _due_date = datetime.strptime(book["due_date"] , "%d-%m-%Y")
                days = (_due_date-today).days
                _available_on = (_due_date+timedelta(days=1)).strftime("%d-%m-%Y")
                print(f"Book is already borrowed for remaining {days} days and will be available on {_available_on}")
                return

    if not is_found:
        print("This title doesn't exist in the library")
        return
    
    while True:
            try:
                days_to_borrow = int(input("Please enter a number of days(max 30 days only))\n"))

                if(0<days_to_borrow<=30):
                    break
                else:
                    print("Please enter the number in range")
            except ValueError as v:
                print("Please enter valid days")

    date_of_borrow = today.strftime("%d-%m-%Y")
    due_date = (today + timedelta(days=days_to_borrow)).strftime("%d-%m-%Y")

    book_to_update["is_available"] = False
    book_to_update["date_of_borrow"] = date_of_borrow
    book_to_update["due_date"] = due_date

    library[book_index] = book_to_update

    write_json(library)


def view_overdues (library):
    if not library:
        alert_for_not()
        return
    
    today = datetime.now()
    found = False

    for index , book in enumerate(library , 1):
        if book["due_date"]:
            due_date = datetime.strptime(book["due_date"] , "%d-%m-%Y")
            if today > due_date:
                found = True
                print_book(index , book)

    if not found:
        print("No overdues found!")

def return_book(library):
    if not library:
        alert_for_not()
        return
    
    found_index = 1
    index_keys = {}

    for index , book in enumerate(library , 0):
        if not book["is_available"]:
            print_book(found_index , book)
            index_keys[found_index] = index
            found_index+=1

    if found_index == 1:
        print("No book borrowed yet!")
        return
    
    while True:
        try:
            book_to_return = int(input("Please select the number of the book you want to return\n"))

            if 0<book_to_return<=len(index_keys):
                break
            
            print("No book found! Please try again!")
        except ValueError as v:
            print("Please enter a valid number\n")

    book = library[index_keys[book_to_return]]

    book["is_available"] = True
    book["due_date"] = None
    book["date_of_borrow"] = None

    write_json(library)