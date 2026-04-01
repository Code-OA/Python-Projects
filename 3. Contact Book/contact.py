from storage import write_json

def add_contact(contacts):
    while True:
        name =  input("Please enter your name:\n")
        if name:
            break

    while True:
        number =  input("Please enter your number:\n")
        if number.isdigit() and len(number) == 10:
            break

    while True:
        email =  input("Please enter your email:\n")
        if email:
            break

    contacts.append({
        "name" : name,
        "phone" : number,
        "email": email
    })

    write_json(contacts)
    

def view_all(contacts):
    if not contacts:
        print("No contacts available")
        return
    
    for index,contact in enumerate(contacts , 1):
        print(f"{index}. {contact["name"].capitalize()} | +91 {contact["phone"]} | {contact["email"]}")

def search_contact(contacts):
    if not contacts:
        print("No contacts available")
        return

    while True:
        search_input = input("Please enter the name to search: ")
        if search_input:
            break
    
    for index , contact in enumerate(contacts , 1):
        if  search_input.lower() in contact["name"].lower():
            print(f"{index}. {contact["name"].capitalize()} | +91 {contact["phone"]} | {contact["email"]}")

def delete_contact(contacts):
    view_all(contacts)

    while True:
        try:
            number_to_del = int(input("Please select and enter a number you want to delete: "))
            if not number_to_del or number_to_del < 1 or number_to_del > len(contacts):
                print("invalid selection")
                continue

            break
        except ValueError as v:
            print("Please enter a valid number")

    popped_one = contacts.pop(number_to_del-1)

    write_json(contacts)
    print(f"{number_to_del}. {popped_one["name"]} | {popped_one["phone"]} | {popped_one["email"]}")

    