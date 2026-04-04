import os
from flask import Flask , request , jsonify
from db import db_init , create_user ,is_user , find_by_id
from dotenv import load_dotenv
import bcrypt
import sqlite3
from flask_jwt_extended import JWTManager,  create_access_token , get_jwt_identity , jwt_required

load_dotenv()
app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)

# consistent response format
def get_data(message=None , error=None):
    return {"message":message , "error" : error}

@app.route("/register" , methods=["POST"])
def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if email and password:
        password = data["password"].encode("utf-8")
        hashed_pass = bcrypt.hashpw(password , bcrypt.gensalt())
        try:
            created_user = create_user(email , hashed_pass.decode("utf-8"))
        except sqlite3.IntegrityError:
            return jsonify(get_data(error=f"{email} already exist!")) , 409
        return jsonify(created_user) , 201
    
    return jsonify(get_data("please submit the data!")) , 400
    

@app.route("/login" , methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify(get_data(error="Please provide the data!")) , 400
    email = data.get("email")
    password = data.get("password")
    if email and password:
        user_data = is_user(email)
        if(user_data):
            user_pass = user_data["data"].get("password").encode("utf-8")
            check_pass = bcrypt.checkpw(password.encode("utf-8") , user_pass)
            if check_pass:
                token = create_access_token(identity=str(user_data["data"]["id"]))
                return jsonify({"token" : token}) , 200
            
            return jsonify({"error": "sorry your email or password is wrong"}) , 401
            
    else:
        return {"message" :  "provide credentials"} , 400

@app.route("/me" , methods=["GET"])
@jwt_required()
def me():

    id = get_jwt_identity()
    print(id)

    user = find_by_id(int(id))
    if user:
        user["data"].pop("password")
        return jsonify(user["data"])
    
    return jsonify({"error": "user doesn't exist!"}) , 404

if __name__ == "__main__":
    db_init()
    app.run(debug=True)