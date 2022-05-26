Угнежђени упити - квиз
======================


.. quizq::

    .. mchoice:: ugnezdeni_sta
        :answer_a: Комбиновање резултата два независна упита.
        :answer_b: Упит над више табела.
        :answer_c: Условно извршавање упита.
        :answer_d: Упит над резултатом другог упита.
        :correct: d

        Шта је угнежђени упит?

.. quizq::

    .. mchoice:: ugnezdeni_korelisani_kako
        :answer_a: Најпре се, само једном, изврши подупит, а затим, такође само једном, спољни упит.
        :answer_b: Подупит се изврши по једном за сваки ред који се разматра спољним упитом.
        :answer_c: Најпре се, само једном, изврши спољни упит, а затим се за сваки његов ред изврши подупит.
        :answer_d: Најпре се, само једном, изврши подупит, а затим се за сваки његов ред изврши спољни упит.
        :correct: b

        Како се извршава угнежђени упит који садржи корелисани подупит?

.. quizq::

    .. mchoice:: ugnezdeni_postojanje_rezultata
        :answer_a: Само за корелисани подупит, иначе нема смисла.
        :answer_b: Само за некорелисани подупит, иначе нема смисла.
        :answer_c: Користи се и за корелисани и за некорелисани подупит.
        :correct: a

        Провера постојања резултата подупита се користи ...

.. quizq::

    Дат је упит:
    
    .. code-block:: sql
    
        SELECT count(*)
        FROM(
            SELECT COUNT(*) AS broj
            FROM izostanak
            GROUP BY id_ucenik)
        WHERE broj > 10

    .. mchoice:: ugnezdeni_tumacenje_1
        :answer_a: Број ученика који имају више од 10 изостанака
        :answer_b: Укупан број изостанака код свих ученика са више од 10 изостанака
        :answer_c: Укупан број изостанака код 10 ученика са највише изостанака
        :answer_d: Број изостанака за сваког ученика са више од 10 изостанака
        :answer_e: Број изостанака за сваког од 10 ученика са највише изостанака
        :correct: a

        Шта се добија извршавањем овог упита?

.. quizq::

    Дат је упит:
    
    .. code-block:: sql
    
        SELECT p.razred, u.odeljenje, p.naziv AS predmet, count(*) AS neocenjenih
        FROM predmet p
            JOIN ucenik u ON u.razred=p.razred
        WHERE NOT EXISTS (SELECT *
                      FROM ocena o
                      WHERE o.id_predmet = p.id)
        GROUP BY p.id, u.odeljenje
        ORDER BY p.razred, u.odeljenje, p.naziv
        
    .. mchoice:: ugnezdeni_tumacenje_2
        :answer_a: Списак неоцењених ученика, по предметима и одељењима.
        :answer_b: Списак предмета из којих има неоцењених ученика.
        :answer_c: Број неоцењених ученика за сваки предмет у сваком одељењу, где има неоцењених ученика.
        :answer_d: Списак одељења у којима има неоцењених ученика.
        :correct: c

        Шта се добија извршавањем овог упита? Означити најпрецизнији одговор.
