Агрегатне функције и груписање - квиз
=====================================

.. quizq:: 

    .. mchoice:: agregatne_prosek
        :answer_a: AVG
        :answer_b: AVERAGE
        :answer_c: MEAN
        :answer_d: MEDIAN
        :correct: a

        Којом агрегатном функцијом добијамо просечну вредност неке колоне?

.. quizq:: 

    Дат је следећи упит:

    .. code-block:: sql

        SELECT id_ucenik, count(*) AS br_izost
        FROM izostanak
        GROUP BY id_ucenik
        ORDER BY br_izost DESC
        LIMIT 3;
    
    .. mchoice:: agregatne_br_izost
        :answer_a: Подаци о прва три ученика са различитим бројем изостанака.
        :answer_b: Подаци о ученицима који су направили прва три изостанка.
        :answer_c: Подаци о три ученика са највише изостанака.
        :answer_d: Подаци о прва три ученика који имају изостанке.
        :correct: c

        Шта се добија извршавањем овог упита?

.. quizq:: 

    .. dragndrop:: agregatne_izostanci_uparivanje
        :match_1: SELECT COUNT(*) <br/>FROM izostanak  ||| Укупан број направљених изостанака
        :match_2: SELECT COUNT(*) <br/>FROM izostanak <br/>GROUP BY id_ucenik ||| Број изостанака сваког ученика
        :match_3: SELECT COUNT(DISTINCT id_ucenik) <br/>FROM izostanak ||| Број ученика који су правили изостанке
      
        Упари упите са њиховим описима:

.. quizq:: 

    Дати су следећи упити:
    
    .. code-block:: sql
    
        /* upit broj 1*/
        SELECT id_ucenik, id_predmet, max(ocena) as max_ocena
        FROM ocena
        WHERE max_ocena < 3
        GROUP BY id_ucenik, id_predmet

        /* upit broj 2*/
        SELECT id_ucenik, id_predmet, max(ocena) as max_ocena
        FROM ocena
        GROUP BY id_ucenik, id_predmet
        HAVING max_ocena < 3
        
        /* upit broj 3*/
        SELECT id_ucenik, id_predmet, max(ocena) as max_ocena
        FROM ocena
        HAVING max_ocena < 3
        GROUP BY id_ucenik, id_predmet

    
    
    .. mchoice:: agregatne_max_dvojka
        :answer_a: Упит број 1
        :answer_b: Упит број 2
        :answer_c: Упит број 3
        :correct: b

        Којим од понуђених упита добијамо ученике и предмете, за које је највећа оцена ученика из тог предмета двојка?
