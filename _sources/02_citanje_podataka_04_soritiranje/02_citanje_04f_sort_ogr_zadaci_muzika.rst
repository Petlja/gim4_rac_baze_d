Сортирање и ограничавање - музика
---------------------------------

У наставку ћемо приказати неколико упита над базом продавнице музичких
композиција.

.. questionnote::

   Приказати податке о три композиције које заузимају највише бајтова.

.. code-block:: sql

   SELECT *
   FROM kompozicija
   ORDER BY velicina DESC
   LIMIT 3;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id_kompozicija", "naziv", "id_album", "id_format", "id_zanr", "trajanje", "velicina", "cena"
   :align: left

   "3224", "Through a Looking Glass", "229", "3", "21", "5088838", "1059546140", "1.99"
   "2820", "Occupation / Precipice", "227", "3", "19", "5286953", "1054423946", "1.99"
   "3236", "The Young Lords", "253", "3", "20", "2863571", "587051735", "1.99"

.. questionnote::

   Приказати податке о композицијама уређене по степену компресије
   (броју бајтова по једној секунди).

.. code-block:: sql

   SELECT *, velicina / (trajanje / 1000) AS kompresija
   FROM kompozicija
   ORDER BY kompresija DESC
   LIMIT 3;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id_kompozicija", "naziv", "id_album", "id_format", "id_zanr", "trajanje", "velicina", "cena", "kompresija"
   :align: left

   "2844", "Better Halves", "228", "3", "21", "2573031", "549353481", "1.99", "213506"
   "3179", "Sexual Harassment", "250", "3", "19", "1294541", "273069146", "1.99", "211027"
   "2832", "The Woman King", "227", "3", "18", "2626376", "552893447", "1.99", "210545"

.. questionnote::

   Приказати све различите албуме тј. њихове идентификаторе на којима
   се јављају композиције дуже од 10 минута.

.. code-block:: sql

   SELECT DISTINCT id_album
   FROM kompozicija
   WHERE trajanje >= 10 * 60 * 1000;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id_album"
   :align: left

   "16"
   "30"
   "31"
   "35"
   "43"
   ...


Вежба
.....
   
Покушајте да самостално напишете наредних неколико упита.

.. questionnote::

   Приказати списак назива свих албума сортирано по називима албума у
   абецедном реду.

.. dbpetlja:: db_sortiranje_zadaci_muzika_01
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT naziv
                   FROM album
                   ORDER BY naziv
   

.. questionnote::

   Приказати податке о свим купцима из САД сортирано по називу града
   из којег долазе.

.. dbpetlja:: db_sortiranje_zadaci_muzika_02
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT *
                   FROM kupac
                   WHERE drzava = 'USA'
                   ORDER BY grad

                   
.. questionnote::

   Приказати имена, презимена и датуме рођења три најмлађа запослена у
   компанији.
   
.. dbpetlja:: db_sortiranje_zadaci_muzika_03
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT ime, prezime, datum_rodjenja
                   FROM zaposleni
                   ORDER BY datum_rodjenja DESC
                   LIMIT 3

.. questionnote::

   Исписати називе различитих држава из којих долазе купци.
   
.. dbpetlja:: db_sortiranje_zadaci_muzika_04
   :dbfile: music.sql
   :showresult:
   :solutionquery: SELECT DISTINCT drzava
                   FROM kupac

                   
