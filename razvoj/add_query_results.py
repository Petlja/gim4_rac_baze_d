import sys, os, glob
import sqlite3 as sql
import traceback

import locale
locale.setlocale(locale.LC_ALL, '')

def collate_UNICODE(str1, str2):
    return locale.strcoll(str1, str2)

def process_file(filename):
    # citamo linije ulazne datoteke
    with open(filename) as f:
       lines = f.readlines()

    # rezultate obrade upisujemo u privremenu datoteku
    with open(filename + ".tmp", "w") as f:
        i = 0
        while i < len(lines):
            print(lines[i], end="", file=f)
            # proveravamo da li tekuca linija zapocinje upit
            if lines[i].startswith(".. code-block:: sql"):
                print(lines[i+1], end="", file=f)

                # citamo upit
                i += 2
                query = "";
                while i < len(lines) and lines[i].strip() != "":
                    print(lines[i], end="", file=f)
                    query += lines[i].strip() + " ";
                    i += 1

                # obradjujemo samo rezultate SELECT upita
                if not query.startswith("SELECT"):
                    continue

                # da li je upit uspesno izvrsen
                OK = False
                # iteriramo kroz baze nad kojima se pokusava izvrasavanje upita
                databases = ['dnevnik.db',
                             'chinook.db']
                for database in databases:
                    # pokusavamo izvrsavanje upita
                    db_file = os.path.join(BASE_DIR, database)
                    con = sql.connect(db_file)
                    con.create_collation("UNICODE", collate_UNICODE)
                    cur = con.cursor();
                    try:
                        cur.execute(query)
                    except sql.Error as er:
                        # print('SQLite error: %s' % (' '.join(er.args)))
                        con.close()
                        continue

                    # Upit je uspesno izvrsen
                    result_str = "Извршавањем упита добија се следећи резултат:"
                    
                    # upisujemo rezultujucu tabelu 
                    print(file=f)
                    print(result_str, file=f)
                    print(file=f)
                    print(".. csv-table::", file=f)
                    names = list(map(lambda x: x[0], cur.description))
                    print("   :header: ", ", ".join(map(lambda x: '"' + x + '"', names)), file=f)
                    print("   :align: left", file=f)
                    print(file=f)
                    nr = 0
                    for row in cur:
                        nr += 1
                        if nr > 5:
                            print("  ", ", ".join(map(lambda x: "...", row)), file=f)
                            break

                        print("  ", ", ".join(map(lambda x: '"' + str(x) + '"' if x is not None else "NULL", row)), file=f)
                    con.close();


                    # ako je ranije vec postojala rezultujuca tabela, staru tabelu preskacemo
                    if i + 1 < len(lines) and lines[i+1].strip() == result_str:
                        i += 7 # preskacemo zaglavlje tabele
                        while i < len(lines) and lines[i].strip():
                           i += 1

                    # posto smo uspesno izvrsili upit, mozemo prekinuti iteraciju kroz baze
                    OK = True
                    break

                # ako upit nije mogao biti izvrsen ni nad jednom bazom, prijavljujemo gresku
                if not OK:
                    print("Error executing query:", query, file=sys.stderr)
                    
                print(file=f)
            i += 1

    # privremenu datoteku proglasavamo glavnom
    os.rename(filename + ".tmp", filename)
    

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) < 2:
    sys.exit("Source directory or a source file path expected")

dirent = os.path.abspath(sys.argv[1])

if dirent.endswith(".rst"):
    process_file(dirent)
else:
    path = os.path.join(dirent, "**/*.rst")
    for filename in glob.iglob(path, recursive=True):
        process_file(filename)
