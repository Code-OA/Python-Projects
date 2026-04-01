from storage import write_todo_in_json
from datetime import datetime

def _print_item(index , todo):
    print(f"{index}. Task: {todo["task"]} | Priority: {todo["priority"]} | Status: {todo["status"]} | Due date: {todo["due_date"]}")

def add_task(todo_list):
    
    while True:
        task = input("Please enter your task: ")
        if task:
            break

    while True:
        print("Please choose and enter any number for respective priority: ")
        print("1. High" , "2. Medium" , "3. Low" , sep="\n")
        
        try:
            priority = int(input("Please enter your task: "))
            if priority and  1 <= priority <=3:
                break
        except ValueError as v:
            print("Please enter a valid number from the list")

    priority_list = {
        1:"high",
        2:"medium",
        3:"low"
    }

    while True:
        due_date = input("Enter due date (DD-MM-YYYY): ")
        try:
            # checking for valid date format
            datetime.strptime(due_date , "%d-%m-%Y")
            break
        except ValueError as v:
            print("please enter valid date format\n")

    todo_list.append({
        "task": task,
        "priority" : priority_list[priority],
        "due_date" : due_date,
        "status" : False
    })

    write_todo_in_json(todo_list)

def view_all(todo_list):
    if not todo_list:
        print("No items found!")
        return
    
    priority_order = {
        "high":1,
        "medium":2,
        "low":3
    }

    sorted_tasks = sorted(todo_list , key=lambda task : priority_order[task["priority"]])

    for index , todo in enumerate(sorted_tasks , 1):
        _print_item(index , todo)

def view_all_actions(todo_list):
    for index , todo in enumerate(todo_list , 1):
        _print_item(index , todo)


def mark_complete(todo_list):

    if not todo_list:
        print("No items found!")
        return
    
    view_all_actions(todo_list)

    while True:
        try:
            has_done = int(input("Please select a number you want to set as done to it's respective task"))

            if has_done and 1<=has_done<=len(todo_list):
                break
            else:
                print("Please select the number in range\n")

        except ValueError as v:
            print("Please enter a valid input!")

    task_done = todo_list[has_done-1]

    task_done["status"] = True

    write_todo_in_json(todo_list)

    print("Your task has been updated successfully")

    _print_item(has_done , task_done)


def delete_task (todo_list):
    if not todo_list:
        print("No items found!")
        return
    
    view_all_actions(todo_list)

    while True:
        try:
            number_to_delete = int(input('Please enter the number you want to delete\n'))

            if number_to_delete and 1<=number_to_delete<=len(todo_list):
                break
            else:
                print("No task found")
        except ValueError as v:
            print("Please enter a valid number")

    removed_item =  todo_list.pop(number_to_delete-1)

    write_todo_in_json(todo_list)

    _print_item(number_to_delete , removed_item)