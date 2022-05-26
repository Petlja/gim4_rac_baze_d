.. -*- mode: rst -*-

Спајање и груписање
-------------------

У овом делу не бавимо се новим могућностима језика `SQL`, већ само 
новим комбинацијама раније упознатих могућности.

.. questionnote::
                
   Приказати просечне оцене из свих предмета из првог разреда.

Јасно је да је потребно извршити груписање оцена из табеле оцена на
основу предмета (тј. њихових идентификатора) и затим израчунати
статистику (аритметичку средину) за сваку групу посебно. Проблем је то
што се захтева филтрирање предмета тако да се прикажу само просечне
оцене за предмете из првог разреда, а податак о разреду у ком се
предмет предаје се не налази у табели оцена, већ у табели
предмета. Стога је пре класичног груписања и израчунавања статистика
по групама потребно спојити табелу оцена и табелу предмета.
   
.. code-block:: sql

   SELECT naziv, round(AVG(ocena), 2) AS prosek
   FROM ocena
        JOIN predmet on ocena.id_predmet = predmet.id
   WHERE razred = 1
   GROUP BY predmet.id;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv", "prosek"
   :align: left

   "Математика", "3.41"
   "Српски језик", "3.61"
   "Рачунарство и информатика", "3.61"
   "Физика", "3.58"
   "Енглески језик", "3.63"
   ..., ...

.. questionnote::

   Приказати просечне оцене из свих предмета (уређене опадајуће по
   просечној оцени).

Овај упит је сличан претходном. Када бисмо се задовољили приказом
просечних оцена и идентификатора предмета, тада бисмо могли да применимо
само груписање и израчунавање просека група из табеле са
оценама. Међутим, пошто желимо да прикажемо називе предмета, а подаци
о њима се налазе у табели предмета, вршимо спајање две табеле.
   
.. code-block:: sql
                
   SELECT naziv, round(AVG(ocena), 2) AS prosek
   FROM ocena
        JOIN predmet on ocena.id_predmet = predmet.id
   GROUP BY predmet.id
   ORDER BY prosek DESC;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv", "prosek"
   :align: left

   "Изборни програми", "3.9"
   "Физика", "3.87"
   "Физичко васпитање", "3.86"
   "Психологија", "3.83"
   "Рачунарство и информатика", "3.82"
   ..., ...

Могуће је користити и клаузулу ``HAVING`` (подсетимо се, она служи за
филтрирање након груписања на основу израчунатих вредности статистика
група).
   
.. questionnote::
   
   Приказати називе предмета и просечне оцене на писменим задацима за
   све предмете код којих је просечна оцена на писменим задацима бар
   3,50.

.. code-block:: sql
                
   SELECT naziv, round(AVG(ocena), 2) AS prosek
   FROM ocena
        JOIN predmet ON ocena.id_predmet = predmet.id
   WHERE ocena.vrsta = 'писмени задатак'
   GROUP BY predmet.id
   HAVING prosek >= 3.50;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv", "prosek"
   :align: left

   "Српски језик", "3.98"

Вежба
.....

Покушај да наредне упите напишеш самостално.

.. questionnote::
   
   За свако одељење приказати укупан број неоправданих изостанака.

.. dbpetlja:: db_spajanje_i_grupisanje_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT razred, odeljenje, COUNT(*) AS broj
                   FROM izostanak i JOIN
                        ucenik u ON i.id_ucenik = u.id
                   WHERE status = 'неоправдан'
                   GROUP BY razred, odeljenje
                   
.. questionnote::
   
   Приказати просечну оцену (заокружено на две децимале) из математике за свако одељење.   

.. dbpetlja:: db_spajanje_i_grupisanje_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.razred, u.odeljenje, ROUND(AVG(ocena), 2) AS prosek
                   FROM ucenik u JOIN 
                        ocena o ON u.id = o.id_ucenik JOIN
                        predmet p ON p.id = o.id_predmet
                   WHERE p.naziv = 'Математика'
                   GROUP BY u.razred, u.odeljenje
