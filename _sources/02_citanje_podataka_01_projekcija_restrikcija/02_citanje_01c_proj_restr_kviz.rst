Пројекција и селекција - квиз
=============================

.. quizq::

    .. mchoice:: proj_sel_izbor_kolona
        :answer_a: Селекција
        :answer_b: Пројекција
        :answer_c: Рестрикција
        :answer_d: Филтрирање
        :answer_e: Ограничавање
        :correct: b

        Како се назива операција којом се издвајају само неке колоне из табеле?

.. quizq::

    .. mchoice:: proj_sel_izbor_vrsta
        :multiple_answers:
        :answer_a: Селекција
        :answer_b: Пројекција
        :answer_c: Рестрикција
        :answer_d: Филтрирање
        :answer_e: Скраћивање
        :correct: a,c,d

        Означи све називе операције којом се издвајају само неке врсте из табеле?

.. quizq::

    .. mchoice:: proj_sel_projekcija_kako
        :answer_a: Навођењем услова који треба да испуне колоне табеле
        :answer_b: Навођењем услова који треба да испуне редови табеле
        :answer_c: Навођењем имена изабраних колона после речи SELECT
        :answer_d: Подешавањем својстава колона табеле
        :correct: c

        Како се остварује пројекција дате табеле?

.. quizq::

    .. mchoice:: proj_sel_restrikcija_kako
        :answer_a: Навођењем услова који треба да испуне колоне табеле
        :answer_b: Навођењем услова који треба да испуне редови табеле
        :answer_c: Навођењем имена изабраних колона после речи SELECT
        :answer_d: Подешавањем својстава колона табеле
        :correct: b

        Како се остварује рестрикција дате табеле?

.. quizq::

    .. mchoice:: proj_sel_kombinovanje
        :answer_a: Није могуће.
        :answer_b: Могуће је, али то треба да се омогући у подешавањима табеле.
        :answer_c: Могуће је, али то зависи од садржаја табеле.
        :answer_d: Могуће је, увек и без ограничења.
        :correct: d

        Да ли је могуће у истом упиту применити и пројекцију и рестрикцију на дату табелу?

.. quizq::

    .. mchoice:: proj_sel_komb_2_upita
        :answer_a: У првом упиту имамо само селекцију, а у другом и пројекцију и селекцију
        :answer_b: У првом упиту имамо само пројекцију, а у другом имамо само селекцију
        :answer_c: У првом упиту имамо пројекцију и селекцију, а у другом имамо само пројекцију
        :answer_d: У првом упиту имамо само пројекцију, а у другом и пројекцију и селекцију 
        :correct: d

		Дата су следеће два упита:
		
	.. code-block:: sql

		/* prvi upit*/
		SELECT prezime
		FROM ucenik;

		/* drugi upit*/
		SELECT id_ucenik, status 
		FROM izostanak WHERE cas = 1;
			
	Које тврђење је тачно?

.. quizq::

    .. mchoice:: upit_razred_fond
        :answer_a: SELECT razred, fond FROM predmet
        :answer_b: SELECT razred FROM predmet WHERE naziv='Математика';
        :answer_c: SELECT razred, fond FROM predmet WHERE naziv='Математика'; 
        :answer_d: SELECT razred, fond FROM predmet WHERE naziv=Математика;
        :correct: c

        Којим упитом добијамо разред и фонд часова за предмет Математика који се изучава у различитим разредима?

.. quizq::

    .. mchoice:: upit_prezime_dat_4
        :answer_a: SELECT prezime, datum_rodjenja FROM predmet WHERE razred=4
        :answer_b: SELECT prezime, datum_rodjenja FROM ucenik WHERE razred=4 
        :answer_c: SELECT prezime FROM ucenik WHERE razred=4 
        :answer_d: SELECT prezime, datum_rodjenja FROM ucenik WHERE razred=1 
        :correct: b
		
		Којим упитом добијамо презимена и датуме рођења свих ученика четвртог разреда?Којим упитом добијамо разред и фонд часова за предмет Математика који се изучава у различитим разредима?