Базе и табеле - квиз
====================

.. quizq::

    .. mchoice:: baze_tabele_zahtev_upucen_SUBP
        :answer_a: упит
        :answer_b: наредба
        :answer_c: изјава
        :answer_d: налог
        :correct: a

        Како називамо захтев упућен систему за управљање базом података?


.. quizq::

    .. dragndrop:: baze_tabele_sinonimi
        :match_1: табела ||| релација, ентитет
        :match_2: колона ||| атрибут, својство, особина
        :match_3: ред (врста) ||| инстанца, објекат, јединка
        
        Упари појмове који (у контексту база података) имају исто или слично значење. 


.. quizq::

    .. mchoice:: baze_tabele_primarni_kljuc
        :answer_a: Најважнија табела у бази података.
        :answer_b: Прва колона у табели.
        :answer_c: Колона или група колона, који својим садржајем једнозначно идентификују врсту у табели.
        :answer_d: Колона која представља страни кључ у другој табели.
        :correct: c

        Шта је примарни кључ?

.. quizq::

    .. mchoice:: baze_tabele_nalazenje_vrste
        :answer_a: Према вредностима свих атрибута.
        :answer_b: Према положају тог реда у запису табеле.
        :answer_c: Навођењем свих услова који важе за ту врсту.
        :answer_d: Према примарном кључу.
        :correct: d

        Који је основни и најефикаснији начин да се пронађе одређени ред у табели?

.. quizq::

    .. mchoice:: baze_tabele_korist_od_stranog_kljuca
        :multiple_answers:
        :answer_a: мањи укупан број табела у бази података
        :answer_b: избегавање појаве неконзистентних података (нпр. два датума рођења за исту особу)
        :answer_c: мањи број редова у појединим табелама базе података
        :answer_d: избегавање редунданце (вишеструког појављивања истих података) у бази 
        :correct: b,d

        Шта све може да се постигне употребом страног кључа?

.. quizq::

    .. mchoice:: baze_tabele_primer_veze_vise_prema_vise
        :answer_a: изостанак - ученик
        :answer_b: одељење - наставник
        :answer_c: оцена - ученик
        :answer_d: одељење - ученик
        :correct: b

        Шта је од наведеног је пример везе више-према-више?



.. quizq::

    .. mchoice:: id_nastavnika
        :answer_a: 1
        :answer_b: 2
        :answer_c: 3
        :answer_d: 4
        :correct: c
        
        **Наредна питања се односе на следећу слику**

        .. image:: ../../_images/baze_kviz1.png
           :width: 780
           :align: center
    
        Који је идентификациони број наставника који се зове и презива Филип Марић?
            
.. quizq::

    .. mchoice:: kolone_primarni_kljucevi
        :answer_a: id, ime, prezime у табели nastavnik, id_nastavnik у табели predaje
        :answer_b: id у табели nastavnik,  naziv у табели predmet
        :answer_c: id у табели nastavnik, id у табели predmet
        :answer_d: id у табели nastavnik, id_predmet у табели predaje,  id, naziv у табели predmet
        :correct: c

        Који списак садржи само колоне које су примарни кључеви?
		
.. quizq::

    .. mchoice:: kolone_strani_kljucevi
        :answer_a: id у табели nastavnik, id_nastavnik у табели predaje
        :answer_b: id у табели nastavnik,  id у табели predmet
        :answer_c: id_predmet у табели predaje, id у табели predmet
        :answer_d: id_predmet, id_nastavnik у табели predaje
        :correct: d

        Који списак садржи само колоне које су страни кључеви?	
		
.. quizq::

    .. mchoice:: strani_primarni_kljuc
        :answer_a: id_nastavnik у табели predaje, id у табели predmet 
        :answer_b: id_nastavnik у табели predaje, id у табели nastavnik 
        :answer_c: id_predmet у табели predaje, id у табели nastavnik
        :answer_d: id_predmet у табели predaje, id_nastavnik у табели predaje
        :correct: b

        Који списак садржи добру комбинацију страни кључ и одговарајући примарни кључ?
		
		
.. quizq::

    .. mchoice:: nastavnik_RI4
        :answer_a: 1
        :answer_b: 2
        :answer_c: 3
        :answer_d: 4
        :correct: b

        Колико наставника предаје Рачунарство и информатику у четвртом разреду?
		
.. quizq::

    .. mchoice:: nastavnik_RI2
        :answer_a: Нина Алимпић
        :answer_b: Нина Алимпић, Мијодраг Ђуришић, Филип Марић 
        :answer_c: Мијодраг Ђуришић, Филип Марић
        :answer_d: Станка Матковић, Филип Марић 
        :correct: c

        Ко предаје Рачунарство и информатику у другом разреду?