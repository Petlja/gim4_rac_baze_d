.. -*- mode: rst -*-
   
Провера постојања (EXISTS)
--------------------------

Некада желимо да издвојимо само оне врсте за које корелисани подупит
враћа непразну (или празну) табелу тј. ако се утврди да постоји (или
да не постоји) нека врста која задовољава услов корелисаног подупита.
За то се може користити услов ``EXISTS`` (или ``NOT EXISTS``, који је
заправо само негација услова ``EXISTS``).

Корелисани подупити превазилазе домет овог курса. За оне који желе да знају више, 
приказаћемо неколико примера.

.. questionnote::

   Приказати имена ученика који имају неоправдане изостанке.
   
.. code-block:: sql
                
   SELECT id, ime, prezime
   FROM ucenik
   WHERE EXISTS (SELECT *
                 FROM izostanak
                 WHERE izostanak.id_ucenik = ucenik.id AND status = 'неоправдан');

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "ime", "prezime"
   :align: left

   "1", "Петар", "Петровић"
   "5", "Ана", "Пекић"
   "6", "Јован", "Миленковић"
   "8", "Гордана", "Сарић"
   "9", "Вања", "Савић"
   ..., ..., ...

Наравно, постоје и други начини да се овај упит реализује. На пример,
можемо да спојимо табелу ученика и табелу изостанака, групишемо изостанке
по свим ученицима, и прикажемо имена и презимена за сваку групу
(приметимо да овде не примењујемо ни једну агрегатну функцију на
формиране групе).

.. code-block:: sql

   SELECT ucenik.id, ime, prezime
   FROM ucenik JOIN
        izostanak on izostanak.id_ucenik = ucenik.id
   WHERE status = 'неоправдан'
   GROUP BY ucenik.id;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "ime", "prezime"
   :align: left

   "1", "Петар", "Петровић"
   "5", "Ана", "Пекић"
   "6", "Јован", "Миленковић"
   "8", "Гордана", "Сарић"
   "9", "Вања", "Савић"
   ..., ..., ...

|

У наредном проблему можемо да искористимо услов непостојања ``NOT
EXISTS``.
                 
.. questionnote::
           
   Приказати имена ученика који немају нерегулисаних изостанака.
   
.. code-block:: sql
                
   SELECT id, ime, prezime
   FROM ucenik
   WHERE NOT EXISTS (SELECT *
                     FROM izostanak
                     WHERE izostanak.id_ucenik = ucenik.id AND status = 'нерегулисан');

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "ime", "prezime"
   :align: left

   "1", "Петар", "Петровић"
   "2", "Милица", "Јовановић"
   "3", "Лидија", "Петровић"
   "5", "Ана", "Пекић"
   "6", "Јован", "Миленковић"
   ..., ..., ...

   
Вежба
.....

Покушај да самостално напишеш наредни упит.

.. questionnote::

   Прикажи идентификаторе и називе предмета из којих је уписана бар
   нека оцена на писменом задатку (употреби услов ``EXISTS``).
   
.. dbpetlja:: db_ugnezdjeni_upiti_exists_01
   :dbfile: dnevnik.sql
   :showresult:
   :solutionquery: SELECT id, naziv
                   FROM predmet p
                   WHERE EXISTS (SELECT *
                                 FROM ocena o
                                 WHERE o.vrsta = 'писмени задатак' AND
                                       o.id_predmet = p.id)

Нагласимо да је задатак могуће решити и без угнежђених подупита и
услова ``EXISTS``, обичним спајањем.

.. code-block:: sql

   SELECT DISTINCT p.id, p.naziv
   FROM predmet p JOIN
        ocena o ON p.id = o.id_predmet
   WHERE vrsta = 'писмени задатак'

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "id", "naziv"
   :align: left

   "1", "Математика"
   "2", "Српски језик"

