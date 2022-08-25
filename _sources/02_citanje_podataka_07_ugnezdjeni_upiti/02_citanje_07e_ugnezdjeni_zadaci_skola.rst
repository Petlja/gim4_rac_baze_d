.. -*- mode: rst -*-

Угнежђени упити -- задаци (дневник)
...................................

Угнежђени подупити су, без сумње, најкомпликованији концепт језика SQL
који ћете срести у овом курсу и користе се само у случају потребе да
се изврше прилично напредне анализе података. Стога се овакви упити
могу сматрати материјалом за ученике који имају жељу да се у
будућности озбиљније баве програмирањем. У наставку се налази неколико
задатака који се могу решити коришћењем угнежђених подупита. Можете
покушати да их самостално решите, а иза сваког задатка дато је и
поступно објашњено решење.

.. questionnote::

   Рођендански парадокс нам говори да је у одељењу од 23 ученика
   вероватноћа да два ученика имају исти датум рођења преко
   50%. Исписати она одељења у којима постоји више ученика који су
   рођени у истом дану, као и највећи број ученика који су рођени у
   једном дану.

Покушај прво да самостално решиш задатак.
   
.. dbpetlja:: db_ugnezdjeni_upiti_zadaci_01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT razred, odeljenje, MAX(broj) AS max_broj 
                   FROM (SELECT razred, odeljenje, datum_rodjenja, COUNT(datum_rodjenja) AS broj
                         FROM ucenik
                         GROUP BY datum_rodjenja, razred, odeljenje)
                   GROUP BY razred, odeljenje
                   HAVING max_broj > 1
                   ORDER BY razred, odeljenje;

У наставку је описано и решење.

У првој фази решавања задатка ћемо за сваки датум, разред и одељење
израчунати број ученика тог одељења који су рођени на тај датум.

.. code-block:: sql

   SELECT razred, odeljenje, datum_rodjenja, COUNT(datum_rodjenja) AS broj
   FROM ucenik
   GROUP BY datum_rodjenja, razred, odeljenje

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "razred", "odeljenje", "datum_rodjenja", "broj"
   :align: left

   "4", "3", "2003-03-01", "1"
   "4", "2", "2003-03-02", "1"
   "4", "1", "2003-03-03", "1"
   "4", "3", "2003-03-06", "1"
   "4", "1", "2003-03-07", "1"
   ..., ..., ..., ...

У другој фази из те табеле одређујемо максимални број за свако
одељење, издвајајући само она одељења код којих је тај максимални број
већи од 1.

.. code-block:: sql

   SELECT razred, odeljenje, MAX(broj) AS max_broj 
   FROM (SELECT razred, odeljenje, datum_rodjenja, COUNT(datum_rodjenja) AS broj
         FROM ucenik
         GROUP BY datum_rodjenja, razred, odeljenje)
   GROUP BY razred, odeljenje
   HAVING max_broj > 1
   ORDER BY razred, odeljenje;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "razred", "odeljenje", "max_broj"
   :align: left

   "1", "1", "2"
   "1", "2", "3"
   "2", "1", "2"
   "2", "2", "2"
   "2", "3", "2"
   ..., ..., ...

.. questionnote::

   Приказати број оцена из математике свих ученика.

Покушај прво да самостално решиш задатак.
   
.. dbpetlja:: db_ugnezdjeni_upiti_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.id, u.ime, u.prezime, COUNT(*) AS broj_ocena_iz_matematike
                   FROM ucenik u JOIN
                        ocena o ON u.id = o.id_ucenik
                   WHERE o.id_predmet IN (SELECT id FROM predmet WHERE naziv = 'Математика')
                   GROUP BY u.id;

У наставку је описано и решење.

Важан корак у решењу је да се издвоје само оне оцене које су из
математике. Један начин да то урадимо је да у првој фази, у засебном
упиту, издвојимо идентификаторе свих предмета који имају назив
``Математика`` (јер се математика у сваком разреду бележи као посебан
предмет).

.. code-block:: sql

   SELECT id
   FROM predmet
   WHERE naziv = 'Математика'

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id"
   :align: left

   "1"
   "4"
   "8"
   "9"

Тај скуп идентификатора можемо употребити за филтрирање табеле свих
оцена (коришћењем оператора ``IN``). Када се добије табела која садржи
само оцене из математике, задатак се решава рутински, коришћењем
груписања (по идентификатору ученика) и пребројавањем елемената у
свакој групи.
   
.. code-block:: sql
                
   SELECT u.id, u.ime, u.prezime, COUNT(*) AS broj_ocena_iz_matematike
   FROM ucenik u
        JOIN ocena o ON u.id = o.id_ucenik
   WHERE o.id_predmet IN (SELECT id FROM predmet WHERE naziv = 'Математика')
   GROUP BY u.id;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "ime", "prezime", "broj_ocena_iz_matematike"
   :align: left

   "1", "Петар", "Петровић", "6"
   "2", "Милица", "Јовановић", "6"
   "3", "Лидија", "Петровић", "6"
   "4", "Петар", "Миловановић", "4"
   "5", "Ана", "Пекић", "4"
   ..., ..., ..., ...

Нагласимо да ово није једино могуће решење (на пример, задатак се
могао решити тако што би се спојиле табеле оцена и предмета и затим
издвојиле само оне врсте код којих је назив предмета једнак
``Математика``).
   
.. questionnote::

   Приказати податке о ученицима који би по тренутним оценама имали
   закључену петицу из српског језика. Уредити списак по разредима и
   одељењима, а затим по азбучном реду.

Покушај прво да самостално решиш задатак.
   
.. dbpetlja:: db_ugnezdjeni_upiti_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.id, u.ime, u.prezime, u.razred, u.odeljenje
                   FROM ocena o JOIN
                        ucenik u ON o.id_ucenik = u.id
                   WHERE id_predmet IN (SELECT id
                                        FROM predmet
                                        WHERE naziv = 'Српски језик')
                   GROUP BY u.id
                   HAVING AVG(ocena) >= 4.5
                   ORDER BY razred, odeljenje, prezime, ime;

У наставку је описано и једно решење. Задатак је прилично сличан
претходном, јер захтева да се издвоје само оне оцене које су из
српског језика. То можемо поново урадити тако што у засебном подупиту
издвојимо идентификаторе свих предмета који одговарају настави српског
језика.
   
.. code-block:: sql
   
   SELECT u.id, u.ime, u.prezime, u.razred, u.odeljenje
   FROM ocena o JOIN
        ucenik u ON o.id_ucenik = u.id
   WHERE id_predmet IN (SELECT id
                        FROM predmet
                        WHERE naziv = 'Српски језик')
   GROUP BY u.id
   HAVING AVG(ocena) >= 4.5
   ORDER BY razred, odeljenje, prezime, ime;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "ime", "prezime", "razred", "odeljenje"
   :align: left

   "21", "Анђелија", "Богдановић", "1", "1"
   "42", "Весна", "Граховац", "1", "2"
   "46", "Весна", "Нешић", "1", "2"
   "82", "Виолета", "Милојевић", "1", "3"
   "76", "Новак", "Радивојевић", "1", "3"
   ..., ..., ..., ..., ...

.. questionnote::

   Приказати број изостанака свих ученика који би по тренутним оценама
   имали закључену петицу из математике.


Покушај прво да самостално решиш задатак.
   
.. dbpetlja:: db_ugnezdjeni_upiti_zadaci_02
   :dbfile: dnevnik.sql
   :solutionquery: SELECT u.id, u.ime, u.prezime, COUNT(*) AS broj_izostanaka
                   FROM izostanak i JOIN 
                        ucenik u ON i.id_ucenik = u.id
                   WHERE u.id IN (SELECT id_ucenik
                                  FROM ocena
                                  WHERE id_predmet IN (SELECT id
                                                       FROM predmet
                                                       WHERE naziv = 'Математика')
                                  GROUP BY id_ucenik
                                  HAVING AVG(ocena) >= 4.5)
                   GROUP BY u.id;


У наставку је описано и једно решење. Идеја је да у угнежђеном
подупиту одредимо идентификаторе свих ученика који би по тренутним
оценама имали закључену оцену 5 из математике. Интересантно, тај
угнежђени подупит има свој угнежђени подупит у ком издвајамо све
идентификаторе предмета математике.

.. code-block:: sql

   SELECT id_ucenik
   FROM ocena
   WHERE id_predmet IN (SELECT id
                        FROM predmet
                        WHERE naziv = 'Математика')
   GROUP BY id_ucenik
   HAVING AVG(ocena) >= 4.5;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id_ucenik"
   :align: left

   "40"
   "45"
   "46"
   "47"
   "50"
   ...

Тај скуп идентификатора можемо сада употребити да урадимо филтрирање
табеле изостанака и да добијемо само изостанке тих ученика. Након
тога, изостанке једноставно можемо пребројати коришћењем груписања
свих на основу изостанака и на основу идентификатора ученика.
    
.. code-block:: sql
   
   SELECT u.id, u.ime, u.prezime, COUNT(*) AS broj_izostanaka
   FROM izostanak i JOIN 
        ucenik u ON i.id_ucenik = u.id
   WHERE u.id IN (SELECT id_ucenik
                  FROM ocena
                  WHERE id_predmet IN (SELECT id
                                       FROM predmet
                                       WHERE naziv = 'Математика')
                  GROUP BY id_ucenik
                  HAVING AVG(ocena) >= 4.5)
   GROUP BY u.id;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "ime", "prezime", "broj_izostanaka"
   :align: left

   "40", "Емилија", "Рељин", "68"
   "45", "Николај", "Кнежевић", "32"
   "46", "Весна", "Нешић", "48"
   "47", "Душанка", "Петровић", "17"
   "50", "Петар", "Милић", "6"
   ..., ..., ..., ...

