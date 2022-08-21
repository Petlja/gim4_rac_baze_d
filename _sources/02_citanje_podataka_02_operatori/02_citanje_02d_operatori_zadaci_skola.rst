.. -*- mode: rst -*-

Логички и релацијски оператори -- задаци (дневник)
..................................................

Покушај сада да самостално решиш наредних неколико задатака.

Решења можеш да тестираш овде, а можеш све задатке да урадиш и у систему SQLite Studio. 
Непоходно је, наравно, да је систем преузет на рачунар и је додата база података са називом 
*dnevnik* како је описано у ранијим лекцијама. 
 
Упити се пишу након што се кликне на креирану базу у прозору ``Databases`` и потом изабере команда 
менија ``Tools → Open SQL Editor``. Када се напише упит, кликне се на дугме ``Execute query (F9)`` 
(плави троуглић).

Савет је да се у прозору ``Databases`` увек прво провере тачни називи табела. 

.. image:: ../../_images/dnevnik.png
   :width: 400
   :align: center
   
Често ће нам код упита бити потребно да знамо и тачне називе колона, а понекад нам је значајно и да 
знамо како су неки подаци записани у бази (да ли су ћирилична слова, да ли су латинична, 
да ли имена и називи почињу великим словом, итд), па је добро да се пре писања коначног 
решења задатка прво напише и изврши основни SELECT упит који приказује све податке из табеле 
коју треба да користимо у решењу задатка.


.. questionnote::

   Приказати имена свих девојчица у одељењу III1.
 
.. dbpetlja:: db_operatori_zadaci_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT ime
                   FROM ucenik
                   WHERE pol = 'ж' AND razred = 3 AND odeljenje = 1
   :showresult:


.. questionnote::

   Приказати сва мушка имена ученика која се завршавају словом ``ан``.

.. dbpetlja:: db_operatori_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT ime
                   FROM ucenik
                   WHERE pol = 'м' AND ime LIKE '%ан'
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
