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

@app.route("/customer", methods=["GET", "POST"])
def customer():
    if request.method == 'GET':
        return render_template("customer.html")
    else:
        try:
            db_conn = get_db()
            cursor = db_conn.cursor()
            query = ("INSERT INTO Customer " +
                     "('FirstName', 'LastName', 'Phone', 'Email')" +
                     "VALUES (?, ?, ?, ?)")
            first_name = request.form['first-name']
            last_name = request.form['last-name']
            phone = request.form['phone']
            email = request.form['e-mail']
            cursor.execute(query, (first_name, last_name, phone, email))
            db_conn.commit()
            return render_template("customer.html",
                                   msg="Customer was successfully added")
        except:
            return render_template("customer.html",
                                   msg="Error adding new customer")

