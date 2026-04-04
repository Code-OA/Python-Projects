import sqlite3


def get_connection ():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

SCHEMA = """
CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT  NOT NULL
                 )
"""

def db_init():
    conn = get_connection()
    conn.execute(SCHEMA)
    conn.commit()
    conn.close()

def create_user(email , password):
    conn = get_connection()
    conn.execute("INSERT INTO users (email , password) Values (? , ?)" , (email ,password))
    conn.commit()
    conn.close()
    return {"message" : "successfully created user" , "error" : False}

def is_user(email):
    conn = get_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?" , (email,)).fetchone()
    conn.close()
    
    if not user:
        return None
    
    return {"data": dict(user) , "error" : False}

def find_by_id(id):
    conn = get_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?" , (id,)).fetchone()

    if not user:
        return None
    
    return {"data":dict(user)}

    
