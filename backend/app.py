from flask import Flask, session
from database import get_db

app = Flask(__name__)
app.secret_key = "i"


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





@app.route("/home")
def index():
    session["user"] = 1   # <-- creates session
    return "ok"



@app.route("/login", methods=["POST"])
def login():
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
