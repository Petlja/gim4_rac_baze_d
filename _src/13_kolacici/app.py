from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    if "name" in request.cookies:
        name = request.cookies.get("name")
        return render_template("index.html", name=name)
    else:
        return render_template("index.html")

@app.route("/setcookie", methods=["POST", "GET"])
def setcookie():
    if request.method == "POST":
        name = request.form["name"]
        response = make_response(redirect(url_for("index")))
        response.set_cookie("name", name)
        return response

@app.route("/resetcookie")
def resetcookie():
    response = make_response(redirect(url_for("index")))
    response.set_cookie("name", "", expires=0)
    return response
    
