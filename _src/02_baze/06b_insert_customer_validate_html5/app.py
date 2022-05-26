import os, re
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

@app.route("/customer", methods=["GET", "POST"])
def customer():
    if request.method == 'GET':
        return render_template("customer.html")
    else:
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        phone = request.form['phone']
        email = request.form['e-mail']
            
        error = None
        if not first_name or not first_name.strip():
            error = "First name is missing"
        elif not last_name or not last_name.strip():
            error = "Last name is missing"
        elif not phone  or not phone.strip():
            error = "Phone is missing"
        elif not email or not re.match(r"[a-z0-9+_\.-]+@[a-z0-9\.-]+", email):
            error = "E-mail is not valid"

        if error:
            return render_template("customer.html", msg=error)
            
        try:
            db_conn = get_db()
            cursor = db_conn.cursor()
            query = ("INSERT INTO Customer " +
                     "('FirstName', 'LastName', 'Phone', 'Email')" +
                     "VALUES (?, ?, ?, ?)")
            cursor.execute(query, (first_name, last_name, phone, email))
            db_conn.commit()
            return render_template("customer.html",
                                   msg="Customer was successfully added")
        except:
            return render_template("customer.html",
                                   msg="Error adding new customer")
