import json

def load_todo():
    try:
        with open("todo_list.json" , "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return []
    
def write_todo_in_json(todo_list):
    with open("todo_list.json" , "w") as f:
        json.dump(todo_list , f)
