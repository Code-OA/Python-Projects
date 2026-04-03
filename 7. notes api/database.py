import sqlite3
import uuid
from datetime import datetime

def get_connection ():
    conn = sqlite3.connect("notes.db")
    conn.row_factory = sqlite3.Row
    return conn

def init():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes(
                 id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                 content TEXT NOT NULL,
                 created_at TEXT
                 )
""")
    
    conn.commit()
    conn.close()

def get_all_notes():
    conn = get_connection()
    notes = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()

    return [dict(note) for note in notes]

def create_note(title, content):
    conn = get_connection()
    note_id = str(uuid.uuid4())
    created_at = datetime.now().strftime("%d-%m-%Y")
    conn.execute("INSERT INTO notes (id , title , content , created_at) Values (?, ?, ?, ?)" , (note_id , title , content , created_at))

    conn.commit()
    conn.close()
    return {"id" : note_id , "title" : title , "content" : content , "created_at" : created_at}

def delete_note(id):
    conn = get_connection()
    note = conn.execute("SELECT * FROM notes WHERE id = ?" , (id,)).fetchone()
    if not note:
        conn.close()
        return None
    query = "DELETE FROM notes WHERE id = ?"
    conn.execute(query , (id,))
    conn.commit()
    conn.close()
    return dict(note)