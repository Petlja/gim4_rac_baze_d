.. -*- mode: rst -*-

Пројекција и селекција -- задаци за вежбу (дневник)
---------------------------------------------------

Покушај самостално да решиш наредних неколико задатака.

.. questionnote::

   Напиши упит који из табеле ученика издваја ``id``, ``ime`` и
   ``prezime`` сваког ученика.

.. dbpetlja:: db_proj_restr_01
   :dbfile: dnevnik.sql
   :solutionquery:  SELECT id, ime, prezime
                    FROM ucenik
   :showresult:
   
.. questionnote::

   Напиши упит који из табеле изостанака приказује све податке о
   оправданим изостанцима.

.. dbpetlja:: db_proj_restr_02
   :dbfile: dnevnik.sql
   :solutionquery:  SELECT * FROM izostanak
                    WHERE status = 'оправдан'
   :showresult:

.. questionnote::

   Напиши упит који приказује назив и фонд часова сваког предмета из
   другог разреда.

.. dbpetlja:: db_proj_restr_03
   :dbfile: dnevnik.sql
   :solutionquery:     SELECT naziv, fond
                       FROM predmet
                       WHERE razred = 2
   :showresult:
