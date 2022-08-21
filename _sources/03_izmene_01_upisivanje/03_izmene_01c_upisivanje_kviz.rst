Уписивање података - квиз
=========================

.. quizq::

    .. mchoice:: unos1
        :answer_a: INSERT
        :answer_b: ADD
        :answer_c: APPEND
        :answer_d: UPDATE
        :correct: a

        Којом SQL командом се у табелу уписују нови редови?

.. quizq::

    .. mchoice:: unos2
        :answer_a: Ипак ће бити уписана вредност NULL у ту колону
        :answer_b: За ту колону неће бити уписано ништа, у остале колоне ће бити уписане наведене вредности
        :answer_c: Биће пријављена грешка, а табела ће остати неизмењена
        :answer_d: У простору за ту колону ће остати насумичан садржај, а у остале колоне ће бити уписане наведене вредности
        :correct: c

        Шта се дешава ако изоставимо вредност за колону у којој су недостајуће вредности забрањене (NOT NULL) и за коју није постављена опција AUTOINCREMENT?

.. quizq::

    .. mchoice:: unos3
        :answer_a: Да пронађемо ред у табели, у који желимо да унесемо измене.
        :answer_b: Да у једном упиту најпре пронађемо вредности које не знамо, а затим да их (заједно са познатим вредностима) упишемо у један или више нових редова табеле.
        :answer_c: Помоћу ове команде формирамо нову табелу, користећи садржај постојећих табела.
        :correct: b

        Чему служи команда INSERT са клаузулом SELECT?

.. quizq::

    .. mchoice:: unos4
        :answer_a: VALUES ('Милица', 'Петровић', 2, 1)
        :answer_b: VALUES ('Милица', 'Петровић', 'ж', '2005-08-31')
        :answer_c: VALUES ('Милица', 'Петровић', 'ж', 2, 1, '2005-08-31')
        :answer_d: VALUES ('Милица', 'Петровић', 'ж', '2005-08-31', 2, 1) 
        :correct: d

		Уколико у теблу ucenik треба да унесемо нови ред и неопходно је да податке унесемо у следећем 
		редоследу (ime, prezime, pol, datum_rodjenja, razred, odeljenje), која клаузула VALUES је исправна?
		
.. quizq::

    .. mchoice:: unos5
        :answer_a: (datum, ocena, vrsta, id_ucenik, id_predmet)
        :answer_b: (id_ucenik, id_predmet, datum, ocena, vrsta)
        :answer_c: (id_ucenik, id_predmet, ocena, vrsta, datum)
		:answer_d: (id_ucenik, id_predmet, datum, vrsta, ocena)
        :correct: b

        Који списак колона одговара следећој клаузули:  
		VALUES (293, 9, '2020-10-01', 5, 'контролна вежба')?

