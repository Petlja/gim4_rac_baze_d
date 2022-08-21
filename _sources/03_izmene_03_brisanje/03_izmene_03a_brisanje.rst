.. -*- mode: rst -*-

Брисање података
----------------

Редови из табеле се могу обрисати упитима ``DELETE``. Њихов општи облик је

.. code-block:: sql

   DELETE FROM naziv_tabele
   WHERE uslov;

Обрати пажњу на то да се не наводи које колоне се бришу, јер се увек
бришу цели редови (нема потребе и није исправно наводити ``DELETE * FROM``). 
Уколико се услов ``WHERE`` не наведе, биће обрисани сви редови,
тј. цела табела ће бити испражњена, што често није оно што желимо.

.. questionnote::

   Обрисати све оцене из табеле оцена које одговарају ученику са
   идентификатором 123.

.. code-block:: sql

   DELETE FROM ocena
   WHERE id_ucenik = 123;


.. questionnote::

   Обрисати све изостанке које је направио ученик Лав Грујић из IV3.

За разлику од претходног, у овом упиту морамо да прочитамо
идентификатор ученика из базе.


.. code-block:: sql

   DELETE FROM izostanak
   WHERE id_ucenik = (SELECT id
                      FROM ucenik
                      WHERE ime = 'Лав' AND prezime = 'Грујић' AND
                            razred = 4 AND odeljenje = 3);

Вежба
.....

Покушај да неколико наредних упита реализујеш самостално.

.. questionnote::

   Министарство је одлучило да се све јединице које су ђаци добили
   пониште (због ванредне ситуације). Напиши упит којим се све оне
   бришу из базе.

.. dbpetlja:: db_brisanje_01
   :dbfile: dnevnik.sql
   :solutionquery: DELETE FROM ocena
                   WHERE ocena = 1
   :checkquery: SELECT * FROM ocena

.. questionnote::

   Обрисати из базе све податке о оценама из математике (у свим
   разредима).

.. dbpetlja:: db_brisanje_02
   :dbfile: dnevnik.sql
   :solutionquery: DELETE FROM ocena
                   WHERE id_predmet IN (SELECT id
                                        FROM predmet
                                        WHERE naziv = 'Математика')
   :checkquery: SELECT * FROM ocena
                
