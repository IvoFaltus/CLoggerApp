from flask import Flask, session,request,jsonify,make_response
from flask_cors import CORS
from database import authenticate,login_user, verify,deleteSession,create_user
#from database import get_db
import json
app = Flask(__name__)
app.secret_key = "i"
CORS(app,
     supports_credentials=True,
     origins=["http://localhost:5173", "http://127.0.0.1:5173"])
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"



@app.post("/login_check")
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if(authenticate(username,password)):
        token=login_user(username)
        response = jsonify({"token":token})
        response.set_cookie(
    "sessionid",
    token,
    httponly=True,
    samesite="None",
    secure=True  # only OK for localhost
)
        return response
    else:
        return jsonify({"msg":"error"})

    

@app.get("/verify_token")
def verify_token():
    print("verifyyyyyy")
    token = request.cookies.get("sessionid")
    print(token)
    print(f"{RED}{verify(token)}{RESET}")
    print(f"{RED}{token}{RESET}")
    result = {"msg":"error"} if not verify(token) else {"msg":"success"}
    
    return jsonify(result)
    
@app.get("/logout")
def logout():
    pass

@app.delete("/delete_session")
def delete_session():
    response = make_response(jsonify({"msg": "success"}), 204)

    sessionid = request.cookies.get("sessionid")
    if sessionid:
        deleteSession(sessionid)  # from db
        response.delete_cookie("sessionid", path="/")

    return response

@app.post("/create_user")
def createUser():
    data = request.get_json()
    username = data["username"]
    name=data["name"]
    lastname=data["lastname"]
    password=data["password"]
    return jsonify(create_user(username,name,lastname,password))



if __name__ == "__main__":
    app.run(debug=True)
