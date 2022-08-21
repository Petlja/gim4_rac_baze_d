.. -*- mode: rst -*-

Уклањање дупликата (DISTINCT)
-----------------------------

У неким случајевима желимо да елиминишемо дупликате из резултата
тј. желимо да добијемо само јединствене вредности унутар неке
колоне. То се постиже навођењем ``DISTINCT`` уз име колоне.

.. questionnote::

   Приказати сва различита имена ученика (без понављања).

.. code-block:: sql

   SELECT DISTINCT ime
   FROM ucenik;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "ime"
   :align: left

   "Петар"
   "Милица"
   "Лидија"
   "Ана"
   "Јован"
   ...

Ако бисмо желели да имена буду сортирана по азбучном реду, додали
бисмо клаузулу ``ORDER BY``.

.. code-block:: sql

   SELECT DISTINCT ime
   FROM ucenik
   ORDER BY ime;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "ime"
   :align: left

   "Адам"
   "Адријана"
   "Аида"
   "Алекса"
   "Александра"
   ...

Наравно, клаузула ``DISTICT`` може да се комбинује са селекцијом (клаузулом
``WHERE``).

.. questionnote::

   Приказати сва различита женска имена ученица школе. 

.. code-block:: sql

   SELECT DISTINCT ime
   FROM ucenik
   WHERE pol = 'ж';

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "ime"
   :align: left

   "Милица"
   "Лидија"
   "Ана"
   "Јована"
   "Гордана"
   ...

Као што се може претпоставити, ``DISTINCT`` је применљив на различите
типове података.
   
.. questionnote::

   Приказати све различите датуме у којима ученик са идентификатором 1
   има изостанке.

.. code-block:: sql

   SELECT DISTINCT datum
   FROM izostanak
   WHERE id_ucenik = 1;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "datum"
   :align: left

   "2020-10-01"
   "2020-10-16"
   "2020-12-08"
   "2021-02-11"
   "2021-02-16"
   ...

``DISTINCT`` може да се примени и на више колона.

.. questionnote::

   Приказати сва одељења у школи.


.. code-block:: sql

   SELECT DISTINCT razred, odeljenje
   FROM ucenik;

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "razred", "odeljenje"
   :align: left

   "1", "1"
   "2", "1"
   "1", "2"
   "3", "1"
   "1", "3"
   ..., ...

``DISTINCT`` се односи на пар који чини ознака разреда и ознака одељења.

Вежба
.....

Покушај да наредни упит напишеш самостално. Решење можеш да тестираш овде, 
а можеш задатак да урадиш и у систему SQLite Studio.

.. questionnote::

   Приказати све различите називе предмета.

   
.. dbpetlja:: db_uklanjanje_duplikata__01
   :dbfile: dnevnik.sql
   :solutionquery: SELECT DISTINCT naziv
                   FROM predmet
   :showresult:

