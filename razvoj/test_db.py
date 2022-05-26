import os
import sqlite3

import locale
locale.setlocale(locale.LC_ALL, 'sr_RS.UTF-8')

def get_db():
    if not "db_conn" in globals():
        global db_conn
        db_conn = sqlite3.connect(os.path.join(os.getcwd(), 'dnevnik.db'))
        db_conn.row_factory = sqlite3.Row
       
        def collate_UNICODE(str1, str2):
            return locale.strcoll(str1, str2)

        db_conn.create_collation("UNICODE", collate_UNICODE)
    return db_conn
       

import atexit

@atexit.register
def close_db():
    if "db_conn" in globals():
        global db_conn
        db_conn.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    if one:
        return rows[0] if rows else None
    else:
        return rows

for prezime in query_db("SELECT DISTINCT substr(prezime, 1, 1) FROM ucenik ORDER BY prezime"):
    print(prezime[0])

