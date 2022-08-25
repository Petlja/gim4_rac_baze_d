.. -*- mode: rst -*-

Уписивање података прочитаних из базе
-------------------------------------

Постоји још један облик упита ``INSERT``, који омогућава да се
вредности које се уписују у табелу прочитају из базе коришћењем упита
``SELECT``.

.. code-block:: sql

   INSERT INTO tabela (kolona_1, ..., kolona_k)
   SELECT ...;


На пример, могли бисмо да направимо привремену табелу ``prosek`` са
колонама ``predmet_id``, ``naziv``, ``razred``, ``prosek`` и затим је
попунимо коришћењем следећег упита:

.. code-block:: sql

   INSERT INTO prosek (predmet_id, naziv, razred, prosek)
   SELECT p.id, p.naziv, p.razred, AVG(o.ocena)
   FROM predmet p JOIN
        ocena o ON p.id = o.id_predmet
   GROUP BY p.id;

Ово можемо да искористимо и да у једном кораку упишемо оцену Аници Павловић.

.. code-block:: sql
                
   INSERT INTO ocena (id_ucenik, id_predmet, datum, ocena, vrsta)
   SELECT *, '2020-10-01', 5, 'контролна вежба' 
   FROM
      (SELECT id
       FROM ucenik
       WHERE ime = 'Аница' AND prezime = 'Павловић' AND razred = 4 AND odeljenje = 2), 
      (SELECT id
       FROM predmet
       WHERE naziv = 'Математика' AND razred = 4);

У клаузули ``FROM`` наводе се две табеле које су обе резултат
угнежђених упита и имају по један ред и једну колону. Гради се њихов
Декартов производ и тако се добија табела која садржи само један ред,
који је уређени пар јединственог идентификатора ученице Анице Павловић
и јединственог идентификатора предмета математика у четвртом разреду.
Ти подаци се читају помоћу спољашњег ``SELECT *``, додају им се датум,
оцена и врста и онда се тако добијена врста уписује у табелу оцена
помоћу ``INSERT INTO``.

Упоредите овај поступак са оним наведеним на претходној страни.

Вежба
.....

Покушај да наредни упит напишеш самостално.

.. questionnote::

   Напиши упит који ученику Јовану Миленковићу из одељења I2 уписује
   оцену 4 на усменом одговору (врста оцене је 'усмени одговор') из српског
   језика 23. јануара 2021. године. Идентификатор ученика и предмета
   прочитати упитом ``SELECT``.

   
.. dbpetlja:: db_upisivanje_procitanog_01
   :dbfile: dnevnik.sql
   :solutionquery: INSERT INTO ocena (id_ucenik, id_predmet, datum, ocena, vrsta)
                   SELECT *, '2020-01-23', 4, 'усмени одговор' FROM
                   (SELECT id
                    FROM ucenik
                    WHERE ime = 'Јован' AND prezime = 'Миленковић' AND razred = 1 AND odeljenje = 2), 
                   (SELECT id
                    FROM predmet
                    WHERE naziv = 'Српски језик' AND razred = 1);
   :checkquery: SELECT * FROM ocena WHERE id_ucenik IN (SELECT id FROM ucenik WHERE ime='Јован' AND prezime='Миленковић')
