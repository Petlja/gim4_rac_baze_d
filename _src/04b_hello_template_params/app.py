from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    ucenici = [("Петар", "Петровић"),
               ("Јована", "Јовановић"),
               ("Ана", "Анић")]
    return render_template("ucenici.html", ucenici=ucenici)
