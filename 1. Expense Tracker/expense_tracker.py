from datetime import datetime
import json

expenses = []

def fetch_from_file ():
    global expenses

    try:
        with open("expenses.json" , "r") as f:
            expenses = json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        pass

def write_to_file ():
    with open("expenses.json" , "w") as f:
        json.dump(expenses , f)

def filter_by_category ():
    category_input = input("Please enter the category: ").lower()

    found = False

    if not expenses:
        print("No expenses right now! Please add expenses first")
        return

    for index , expense in enumerate(expenses , 1):
        if category_input in expense["category"]:
            found = True
            print(f"{index}. Amount : {expense["amount"]} | Category : {expense["category"].capitalize()} | Description : {expense["description"]} | Date : {expense["date"]} | Day : {expense["day"]}\n")

    if not found:
        print("No result found!\n")
        
                
def delete_expense ():

    if not expenses:
        print("No expenses right now! Please add expenses first")
        return

    for index , expense in enumerate(expenses , 1):
        print(f"{index}. Amount : {expense["amount"]} | Category : {expense["category"].capitalize()} | Description : {expense["description"]} | Date : {expense["date"]} | Day : {expense["day"]}\n")

    try:
        delete_number_input = int(input("Please enter the number of the item to remove: "))

        if delete_number_input < 1 or delete_number_input > len(expenses):
            print("Alert! Invalid number entered\n")
        else:
            pop_item = expenses[delete_number_input-1]
            expenses.pop(delete_number_input-1)
            write_to_file()
            print(f"your expense from the list has been deleted\nAmount : {pop_item["amount"]} | Category : {pop_item["category"].capitalize()} | Description : {pop_item["description"]} | Date : {pop_item["date"]} | Day : {pop_item["day"]}\n")
    except ValueError as e:
        print("Alert! Please enter a valid number\n")
    

def add_expense ():
    try:
        amount = float(input("Please enter the amount: "))
    except ValueError as e:
        print("Please enter a valid amount")
        return

    category = input("Please enter the category: ")

    description = input("Please write a description: ")
    today = datetime.now()
    date = today.strftime("%d-%m-%Y")
    day = today.strftime("%A")
    
    expenses.append({
        "amount" : amount,
        "category" : category.lower(),
        "description" : description,
        "date" : date,
        "day" : day
    })

    write_to_file()


def view_all ():
    

    if not expenses:
        print("No expenses right now! Please add expenses first")
        return

    for index , expense in enumerate(expenses , 1):
        print(f"{index}. Amount : {expense["amount"]} | Category : {expense["category"].capitalize()} | Description : {expense["description"]} | Date : {expense["date"]} | Day : {expense["day"]}\n")

def view_total ():
    if not expenses:
        print("No expenses right now! Please add expenses first")
        return
    
    total = sum(expense["amount"] for expense in expenses)

    print(f"Your total amount is {total}\n")

def show_menu ():
    fetch_from_file()

    while True:
        print("1. Add Expense")
        print("2. View all")
        print("3. View total")
        print("4. Filter")
        print("5. Delete")
        print("6. Exit")
        print("Please choose any option and type here: " , end="")
        selected_command = input()

        if selected_command == "1":
            add_expense()
        elif selected_command == "2":
            view_all()
        elif selected_command == "3":
            view_total()
        elif selected_command == "4":
            filter_by_category()
        elif selected_command == "5":
            delete_expense()
        elif selected_command == "6":
            exit()
        else:
            print("Alert! Enter a valid command.")



show_menu()