import os
from flask import Flask, render_template, request, flash, redirect, url_for, session, g
import sqlite3
import bcrypt

app = Flask(__name__)

DATABASE = os.path.join(app.root_path, 'prodavnica.db')

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

app.secret_key = b'Ky\x9fB\xcd\x8d\xd55\xc2\x7f\xe8=\x1eE\xcf\xff'

# [index]
@app.route("/")
def index():
    return render_template("index.html");
# [index]


# [validate-register-form]
def validate_register_form(form):
    if not "username" in form or not form["username"].strip():
        return False
    if not "password" in form or not form["password"].strip():
        return False;
    if not "name" in form or not form["name"].strip():
        return False
    if not "email" in form or not form["email"].strip():
        return False
    return True
# [validate-register-form]

# [validate-login-form]
def validate_login_form(form):
    if not "username" in form or not form["username"].strip():
        return False
    if not "password" in form or not form["password"].strip():
        return False
    return True
# [validate-login-form]

# [username-available]
def username_available(username):
    count = query_db("SELECT COUNT(*) FROM user WHERE username=?", (username, ), True)[0]
    return count == 0
# [username-available]

# [register-user]
def register_user(username, password, name, email):
    db_conn = get_db()
    cursor = db_conn.cursor()
    hash_and_salt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    cursor.execute("INSERT INTO user VALUES (?, ?, ?, ?)", (username, hash_and_salt, name, email))
    db_conn.commit()
# [register-user]

# [check-login]
def check_login(username, password):
    row = query_db("SELECT password FROM user WHERE username=?", (username, ), True)
    if not row:
        return False
    hash_and_salt = row[0]
    return bcrypt.checkpw(password.encode(), hash_and_salt)
# [check-login]

# [login]
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        OK = True
        if validate_login_form(request.form):
            username = request.form["username"]
            password = request.form["password"]
            if check_login(username, password):
                session["username"] = request.form["username"]
            else:
                OK = False
        else:
            OK = False
        if OK:
            flash("Uspešno ste se ulogovali", "success")
        else:
            flash("Pogrešno korisničko ime ili lozinka", "danger")
    else:
        flash("Greška u prenosu podataka o logovanju", "danger")
    return redirect(url_for("index"))
# [login]

# [logout]
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))
# [logout]

# [register]
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        if validate_register_form(request.form):
            username = request.form["username"]
            if not username_available(username):
                flash("Korisničko ime " + username + " je već odabrano, " +
                      "molimo vas da pokušate ponovo", "danger")
                return render_template("register.html",
                                       name=name, email=email)
            else:
                password = request.form["password"]
                name = request.form["name"]
                email = request.form["email"]
                register_user(username, password, name, email)
                session["username"] = username    # korisnika automatski i logujemo
                flash("Korisnik " + username + " je uspešno registrovan", "success")
                return redirect(url_for("index")) # vraćamo se na početnu stranu
        else:
            flash("Pogrešno navedeni podaci u formularu za registraciju", "danger")
            username = request.form["username"]
            name = request.form["name"]
            email = request.form["email"]
            return render_template("register.html",
                                   username=username, name=name, email=email)
    else:
        return render_template("register.html")
# [register]
