Угнежђени упити -- музика
.........................

.. questionnote::

   Приказати дигитални формат који је доминантан (највише бајтова је у
   том формату).

.. code-block:: sql

   SELECT naziv, MAX(velicina)
   FROM (SELECT format.naziv, SUM(velicina) AS ukupno
         FROM kompozicija JOIN
              format ON kompozicija.id_format = format.id_format);

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv", "MAX(velicina)"
   :align: left

   "MPEG audio file", "117386255350"

.. questionnote::

   Одредити назив плејлисте на којој има највише песама.

.. code-block:: sql

   SELECT naziv, MAX(Count)
   FROM (SELECT plejlista.naziv, COUNT(*) AS Count
         FROM plejlista_kompozicija JOIN
              plejlista ON plejlista.id_plejlista = plejlista_kompozicija.id_plejlista
         GROUP BY plejlista.id_plejlista);

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv", "MAX(Count)"
   :align: left

   "Music", "3290"

.. questionnote::

   Приказати називе свих извођача који су снимали блуз (*Blues*)
   композиције.

.. code-block:: sql

   SELECT naziv
   FROM izvodjac
   WHERE EXISTS (SELECT *
                 FROM kompozicija JOIN
                      album ON kompozicija.id_album = album.id_album JOIN
                      zanr ON kompozicija.id_zanr = zanr.id_zanr
                 WHERE album.id_izvodjac = izvodjac.id_izvodjac AND zanr.naziv = 'Blues');

Извршавањем упита добија се следећи резултат:

.. csv-table::
   :header:  "naziv"
   :align: left

   "Buddy Guy"
   "Eric Clapton"
   "Iron Maiden"
   "Stevie Ray Vaughan & Double Trouble"
   "The Black Crowes"

