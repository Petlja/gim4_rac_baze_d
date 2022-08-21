.. -*- mode: rst -*-

Изрази и функције - задаци (дневник)
....................................

Покушај самостално да урадиш наредних неколико задатака. 
Решења можеш да тестираш овде, а можеш задатке да урадиш и у систему SQLite Studio.

.. questionnote::

   Приказати имена и презимена ученика и пол (уместо ``м`` и ``ж``
   треба да пише ``мушки`` односно ``женски``).

.. dbpetlja:: db_izrazi_vezba_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT ime, prezime,
                          CASE
                               WHEN pol = 'м' THEN 'мушки'
                               WHEN pol = 'ж' THEN 'женски'
                          END AS pol
                   FROM ucenik
   :showresult:               

.. questionnote::
   
   Приказати имена и презимена свих ученика чије име и презиме почиње
   на исто слово (нпр. ``Петар Петровић``, ``Јована Јанковић`` и
   слично).

.. dbpetlja:: db_izrazi_vezba_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT ime, prezime
                   FROM ucenik
                   WHERE substr(ime, 1, 1) = substr(prezime, 1, 1)
   :showresult:               

.. questionnote::

   За сваки предмет приказати шифру која се гради од прва три слова
   назива предмета и разреда у ком се предмет предаје (нпр. за
   математику у првом разреду, шифра је ``мат1``).

.. dbpetlja:: db_izrazi_vezba_03
   :dbfile: dnevnik.sql
   :solutionquery: SELECT substr(naziv, 1, 3) || razred AS sifra
                   FROM predmet
   :showresult:               


.. questionnote::

   Коришћењем функције за издвајање месеца из датума, приказати све
   податке о ученицима рођеним у фебруару месецу.

.. dbpetlja:: db_izrazi_vezba_04
   :dbfile: dnevnik.sql
   :solutionquery: SELECT *
                   FROM ucenik
                   WHERE strftime('%m', datum_rodjenja) = '02';
   :showresult:               
