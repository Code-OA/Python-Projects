from flask import Flask , jsonify , request
from storage import load_json , write_json

app = Flask(__name__)

@app.route("/notes" , methods = ["GET"])
def get_notes():
    notes = load_json()
    return jsonify(notes)

@app.route("/notes" , methods=["POST"])
def write_note():
    note = request.get_json()
    notes = load_json()
    note['id'] = len(notes)+1
    notes.append(note)
    write_json(notes)
    return jsonify(note) , 201

@app.route("/notes/<int:id>" , methods=["DELETE"])
def delete_note(id):
    notes = load_json()

    for index , note in enumerate(notes , 0):
        if note["id"] == int(id):
            deleted = notes.pop(index)
            write_json(notes)
            return jsonify(deleted) , 200
        
        
    return jsonify({"err" : "Note not found!"}) , 404
    

if __name__ == "__main__":
    app.run(debug=True)