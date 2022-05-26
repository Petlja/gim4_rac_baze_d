Спајање табела - квиз
=====================

.. quizq::

    .. mchoice:: spajanje_zasto
        :answer_a: Креирање нових табела, које ће бити запамћене у бази података.
        :answer_b: Добијање резултата који садржи податке из више табела.
        :answer_c: Смањивање броја табела у бази података.
        :answer_d: Могуће су разне реорганизације базе података (не само промена броја табела).
        :correct: b

        Шта се постиже спајањем табела у упитима?

.. quizq::

    .. mchoice:: spajanje_implicitno
        :answer_a: Спајање сваког реда једне табеле са сваким редом друге табеле.
        :answer_b: Спајање више од две табеле.
        :answer_c: Спајање које се дешава аутоматски и није под контролом онога ко пише упит.
        :answer_d: Спајање табеле са самом собом.
        :correct: a

        Шта је имплицитно спајање табела?

.. quizq::

    .. mchoice:: spajanje_redosled_tabela
        :answer_a: Не, ни код унутрашњег, ни код левог спољашњег спајања
        :answer_b: Код унутрашњег спајања може да утиче, а код левог спољашњег спајања не.
        :answer_c: Код унутрашњег спајања не утиче, а код левог спољашњег спајања може да утиче.
        :answer_d: Код сваког спајања може да утиче. 
        :correct: c

        Приликом спајања две табеле, име једне табеле наводимо после речи FROM, а другу после речи JOIN.
        Да ли замена места именима табела (тј. навођење друге после FROM, а прве после JOIN) утиче на резултат?

.. quizq::

    Дата су следећа два упита:
    
    .. code-block:: sql
    
        /* prvi upit*/
        SELECT *
        FROM tabela_a
             JOIN tabela_b ON tabela_a.id = tabela_b.id_a;

        /* drugi upit*/
        SELECT *
        FROM tabela_a
             LEFT JOIN tabela_b ON tabela_a.id = tabela_b.id_a;
     
    .. mchoice:: spajanje_duza_tabela
        :multiple_answers:
        :answer_a: Резултат другог упита је увек дужи од резултата првог упита.
        :answer_b: Резултати ових упита могу да буду потпуно исти.
        :answer_c: Резултат другог упита никад није краћи од резултата првог упита.
        :answer_d: Резултат првог упита никад није краћи од резултата другог упита.
        :correct: b,c

        Означите сва тачна тврђења о резултатима датих упита.

.. quizq::

    Дат је следећи упит:
    
    .. code-block:: sql

        SELECT ime, prezime, razred, odeljenje, ocena, datum
        FROM ocena o
            JOIN ucenik u ON u.id = o.id_ucenik
        ORDER BY id_ucenik
    
    .. mchoice:: spajanje_left_i_inner_join_1
        :answer_a: Ако су сви ученици оцењени
        :answer_b: Ако су вредности id_ucenik у табели ocena исправне (тј. за сваку постоји ученик са тим идентификатором у табели ucenik)
        :answer_c: Резултат ће увек бити различит (без обзира на податке)
        :answer_d: Резултат ће увек бити исти (без обзира на податке)
        :correct: b

        Под којим условима је се резултат неће променити када у упиту уместо JOIN напишемо LEFT JOIN?

.. quizq::

    Дат је следећи упит:
    
    .. code-block:: sql

        SELECT ime, prezime, razred, odeljenje, ocena, datum
        FROM ucenik u
            JOIN ocena o ON u.id = o.id_ucenik
        ORDER BY id_ucenik
    
    .. mchoice:: spajanje_left_i_inner_join_2
        :answer_a: Ако су сви ученици оцењени
        :answer_b: Ако су вредности id_ucenik у табели ocena исправне (тј. за сваку постоји ученик са тим идентификатором у табели ucenik)
        :answer_c: Резултат ће увек бити различит (без обзира на податке)
        :answer_d: Резултат ће увек бити исти (без обзира на податке)
        :correct: a

        Под којим условима је се резултат неће променити када у упиту уместо JOIN напишемо LEFT JOIN?
