import os
from flask import Flask, render_template, g, request
import sqlite3

app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'chinook.db')

def get_db():
    if not "_db_conn" in g:
        g._db_conn = sqlite3.connect(DATABASE)
        g._db_conn.row_factory = sqlite3.Row
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

@app.route("/genres")
def genres():
    genres = query_db("SELECT GenreId, Name FROM genre")
    return render_template("genres.html", genres=genres)
    
@app.route("/tracks")
def tracks_by_genre():
    # proveravamo da li se među GET parametrima nalazi genre_id 
    if "genre_id" in request.args:
        # čitamo identifikator žanra iz GET parametara
        genre_id = request.args.get("genre_id")
        # čitamo iz baze naziv žanra
        genre_name = query_db("SELECT Name FROM Genre WHERE GenreId=?", (genre_id,), True)
        if genre_name == None:
             return render_template("tracks.html", error=True,
                                    error_msg="wrong genre id supplied")
        # čitamo iz baze spisak od najviše 10 kompozicija tog žanra
        tracks = query_db("SELECT Name FROM Track WHERE GenreId=? LIMIT 10", (genre_id,))
        # formiramo i vraćamo veb-stranu
        return render_template("tracks.html", genre_name=genre_name["Name"], tracks=tracks)
    else:
        # formiramo i vraćamo veb-stranu koja ukazuje na grešku
        return render_template("tracks.html", error=True,
                               error_msg="no genre id supplied")
