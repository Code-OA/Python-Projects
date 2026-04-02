import json

def load_json():
    try:
        with open("notes.json" , "r") as f:
            return json.load(f)
    except (FileNotFoundError , json.JSONDecodeError):
        return []
    
def write_json (notes):
    with open("notes.json" , "w") as f:
        json.dump(notes , f)