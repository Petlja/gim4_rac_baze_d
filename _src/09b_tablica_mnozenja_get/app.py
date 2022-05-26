from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    n = request.args.get("n", 10, int)
    return render_template("tablica.html", n=n)
