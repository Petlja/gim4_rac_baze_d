import os
import shutil
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

DATABASE = os.path.join(app.instance_path, 'dnevnik.db')

if not os.path.exists(DATABASE):
    os.makedirs(app.instance_path)
    shutil.copyfile(os.path.join(app.root_path, 'dnevnik.db'), DATABASE)

def procitaj_sve_ucenike(conn, razred):
    cur =  conn.cursor()
    osnovni_upit = 'SELECT ime, prezime FROM ucenik'
    if razred:
        cur.execute(osnovni_upit + ' WHERE razred=?', (razred,))
    else:
        cur.execute(osnovni_upit)
    ucenici = []
    for ime, prezime in cur:
        ucenici.append({'ime': ime, 'prezime': prezime})
    cur.close()
    return ucenici

@app.route('/')
def index():
    razred = request.args.get('razred', None, int)
    conn = sqlite3.connect(DATABASE)
    ucenici = procitaj_sve_ucenike(conn, razred)
    conn.close()
    return render_template('index.html', razred=razred, ucenici=ucenici)
