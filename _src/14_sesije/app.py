from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "tajni kljuc nase aplikacije"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        return render_template("index.html", username=username)
    else:
        return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))
    
