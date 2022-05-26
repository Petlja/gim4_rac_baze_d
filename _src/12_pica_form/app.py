from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if "naruci" in request.args:
        ime = request.args.get("ime")
        adresa = request.args.get("adresa")
        vrsta = request.args.get("vrsta")
        velicina = request.args.get("velicina")
        dodaci = []
        if "kecap" in request.args:
            dodaci.append(request.args.get("kecap"))
        if "origano" in request.args:
            dodaci.append(request.args.get("origano"))
            
        return render_template("narudzbenica.html", ime=ime,
                               adresa=adresa, vrsta=vrsta,
                               velicina=velicina, dodaci=dodaci)
    else:
        return render_template("formular.html")
        
