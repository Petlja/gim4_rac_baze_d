Ажурирање података - квиз
=========================

.. quizq::

    .. mchoice:: izmena_1
        :answer_a: UPGRADE
        :answer_b: CHANGE
        :answer_c: UPDATE
        :answer_d: REFRESH
        :correct: c

        Којом SQL командом се постојећи подаци у табели замењују новим?

.. quizq::

    .. mchoice:: izmena_2
        :answer_a: Увек само текући ред.
        :answer_b: Увек само последњи ред.
        :answer_c: Увек само први ред.
        :answer_d: Увек сви редови.
        :answer_e: Редови за које важи услов који наведемо.
        :correct: e

        Који редови табеле ће бити измењени извршавањем команде за ажурирање табеле?

.. quizq::

    .. mchoice:: izmena_3
        :multiple_answers:
        :answer_a: Поништавањем извршења последњег упита помоћу команде UNDO.
        :answer_b: Тако што пре упита ажурирања извршимо упит SELECT, да бисмо видели редове који би били промењени.
        :answer_c: Тако што пре упита ажурирања направимо копију целе базе података.
        :answer_d: Тако што погледамо *preview* резултата упита ажурирања.
        :correct: b,c

        На који све начин можемо да смањимо шансе да изгубимо податке услед случајног мењања редова у некој табели, а које није требало мењати?

.. quizq::

    .. mchoice:: izmena_4
        :answer_a: SET datum_rodjenja = '2005-08-31' WHERE datum_rodjenja != '2005-08-31'
        :answer_b: SET datum_rodjenja = '2005-08-31' WHERE id = 4 
        :answer_c: SET id = 4 WHERE datum_rodjenja = '2005-08-31'
        :answer_d: SET id = 4 WHERE id = 4
        :correct: b

        Шта је неопходно да додамо упиту којим ажурирамо податке уколико желимо ученику 
		са идентификационим бројем 4 да променимо неисправно унет датум рођења на 
		исправан 31. август 2005. године?

.. quizq::

    .. mchoice:: izmena_5
        :answer_a: SET fond = 3 WHERE fond = 2
        :answer_b: SET fond = 2 WHERE fond = 3 
        :answer_c: SET fond = 2 WHERE naziv = 'Рачунарство и информатика' AND razred = 3
        :answer_d: SET fond = 3 WHERE naziv = 'Рачунарство и информатика' AND razred = 1 
        :correct: d

        По новом плану и програму предмет рачунарство и информатика у првом разреду треба да има фонд 
		од 3 уместо 2 часа. Ово је једини предмет са тренутним фондом од 2 часа код којег постоји измена. 
		Шта је неопходно да додамо упиту којим ажурирамо податке у складу са овом изменом?

.. quizq::

    .. mchoice:: izmena_6
        :answer_a: SET datum = '2020-10-16' WHERE datum = '2020-10-15' AND id_ucenik = 1
        :answer_b: SET datum = '2020-10-16' WHERE datum = '2020-10-15' AND id_predmet = 1
        :answer_c: SET datum = '2020-10-15' WHERE datum = '2020-10-16' AND id_ucenik  =1
        :answer_d: SET datum = '2020-10-15' WHERE datum = '2020-10-16' AND id_predmet = 1 
        :correct: d

        Наставник је грешком уписао да је писмени задатак из предмета чији је идентификатор 1 
		одржан 15. октобра, а одржан је заправо 16. октобра. Шта је неопходно да додамо упиту којим 
		ажурирамо податке у складу са овом изменом?

.. quizq::

    .. mchoice:: izmena_7
        :answer_a: SET fond = fond - 1 WHERE naziv = 'Математика' AND razred = 1
        :answer_b: SET fond = fond - 1 WHERE naziv = 'Математика' 
        :answer_c: SET fond = fond + 1 WHERE naziv = 'Математика' AND razred = 1 
        :answer_d: SET fond = fond + 1 WHERE naziv = 'Математика'
        :correct: d

        По новом плану и програму фонд часова математике у сваком разреду се повећава за један. 
		Уколико је потребно да напишемо један упит који реализује ову промену за све разреде, 
		шта је неопходно да додамо упиту у складу са овом изменом?
