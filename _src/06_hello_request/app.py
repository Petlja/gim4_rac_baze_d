from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/pretraga")
def search():
    vrsta = request.args.get("vrsta", "svi proizvodi")
    max_cena = request.args.get("max_cena", float('inf'), type=float)
    return render_template("search.html",
                           vrsta=vrsta, max_cena=max_cena)
