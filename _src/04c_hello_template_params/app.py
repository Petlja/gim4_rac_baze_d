from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    ucenici = [{"ime": "Петар", "prezime": "Петровић"},
               {"ime": "Јована", "prezime": "Јовановић"},
               {"ime": "Ана", "prezime": "Анић"}]
    return render_template("ucenici.html", ucenici=ucenici)
