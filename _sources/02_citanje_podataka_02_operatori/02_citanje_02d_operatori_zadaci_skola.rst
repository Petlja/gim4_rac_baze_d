.. -*- mode: rst -*-

Логички и релацијски оператори -- задаци (дневник)
..................................................

Покушај сада да самостално решиш наредних неколико задатака.

.. questionnote::

   Приказати имена свих девојчица у одељењу III1.

.. dbpetlja:: db_operatori_zadaci_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT ime
                   FROM ucenik
                   WHERE pol = 'ж' AND razred = 3 AND odeljenje = 1
   :showresult:


.. questionnote::

   Приказати сва мушка имена ученика која се завршавају словом ``а``.

.. dbpetlja:: db_operatori_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT ime
                   FROM ucenik
                   WHERE pol = 'м' AND ime LIKE '%а'
   :showresult:


.. questionnote::

   Приказати податке о свим ученицима рођеним у априлу 2006.

.. dbpetlja:: db_operatori_zadaci_03
   :dbfile: dnevnik.sql
   :solutionquery: SELECT *
                   FROM ucenik
                   WHERE datum_rodjenja BETWEEN '2006-04-01' AND '2006-04-30'
   :showresult:


.. questionnote::

   Приказати податке о свим ученицима који су рођени у зимским
   месецима (у децембру, јануару или фебруару).

.. dbpetlja:: db_operatori_zadaci_04
   :dbfile: dnevnik.sql
   :solutionquery: SELECT *
                   FROM ucenik
                   WHERE datum_rodjenja LIKE '%-12-%' OR
                         datum_rodjenja LIKE '%-01-%' OR
                         datum_rodjenja LIKE '%-02-%'
   :showresult:


.. questionnote::

   Приказати сва имена ученика која почињу самогласником.

.. dbpetlja:: db_operatori_zadaci_05
   :dbfile: dnevnik.sql
   :solutionquery: SELECT *
                   FROM ucenik
                   WHERE ime LIKE 'А%' OR
                         ime LIKE 'Е%' OR
                         ime LIKE 'И%' OR
                         ime LIKE 'О%' OR
                         ime LIKE 'У%'
   :showresult:
