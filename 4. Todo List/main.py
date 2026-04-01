from storage import load_todo
import tasks

def main():
    todo_list = load_todo()

    while True:
        print("Welcome to Todo list!")

        print("1. Add Task")
        print("2. View Task")
        print("3. Mark as complete")
        print("4. Delete the task")
        print("Type 'exit' to quit")

        user_input = input("Please enter a number to peform the action: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            exit()

        if user_input == "1":
            tasks.add_task(todo_list)
        elif user_input == "2":
            tasks.view_all(todo_list)
        elif user_input == "3":
            tasks.mark_complete(todo_list)
        elif user_input == "4":
            tasks.delete_task(todo_list)

if __name__ == "__main__":
    main()