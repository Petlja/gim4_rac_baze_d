Агрегатне функције и груписање -- музика
----------------------------------------

Прикажимо сада неколико упита који користе агегатне функције и
груписање над базом продавнице музичких композиција.

.. questionnote::

   Израчунати колико укупно гигабајта заузимају све композиције.

.. code-block:: sql

   SELECT SUM(velicina) / (1024.0 * 1024.0 * 1024.0) AS GB
   FROM kompozicija;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "GB"
   :align: left

   "109.32446955703199"

|

.. questionnote::

   Одредити колико милисекунди траје најкраћа, а колико најдужа композиција.

.. code-block:: sql

   SELECT Min(trajanje) AS najkraca, Max(trajanje) AS najduza
   FROM kompozicija;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "najkraca", "najduza"
   :align: left

   "1071", "5286953"

|

.. questionnote::

   Одредити укупан број жанрова.

.. code-block:: sql

   SELECT COUNT(*)
   FROM zanr

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "COUNT(*)"
   :align: left

   "25"

|

.. questionnote::

   Одредити број различитих албума који садрже песме.

.. code-block:: sql

   SELECT COUNT(DISTINCT id_album)
   FROM kompozicija

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "COUNT(DISTINCT id_album)"
   :align: left

   "347"

|

.. questionnote::

   Одредити број албума у табели албума.

.. code-block:: sql

   SELECT COUNT(*)
   FROM album

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "COUNT(*)"
   :align: left

   "347"

|

.. questionnote::

   Одредити број композиција сваког жанра.

.. code-block:: sql

   SELECT id_zanr, COUNT(*)
   FROM kompozicija
   GROUP BY id_zanr

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id_zanr", "COUNT(*)"
   :align: left

   "1", "1297"
   "2", "130"
   "3", "374"
   "4", "332"
   "5", "12"
   ..., ...

|

.. questionnote::

   Одредити укупну дужину свих песама на сваком албуму. Списак уредити
   по укупној дужини, од најкраћих, до најдужих албума.


.. code-block:: sql

   SELECT id_album, SUM(trajanje) AS trajanje_albuma
   FROM kompozicija
   GROUP BY id_album
   ORDER BY trajanje_albuma

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id_album", "trajanje_albuma"
   :align: left

   "340", "51780"
   "345", "66639"
   "318", "101293"
   "328", "110266"
   "315", "120000"
   ..., ...

|

.. questionnote::

   Одредити највећи број песама на некој листи.


.. code-block:: sql

   SELECT COUNT(*) AS broj
   FROM plejlista_kompozicija
   GROUP BY id_plejlista
   ORDER BY broj DESC
   LIMIT 1

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "broj"
   :align: left

   "3290"

Вежба
.....

.. questionnote::

   На основу свих наруџбеница одредити укупан промет компаније.

   
.. dbpetlja:: db_agregatne_muzika_zadaci_01
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT SUM(ukupan_iznos)
                   FROM narudzbenica

.. questionnote::

   Одредити просечни износ наруџбенице током 2010. године.
   

.. dbpetlja:: db_agregatne_muzika_zadaci_02
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT AVG(ukupan_iznos)
                   FROM narudzbenica
                   WHERE datum LIKE '2010-%'

.. questionnote::

   За сваког купца који је извршио неку наруџбину током 2011. године
   приказати укупан износ наруџбина које је извршио током те
   године. Резултате приказати заокружене на најближи цео број у
   нерастућем редоследу укупног износа наруџбина.
   

.. dbpetlja:: db_agregatne_muzika_zadaci_03
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT id_kupac, ROUND(SUM(ukupan_iznos)) AS ukupno
                   FROM narudzbenica
                   WHERE strftime('%Y', datum) == '2009'
                   GROUP BY id_kupac
                   ORDER BY ukupno DESC


.. questionnote::

   За сваку годину приказати укупан број наруџбина. Резултат сортирати
   на основу године.
   

.. dbpetlja:: db_agregatne_muzika_zadaci_04
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT strftime('%Y', datum) AS godina, COUNT(*) AS ukupno
                   FROM narudzbenica
                   GROUP BY godina
                   ORDER BY godina


.. questionnote::

   На табеле ставки наруџбина ``stavka_narudzbenice`` приказати укупан
   износ наруџбина на свакој наруџбеници (износ сваке ставке се добија
   множењем количине ``kolicina`` и јединичне цене ``cena``, а укупан
   износ наруџбине се добија сабирањем свих овако израчунатих износа
   ставки са те наруџбине). Сваки износ заокружити на две децимале.
   

.. dbpetlja:: db_agregatne_muzika_zadaci_05
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT id_narudzbenica, ROUND(SUM(kolicina * cena), 2) AS Ukupno
                   FROM stavka_narudzbenice
                   GROUP BY id_narudzbenica

      
.. questionnote::

   За сваку државу из које постоји неки купац приказати укупан број
   купаца.

.. dbpetlja:: db_agregatne_muzika_zadaci_06
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT drzava, COUNT(*) AS broj_kupaca
                   FROM kupac
                   GROUP BY drzava

                   
.. questionnote::

   За сваку земљу из које постоји бар 5 купаца приказати укупан број
   купаца (резултат сортирати по броју купаца, нерастући).

.. dbpetlja:: db_agregatne_muzika_zadaci_07
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT drzava, COUNT(*) AS broj_kupaca
                   FROM kupac
                   GROUP BY drzava
                   HAVING broj_kupaca >= 5
                   ORDER BY broj_kupaca DESC
                   
.. questionnote::

   Приказати идентификаторе жанрова за које је у понуди више од 10
   сати музике.

.. dbpetlja:: db_agregatne_muzika_zadaci_08
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT id_zanr
                   FROM kompozicija
                   GROUP BY id_zanr
                   HAVING SUM(trajanje) >= 10 * 60 * 60 * 1000


.. questionnote::

   За сваки жанр приказати број различитих типова медија на којима су
   снимане песме тог жанра (приказати идентификатор жанра и број
   типова медија).

   
.. dbpetlja:: db_agregatne_muzika_zadaci_09
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT id_zanr, COUNT (DISTINCT id_format)
                   FROM kompozicija
                   GROUP BY id_zanr
