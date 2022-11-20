Угнежђени упити - квиз
======================


.. quizq::

    .. mchoice:: ugnezdeni_1
        :answer_a: Комбиновање резултата два независна упита.
        :answer_b: Упит над више табела.
        :answer_c: Условно извршавање упита.
        :answer_d: Упит над резултатом другог упита.
        :correct: d

        Шта је угнежђени упит?

.. quizq::

    Дат је упит:
   
    .. code-block:: sql
    
        SELECT id_predmet, round(AVG(ocena), 2) AS prosek
		FROM ocena
		WHERE id_predmet IN (SELECT id
				     FROM predmet
				     WHERE razred = 1)
		GROUP BY id_predmet;
       
    .. mchoice:: ugnezdeni_3
        :answer_a: идентификатор оцене из табеле ocena
        :answer_b: идентификатор предмета и просечна оцена из табеле ocena 
        :answer_c: идентификатор предмета из табеле predmet
        :correct: b

		Које све колоне или колону враћа као резултат цео упит у следећем примеру?

.. quizq::

    Дат је упит:
    
    .. code-block:: sql
    
        SELECT count(*)
        FROM(
            SELECT COUNT(*) AS broj
            FROM izostanak
            GROUP BY id_ucenik)
        WHERE broj > 10
       
    .. mchoice:: ugnezdeni_4
        :answer_a: Број ученика који имају више од 10 изостанака.
        :answer_b: Укупан број изостанака код свих ученика са више од 10 изостанака.
        :answer_c: Укупан број изостанака код 10 ученика са највише изостанака.
		:answer_d: Број изостанака за сваког ученика са више од 10 изостанака.
		:answer_e: Број изостанака за сваког од 10 ученика са највише изостанака.
        :correct: a

		Шта се добија извршавањем овог упита?

