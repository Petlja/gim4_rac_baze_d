.. -*- mode: rst -*-

Сортирање и ограничавање - задаци (дневник)
...........................................

Покушај самостално да урадиш наредних неколико задатака. 
Решења можеш да тестираш овде, а можеш задатке да урадиш и у систему SQLite Studio.

.. questionnote::

   Прикажи сва различита мушка имена која почињу на слово ``M``.

.. dbpetlja:: db_sortiranje_zadaci_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT DISTINCT ime
                   FROM ucenik
                   WHERE pol = 'м' AND ime LIKE 'М%'
   :showresult:

.. questionnote::

   Прикажи списак првих 10 различитих презимена у азбучном редоследу.

.. dbpetlja:: db_sortiranje_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT DISTINCT prezime
                   FROM ucenik
                   ORDER BY prezime
                   LIMIT 10
   :showresult:

.. questionnote::

   Прикажи податке о свим оценама на писменим задацима сортиране
   опадајући по оцени.

.. dbpetlja:: db_sortiranje_zadaci_03
   :dbfile: dnevnik.sql
   :solutionquery: SELECT *
                   FROM ocena
                   WHERE vrsta = 'писмени задатак'
                   ORDER BY ocena DESC
   :showresult:
