import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(conn, table_name, create_table_sql_statement):
    try:
        cur = conn.cursor()
        cur.execute('DROP TABLE ' + table_name)
        conn.commit()
    except Error as e:
        pass

    try:
        c = conn.cursor()
        c.execute(create_table_sql_statement)
    except Error as e:
        print(e)


def fill_table(conn, sql_create_statement, sql_insert_statement, table_name, path, line_to_tuple):
    print(f'Creating and filling table {table_name}')
    create_table(conn, table_name, sql_create_statement)
    header = True
    cur = conn.cursor()
    # with open(path, 'r', encoding='utf-8') as f:
    f = open(path, 'r', encoding='utf-8')
    count = 0
    for line in f:
        if not header:
            table_rows = line_to_tuple(line)
            for table_row in table_rows:
                cur.execute(sql_insert_statement, table_row)
                count += 1
                if count % 100_000 == 0:
                    print(f'\r{count} rows', end='')
        header = False
    f.close()
    conn.commit()              
    print()
    print(f'Table {table_name} done')


def fill_table_titles(conn):
    sql_create_titles_table = """ CREATE TABLE IF NOT EXISTS NASLOVI (
                                    id text PRIMARY KEY,
                                    tip text,
                                    primarni_naslov text,
                                    originalni_naslov text,
                                    god_pocetka integer,
                                    god_kraja integer,
                                    trajanje_minuta integer,
                                    zanrovi text
                                    ); """
    sql_insert_titles = ''' INSERT INTO NASLOVI(id, tip, primarni_naslov, originalni_naslov, god_pocetka, god_kraja, trajanje_minuta, zanrovi)
                           VALUES(?, ?, ?, ?, ?, ?, ?, ?) '''
    fill_table(conn, sql_create_titles_table, sql_insert_titles, 'NASLOVI', 'title.basics.tsv', line_to_tuple_titles)
    
def fill_tables_names(conn):
    sql_create_names_table = """ CREATE TABLE IF NOT EXISTS IMENA (
                                        id text PRIMARY KEY,
                                        ime text NOT NULL,
                                        god_rodjenja integer,
                                        god_smrti integer,
                                        glavno_zanimanje text
                                    ); """
    sql_insert_names = ''' INSERT INTO IMENA(id, ime, god_rodjenja, god_smrti, glavno_zanimanje)
                           VALUES(?, ?, ?, ?, ?) '''
    fill_table(conn, sql_create_names_table, sql_insert_names, 'IMENA', 'name.basics.tsv', line_to_tuple_names)


def fill_tables_roles(conn):
    # sql_create_roles_table = """ CREATE TABLE IF NOT EXISTS ULOGE (
                                        # FOREIGN KEY (id_ime) REFERENCES imena (id),
                                        # FOREIGN KEY (id_naslov) REFERENCES naslovi (id)
                                    # ); """
    sql_create_roles_table = """ CREATE TABLE IF NOT EXISTS ULOGE (
                                        id_ime text,
                                        id_naslov text
                                    ); """
    sql_insert_roles = ''' INSERT INTO ULOGE(id_ime, id_naslov)
                           VALUES(?, ?) '''
    fill_table(conn, sql_create_roles_table, sql_insert_roles, 'ULOGE', 'name.basics.tsv', line_to_tuple_roles)


def fill_table_ratings(conn):
    sql_create_ratings_table = """ CREATE TABLE IF NOT EXISTS OCENA (
                                    id_naslov text,
                                    srednja_ocena real,
                                    br_glasova integer
                                    ); """
    sql_insert_ratings = ''' INSERT INTO OCENA(id_naslov, srednja_ocena, br_glasova)
                           VALUES(?, ?, ?) '''
    fill_table(conn, sql_create_ratings_table, sql_insert_ratings, 'OCENA', 'title.ratings.tsv', line_to_tuple_ratings)

def fill_table_crew(conn):
    sql_create_crew_table = """ CREATE TABLE IF NOT EXISTS AUTORI (
                                    id_naslov text,
                                    reziseri text,
                                    scenaristi text
                                    ); """
    sql_insert_crew = ''' INSERT INTO AUTORI(id_naslov, reziseri, scenaristi)
                           VALUES(?, ?, ?) '''
    fill_table(conn, sql_create_crew_table, sql_insert_crew, 'AUTORI', 'title.crew.tsv', line_to_tuple_crew)


def line_to_tuple_titles(line):
    id, title_type, primary_title, original_title, is_adult, start_year, end_year, runtime_minutes, genres = line.split('\t')
    if is_adult == '0':
        return ((id, title_type, primary_title, original_title, start_year, end_year, runtime_minutes, genres), )
    return tuple()

def line_to_tuple_names(line):
    id_name, name, birth_year, death_year, primary_profession, known_for_titles = line.split('\t')
    return ((id_name, name, birth_year, death_year, primary_profession), )

def line_to_tuple_roles(line):
    id_name, name, birth_year, death_year, primary_profession, known_for_titles = line.split('\t')
    result = []
    for id_title in known_for_titles.split(','):
        result.append((id_name, id_title))
    return result

def line_to_tuple_ratings(line):
    id_naslov, srednja_ocena, br_glasova = line.split('\t')
    return ((id_naslov, srednja_ocena, br_glasova), )

def line_to_tuple_crew(line):
    id_naslov, reziseri, scenaristi = line.split('\t')
    return ((id_naslov, reziseri, scenaristi), )


def main():
    print(f'sqlite3 verzija {sqlite3.version}')
    database = r"filmovi_sqlite.db"

    conn = create_connection(database)
    if conn is None:
        print("Error! cannot create the database connection.")
        return

    fill_table_titles(conn)   
    fill_tables_names(conn)
    fill_tables_roles(conn)
    fill_table_ratings(conn)
    fill_table_crew(conn)

    conn.close() 

        
if __name__ == '__main__':
    main()
