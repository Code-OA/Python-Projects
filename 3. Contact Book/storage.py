import json

def load_json():
    try:
        with open("contacts.json" , "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return []


def write_json(data):
     with open("contacts.json" , "w") as f:
          json.dump(data , f)