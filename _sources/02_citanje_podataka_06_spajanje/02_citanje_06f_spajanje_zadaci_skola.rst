.. -*- mode: rst -*-

Спајање - задаци (дневник)
............................

У систему SQLite Studio упити се пишу након што се кликне на креирану базу *dnevnik* у прозору 
Databases и потом изабере команда менија ``Tools → Open SQL Editor``. Када се напише упит, 
кликне се на дугме ``Execute query (F9)`` (плави троуглић). 

Савет је да се у прозору ``Databases`` увек прво провере тачни називи табела, 
као и колона. Посебно је важно да проверимо називе страног кључа и примарног 
кључа који му одговара у другој табели када желимо да извршимо спајање, тј. да 
прикажемо податке из више табела које су повезане.  

.. figure:: ../../_images/dnevnik.png
   :width: 500
   :align: center
   :alt: Логотип система SQLite
   :class: screenshot-shadow

.. questionnote::

   Приказати у читљивом формату све оцене на контролним вежбама
   ученика одељења I2. Приказати име и презиме ученика, назив
   предмета, датум добијања оцене и оцену која је добијена.

.. dbpetlja:: db_spajanje_zadaci_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.ime, u.prezime, p.naziv, o.datum, o.ocena
                   FROM ocena o
                        JOIN ucenik u ON o.id_ucenik = u.id
                        JOIN predmet p ON o.id_predmet = p.id
                   WHERE u.razred = 1 AND u.odeljenje = 2 AND o.vrsta = 'контролна вежба'
   :showresult:
   
.. questionnote::
   
   Приказати просечну оцену на сваком писменом задатку у сваком
   одељењу (рачунати само писмене задатке које је истовремено радило
   бар 25 ученика). Приказати разред, одељење, назив предмета, датум
   писменог, просечну оцену и број ученика који су радили писмени.

.. dbpetlja:: db_spajanje_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.razred, u.odeljenje, p.naziv, o.datum, round(AVG(o.ocena), 2) AS prosek, COUNT(*) as broj
                   FROM ocena o JOIN
                        predmet p ON o.id_predmet = p.id JOIN
                        ucenik u ON o.id_ucenik = u.id
                   WHERE o.vrsta = 'писмени задатак'
                   GROUP BY u.razred, u.odeljenje, p.id, o.datum
                   HAVING broj >= 25
   :showresult:
   
.. questionnote::
   
   За сваки предмет приказати месечни преглед броја петица (списак
   уредити по називима предмета у азбучном редоследу, а за сваки
   предмет, по месецима, растуће). Приказати назив предмета, разред,
   месец и број петица.


.. dbpetlja:: db_spajanje_zadaci_03
   :dbfile: dnevnik.sql
   :solutionquery: SELECT p.naziv, p.razred, strftime('%m', o.datum) AS mesec, COUNT(*) AS broj
                   FROM ocena o JOIN
                        predmet p ON o.id_predmet = p.id
                   WHERE o.ocena = 5
                   GROUP BY p.id, mesec
                   ORDER BY p.naziv, mesec
   :showresult:

.. questionnote::
   
   Ситуација је алармантна када ученици неког одељења у неком месецу
   направе 5 или више неоправданих изостанака. Приказати све такве
   случајеве. Приказати разред, одељење, месец и број неоправданих
   изостанака.

.. dbpetlja:: db_spajanje_zadaci_04
   :dbfile: dnevnik.sql
   :solutionquery: SELECT razred, odeljenje, strftime('%m', datum) AS mesec, COUNT(*) AS broj
                   FROM izostanak i JOIN
                        ucenik u ON i.id_ucenik = u.id
                   WHERE status = 'неоправдан'
                   GROUP BY mesec, razred, odeljenje
                   HAVING broj >= 5
   :showresult:
	
.. questionnote::
   
   За сваког ученика приказати просечну оцену из сваког предмета за
   који је добио бар две оцене (приказати имена и презимена ученика,
   називе предмета и просечне оцене заокружене на две децимале).

.. dbpetlja:: db_spajanje_zadaci_05
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.ime, u.prezime, p.naziv, round(AVG(ocena), 2) AS prosek
                   FROM ocena o JOIN
                        ucenik u ON o.id_ucenik = u.id JOIN
                        predmet p ON o.id_predmet = p.id
                   GROUP BY u.id, p.id
                   HAVING COUNT(*) >= 2
   :showresult:
	
.. questionnote::
   
   Рођендански парадокс нам говори да је у одељењу од 23 ученика
   вероватноћа да два ученика имају исти датум рођења скоро 50%. Зато
   се може очекивати да у већини одељења постоји бар два ученика
   рођена истог датума. Исписати све парове ученика из истог одељења
   рођених истог дана. Приказати датум, разред, одељење, имена и
   презимена оба ученика.

.. dbpetlja:: db_spajanje_zadaci_06
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u1.datum_rodjenja, u1.razred, u1.odeljenje,
                          u1.ime, u1.prezime,
                          u2.ime, u2.prezime
                   FROM ucenik AS u1 JOIN 
                        ucenik AS u2 ON 
                            u1.razred = u2.razred AND u1.odeljenje = u2.odeljenje AND
                            u1.datum_rodjenja = u2.datum_rodjenja AND u1.id < u2.id
                   ORDER BY u1.razred, u1.odeljenje
   :showresult:

.. questionnote::
   
   Приказати број оцена из сваког предмета, укључујући и оне предмете
   из којих не постоји ни једна оцена. Резултат сортирати опадајуће по
   броју оцена. Приказати назив предмета, разред и број оцена.

.. dbpetlja:: db_spajanje_zadaci_07
   :dbfile: dnevnik.sql
   :solutionquery: SELECT naziv, razred, COUNT(ocena) AS broj_ocena
                   FROM predmet LEFT JOIN
                        ocena ON predmet.id = ocena.id_predmet
                   GROUP BY predmet.id
                   ORDER BY broj_ocena DESC
   :showresult:
   
.. questionnote::
   
   За сваког ученика приказати број оцена из рачунарства и информатике
   (за ученике који нису још добили оцене из тог предмета приказати
   нулу).
                   
.. dbpetlja:: db_spajanje_zadaci_08
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.ime, u.prezime, COUNT(ocena)
                   FROM ucenik u LEFT JOIN
                        (ocena o JOIN
                         predmet p ON p.id = o.id_predmet AND p.naziv = 'Рачунарство и информатика') ON u.id = id_ucenik
                   GROUP BY u.id
   :showresult: