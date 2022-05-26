from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<ime>")
def pozdravi(ime):
    return render_template("index.html", ime=ime)
