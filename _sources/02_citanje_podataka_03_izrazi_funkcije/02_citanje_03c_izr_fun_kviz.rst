Изрази и функције - квиз
========================

.. quizq::

    .. mchoice:: izrazi_fje_spajanje_niski
        :answer_a: Оператор &
        :answer_b: Оператор &&
        :answer_c: Оператор |
        :answer_d: Оператор ||
        :answer_e: Оператор +
        :correct: d

        Који оператор користимо када желимо да две или више ниски спојимо у једну?

.. quizq::

    Дат је следећи упит:
    
    .. code-block:: sql
    
        SELECT naziv, CASE
                WHEN razred = 1 THEN 'I'
                WHEN razred = 2 THEN 'II'
                WHEN razred = 3 THEN 'III'
                WHEN razred = 4 THEN 'IV'
            END AS godina
        FROM predmet;
    
    .. mchoice:: izrazi_fje_alias
        :answer_a: naziv
        :answer_b: razred
        :answer_c: godina
        :answer_d: predmet
        :answer_e: Неће имати наслов.
        :correct: c

        Који наслов ће имати друга колона резултата добијеног датим упитом?

.. quizq::

    .. mchoice:: izrazi_fje_substr
        :answer_a: "cdef"
        :answer_b: "bcde"
        :answer_c: "bcd"
        :answer_d: "cde"
        :answer_e: "cd"
        :correct: b

        Која је вредност функције substr("abcdefgh", 2, 4)

.. quizq::

    .. mchoice:: izrazi_fje_cast
        :answer_a: SELECT cast (substr(datum, 9, 2) AS int) AS dan FROM izostanak
        :answer_b: SELECT substr(datum, 9, 2) AS dan FROM izostanak
        :answer_c: SELECT cast substr(datum, 9, 2) AS int AS dan FROM izostanak
        :answer_d: SELECT cast (datum AS int) AS dan FROM izostanak
        :correct: a

        Који од понуђених упита даје редни број дана у месецу (као нумерички податак) за сваки уписан изостанак?
        
.. quizq::

    .. mchoice:: izrazi_fje_poslednje_slovo
        :answer_a: SELECT * FROM ucenik WHERE substr(prezime, len(prezime), 1)='в'
        :answer_b: SELECT * FROM ucenik WHERE substr(prezime, length(prezime), 1)='в'
        :answer_c: SELECT * FROM ucenik WHERE substr(prezime, len(prezime)-1, 1)='в'
        :answer_d: SELECT * FROM ucenik WHERE substr(prezime, len(prezime))='в'
        :answer_e: SELECT * FROM ucenik WHERE substr(prezime, length(prezime)-1, 1)='в'
        :correct: b

        Који од понуђених упита даје податке о ученицима чије презиме се завршава на слово „в“?
        
.. comment

    SELECT naziv, razred, 37 * fond AS godisnji_fond        FROM predmet        WHERE godisnji_fond == 74;
    SELECT naziv, razred, 2 - razred % 2 AS smena           FROM predmet;
    
    upper, lower
    max, min (две или више вредности)
