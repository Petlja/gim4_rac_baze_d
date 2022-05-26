.. -*- mode: rst -*-

Агрегатне функције и груписање -- задаци (дневник)
--------------------------------------------------

.. questionnote::

   Приказати укупан број оправданих изостанака које је направио ученик
   са идентификатором 1 (колону назвати ``broj_izostanaka``).

.. dbpetlja:: db_agregatne_zadaci_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT COUNT(*) AS broj_izostanaka
                   FROM izostanak
                   WHERE id_ucenik = 1 AND status = 'оправдан'
   :showresult:
   :checkcolumnname:

.. questionnote::

   Приказати просечну оцену, заокружену на две децимале, на писменом
   задатку из математике одржаном 15. октобра 2020. (та математика има
   идентификатор 1).

.. dbpetlja:: db_agregatne_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT round(AVG(ocena), 2) AS prosek
                   FROM ocena
                   WHERE id_predmet = 1 AND datum = '2020-10-15' AND vrsta = 'писмени задатак'
   :showresult:

.. questionnote::

   За сваки датум у ком је направљен неки изостанак одредити укупан
   број направљених изостанака (колону назвати ``broj_izostanaka``).

.. dbpetlja:: db_agregatne_zadaci_03
   :dbfile: dnevnik.sql
   :solutionquery: SELECT datum, COUNT(*) AS broj_izostanaka
                   FROM izostanak
                   GROUP BY datum
   :showresult:
   :checkcolumnname:

.. questionnote::

   За сваки статус изостанака (оправдани, неоправдани, нерегулисани)
   одредити број таквих изостанака у мају 2021. године.

.. dbpetlja:: db_agregatne_zadaci_04
   :dbfile: dnevnik.sql
   :solutionquery: SELECT status, COUNT(*) AS broj
                   FROM izostanak
                   WHERE datum BETWEEN '2021-05-01' AND '2021-05-31'
                   GROUP BY status
   :showresult:

.. questionnote::

   За сваки статус изостанака одреди први и последњи датум када је
   такав изостанак направљен (колоне назвати ``prvi`` и
   ``poslednji``).

.. dbpetlja:: db_agregatne_zadaci_05
   :dbfile: dnevnik.sql
   :solutionquery: SELECT status, MIN(datum) AS prvi, MAX(datum) AS poslednji
                   FROM izostanak
                   GROUP BY status
   :showresult:
   :checkcolumnname:

.. questionnote::

   За сваки месец приказати број ученика рођених у том месецу (колоне
   назвати ``mesec`` и ``broj``).

.. dbpetlja:: db_agregatne_zadaci_06
   :dbfile: dnevnik.sql
   :solutionquery: SELECT strftime('%m', datum_rodjenja) AS mesec, COUNT(*) AS broj
                   FROM ucenik
                   GROUP BY mesec
   :showresult:
   :checkcolumnname:

.. questionnote::

   За сваки месец у години y ком је неки ученик добио неку јединицу
   приказати број јединица које су ученици добили током тог месеца
   (колоне назвати ``mesec`` и ``broj``).

.. dbpetlja:: db_agregatne_zadaci_07
   :dbfile: dnevnik.sql
   :solutionquery: SELECT strftime('%m', datum) AS mesec, COUNT(*) AS broj
                   FROM ocena
                   WHERE ocena = 1
                   GROUP BY mesec
   :showresult:
   :checkcolumnname:
   
.. questionnote::

   Прикажи датуме у којима има неоправданих изостанака, али је то
   строго мање од 10 (уз сваки датум приказати и број изостанака).

.. dbpetlja:: db_agregatne_zadaci_08
   :dbfile: dnevnik.sql
   :solutionquery: SELECT datum, COUNT(*) AS broj
                   FROM izostanak
                   GROUP BY datum
                   HAVING broj < 10
   :showresult:

.. questionnote::

   Приказати све називе предмета који се предају током неколико
   разреда (приказати само називе).

   
.. dbpetlja:: db_agregatne_zadaci_09
   :dbfile: dnevnik.sql
   :solutionquery: SELECT naziv
                   FROM predmet
                   GROUP BY naziv
                   HAVING COUNT(*) > 1
   :showresult:
