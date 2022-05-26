Табеле у бази
=============

.. code-block:: sql
   CREATE TABLE ucenik
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           ime VARCHAR (50),
           prezime VARCHAR (50),
           datum_rodjenja DATE,
           razred INT,
           odeljenje INT);

   CREATE TABLE predmet
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           naziv VARCHAR (30),
           razred INT,
           fond INT);
                
   CREATE TABLE izostanak
          (id INTEGER PRIMARY KEY AUTOINCREMENT,
           id_ucenik REFERENCES ucenik (id) ON DELETE RESTRICT
                                            ON UPDATE RESTRICT,
           datum DATE,
           cas INT,
           status VARCHAR (15),
           UNIQUE (id_ucenik, datum, cas));

  CREATE TABLE ocena
         (id INTEGER PRIMARY KEY AUTOINCREMENT,
          id_predmet INTEGER REFERENCES predmet (id) ON DELETE RESTRICT
                                                     ON UPDATE RESTRICT,
          id_ucenik INTEGER REFERENCES ucenik (id) ON DELETE RESTRICT
                                                   ON UPDATE RESTRICT,
          ocena INT,
          datum DATE DEFAULT (date('now')) NOT NULL,
          vrsta VARCHAR (20));
