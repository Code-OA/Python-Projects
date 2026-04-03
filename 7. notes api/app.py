from flask import Flask , jsonify , request
import database

app = Flask(__name__)

@app.route("/notes" , methods = ["GET"])
def get_notes():
    notes = database.get_all_notes()
    return jsonify(notes) , 200

@app.route("/notes" , methods=["POST"])
def write_note():
    note = request.get_json()
    if note.get("title") and note.get("content") :
        note = database.create_note(note["title"] , note["content"])
        return jsonify(note) , 201
    
    return jsonify({"error" : "something went wrong!"}) , 400

@app.route("/notes/<string:id>" , methods=["DELETE"])
def delete_note(id):
    note = database.delete_note(id)
    if note:
        return jsonify(note) , 200
    
    return jsonify({"error" : "Note not found!"}) , 404
    

if __name__ == "__main__":
    database.init()
    app.run(debug=True)