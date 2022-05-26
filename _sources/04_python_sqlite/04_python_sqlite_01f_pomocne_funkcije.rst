Дефинисање помоћних функција
----------------------------

Ако се пише више скриптова за рад над истом базом података (што је
често случај код програмирања веб-апликација), тада се програми могу
учинити мало разумљивијим, а програмирање се може мало олакшати
дефинисањем неких помоћних функција.

Једна од њих је функција за повезивање са базом. Могуће је дефинисати
функцију ``get_db()`` чији је задатак да врати конекцију ка бази. Ако
конекција није раније успостављена, она се тада успоставља (позивом
функције ``sqlite3.connect``), а ако јесте, тада се враћа раније
успостављена конекција. Проверу да ли је конекција већ дефинисана
можемо извршити тако што проверимо да ли се ниска ``"db_conn"`` налази
међу називима глобалних променљивих (доступног путем функције
``globals()``).

.. code-block:: py

   def get_db():
       if not "db_conn" in globals():
           global db_conn
           db_conn = sqlite3.connect(os.path.join(os.getcwd(), 'dnevnik.db'))
           db_conn.row_factory = sqlite3.Row
          
           def collate_UNICODE(str1, str2):
               return locale.strcoll(str1, str2)
    
           db_conn.create_collation("UNICODE", collate_UNICODE)
       return db_conn

Можемо дефинисати функцију за затварање везе са базом података (ако је
током скрипта била отворена) и подесити да она аутоматски буде позвана
на крају рада скрипта (то радимо коришћењем модула ``atexit``).

.. code-block:: py

   import atexit

   @atexit.register
   def close_db():
       if "db_conn" in globals():
           global db_conn
           db_conn.close()


Можемо дефинисати и функцију за постављање упита. Њој прослеђујемо
упит, параметре упита и податак о томе да ли желимо само прву врсту
резултата или све врсте резултата.
        
.. code-block:: py

   def query_db(query, args=(), one=False):
       cur = get_db().execute(query, args)
       rows = cur.fetchall()
       cur.close()
       if one:
           return rows[0] if rows else None
       else:
           return rows

Са овим функцијама на располагању, веома једноставно можемо постављати
упите и обрађивати њихове резултате (при чему не морамо експлицитно
позивати функције за отварање и затварање конекције са базом). На
пример, списак свих ученика можемо исписати на следећи начин.

.. code-block:: py

   for (ime, prezime) in query_db("SELECT ime, prezime FROM ucenik"):
       print(ime, prezime)

Име и презиме ученика са датим идентификатором можемо одредити и исписати
на следећи начин:

.. code-block:: py

   id = int(input("Unesi ID učenika:"))
   (ime, prezime) = query_db("SELECT ime, prezime FROM ucenik WHERE ID=?", (id,), True)
   print(ime, prezime)
