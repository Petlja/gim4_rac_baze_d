Уписивање података - квиз
=========================

.. quizq::

    .. mchoice:: unos_komanda
        :answer_a: INSERT
        :answer_b: ADD
        :answer_c: APPEND
        :answer_d: UPDATE
        :correct: a

        Којом SQL командом се у табелу уписују нови редови?

.. quizq::

    .. mchoice:: unos_izostavljanje_vrednosti
        :answer_a: Ипак ће бити уписана вредност NULL у ту колону
        :answer_b: За ту колону неће бити уписано ништа, у остале колоне ће бити уписане наведене вредности
        :answer_c: Биће пријављена грешка, а табела ће остати неизмењена
        :answer_d: У простору за ту колону ће остати насумичан садржај, а у остале колоне ће бити уписане наведене вредности
        :correct: c

        Шта се дешава ако изоставимо вредност за колону у којој су недостајуће вредности забрањене (NOT NULL) и за коју није постављена опција AUTOINCREMENT?

.. quizq::

    .. mchoice:: unos_insert_select
        :answer_a: Да пронађемо ред у табели, у који желимо да унесемо измене.
        :answer_b: Да у једном упиту најпре пронађемо вредности које не знамо, а затим да их (заједно са познатим вредностима) упишемо у један или више нових редова табеле.
        :answer_c: Помоћу ове команде формирамо нову табелу, користећи садржај постојећих табела.
        :correct: b

        Чему служи команда INSERT са клаузулом SELECT?
