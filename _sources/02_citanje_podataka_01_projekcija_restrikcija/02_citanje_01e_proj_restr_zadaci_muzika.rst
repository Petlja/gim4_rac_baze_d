Пројекција и селекција -- музика
--------------------------------

Прикажимо сада неколико упита над базом која садржи податке компанију
за продају музичких композиција.

.. questionnote::

   Прикажи све називе извођача.

.. code-block:: sql

   SELECT naziv
   FROM izvodjac;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv"
   :align: left

   "AC/DC"
   "Accept"
   "Aerosmith"
   "Alanis Morissette"
   "Alice In Chains"
   ...

.. questionnote::

   Прикажи све називе песама са албума чији је идентификатор 1.

.. code-block:: sql

   SELECT naziv
   FROM kompozicija
   WHERE id_album = 1;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv"
   :align: left

   "For Those About To Rock (We Salute You)"
   "Put The Finger On You"
   "Let's Get It Up"
   "Inject The Venom"
   "Snowballed"
   ...

.. questionnote::

   Прикажи сва имена и презимена запослених који су из Канаде.

.. code-block:: sql

   SELECT ime, prezime
   FROM zaposleni
   WHERE drzava = 'Canada';

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "ime", "prezime"
   :align: left

   "Andrew", "Adams"
   "Nancy", "Edwards"
   "Jane", "Peacock"
   "Margaret", "Park"
   "Steve", "Johnson"
   ..., ...


Вежба
.....

Покушај сада самостално да решиш наредних неколико задатака.

.. questionnote::

   Прикажи називе свих албума извођача чији је идентификатор 1.

.. dbpetlja:: db_proj_restr_muz_01
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT naziv
                   FROM album
                   WHERE id_izvodjac = 1

.. questionnote::

   Прикажи идентификаторе, имена и презимена купаца који се зову ``Jack``.

.. dbpetlja:: db_proj_restr_muz_02
   :dbfile: music.sql
   :showresult:
   :solutionquery:  SELECT id_kupac, ime, prezime
                    FROM kupac
                    WHERE ime = 'Jack'
