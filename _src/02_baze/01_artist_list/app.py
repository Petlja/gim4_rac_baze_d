import os
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'chinook.db')

def get_db():
    if not "_db_conn" in g:
        g._db_conn = sqlite3.connect(DATABASE) 
    return g._db_conn

@app.teardown_appcontext
def close_db(exception):
    if "_db_conn" in g:
        g._db_conn.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    if one:
        return rows[0] if rows else None
    else:
        return rows
        
@app.route("/artists")
def artists():
    artists = query_db("SELECT Name FROM Artist LIMIT 10")
    return render_template("artists.html", artists=artists)
