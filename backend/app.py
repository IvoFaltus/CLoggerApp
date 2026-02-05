from flask import Flask, session
from database import get_db

app = Flask(__name__)
app.secret_key = "i"


@app.route("/home")
def index():
    session["user"] = 1   # <-- creates session
    return "ok"

@app.route("/deepweb")
def deepweb():
    if session.get("user") == 2:
        return "nice"
    else:
        return "Access denied", 403


if __name__ == "__main__":
    app.run(debug=True)
