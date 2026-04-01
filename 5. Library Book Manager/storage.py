import json

def load_json():
    try:
        with open("library.json" , "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return []
    
def write_json(library):
    with open("library.json" , "w") as f:
        json.dump(library , f)