from flask import Flask, session,request,jsonify
from flask_cors import CORS
from database import authenticate,login_user
#from database import get_db
import json
app = Flask(__name__)
app.secret_key = "i"
CORS(app,supports_credentials=True)

users = {
    "jozef":{
        "password":"jozef1",
        "data":"jozefova data"
        
        
        },
    "peter":{
        "password":"peter1",
        "data":"petrova data"
        
        
        },
    "vojta":{
        "password":"vojta1",
        "data":"vojtova data"
        
        
        },
    
    
    
}

usersession = {
}





@app.post("/login_check")
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    if(authenticate(username,password)):
        token=login_user(username)
        response = jsonify({"token":token})
        response.set_cookie("sessionid", token, httponly=True, samesite="Lax")
        return response
    else:
        return jsonify({"msg":"error"})

    





if __name__ == "__main__":
    app.run(debug=True)
