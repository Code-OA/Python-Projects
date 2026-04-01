import json
students = []

def load_file_data():
    global students

    try:
        with open("grades.json" , "r") as f:
            students = json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        pass

def write_to_file():

    with open("grades.json" , "w") as f:
        json.dump(students , f)

def add_student():
    name = input("Please enter your name:\n")
    
    if not name:
        print("Please enter your name\n")
        return

    while True:
        grades = input("Please enter your grades (separated by blank space):\n")
        if grades:
            grades = grades.split()
            break
        else:
            print("Please enter the marks")

    try:
        for index , grade in enumerate(grades , 0):
            grades[index] = int(grade)
    except ValueError as v:
        print("Please enter valid marks")
        return

    students.append({
        "name" : name,
        "grades" : grades
    })

    write_to_file()


def students_with_avg():

    if not students:
        print("No students found")
        return

    for index , student in enumerate(students , 1):
        avg = sum(student["grades"])/len(student["grades"])
        print(f"{index}. Name: {student["name"].capitalize()} | Average: {avg}")

def failing_students():
    if not students:
        print("No students found")
        return

    for index , student in enumerate(students , 1):
        avg = sum(student["grades"])/len(student["grades"])

        if avg < 40:
            print(f"{index}. Name: {student["name"].capitalize()} | Average: {avg}")

def delete_student ():
    if not students:
         print("No student found!")
         return
     
    for index , student in enumerate(students , 1):
         total = sum(student["grades"])
         avg = total/len(student["grades"])
         
         print(f"{index}. Name: {student["name"]} | Average: {avg} | Total marks: {total}")

    while True:
        try:
            want_to_del = int(input("Please type number of the item you want to delete: "))
            
            if want_to_del < 1 or want_to_del > len(students):
                print("Invalid number")
                continue

            popped_one = students.pop(want_to_del-1)
            write_to_file()

            print(f"{want_to_del} {popped_one["name"]} has been deleted successfully")
            break
        except ValueError as v:
            print("Please select a valid number")


def show_menu ():

    load_file_data()

    while True:
        print("Welcome to Grade Manager!")

        print("Press:-")
        print("1. Add Student")
        print("2. Stduents with their average")
        print("3. View failing students (average < 40)")
        print("4. Delete a student")
        print("'Type 'exit' to quit")

        selected_cmd = input("Please choose and write any option by number to perform an action:\n")

        if selected_cmd == "exit":
            exit()
        
        if selected_cmd == "1":
            add_student()
        elif selected_cmd == "2":
            students_with_avg()
        elif selected_cmd == "3":
            failing_students()
        elif selected_cmd == "4":
            delete_student()
        else:
            print("Please select a valid command")

        print("\n")

show_menu()