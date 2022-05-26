from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/calculator")
def calculator():
    sab1 = request.args.get("sab1", "")
    sab2 = request.args.get("sab2", "")
    try:
        zbir = int(sab1) + int(sab2)
    except:
        zbir = None
    return render_template("index.html", sab1=sab1, sab2=sab2, zbir=zbir)
