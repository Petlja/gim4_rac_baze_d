Сортирање, уклањање дупликата, ограничавање одговора - квиз
===========================================================

.. quizq::

    .. mchoice:: sortiranje_klauzula
        :answer_a: Клаузула ORDER BY
        :answer_b: Клаузула SORT BY
        :answer_c: Клаузула ORDERED BY
        :answer_d: Клаузула SORTED BY
        :answer_e: Клаузула ARRANGE BY
        :correct: a

        Која клаузула се користи када желимо да подаци у резултату буду уређени растуће по некој колони?

.. quizq::

    .. mchoice:: sortiranje_tip_podatka
        :multiple_answers:
        :answer_a: Бројеви
        :answer_b: Ниске
        :answer_c: Датуми
        :correct: a,b,c

        За које од понуђених типова података резултат упита може да се сортира по податку тог типа (означи све тачне одговоре)?

.. quizq::

    .. mchoice:: sortiranje_opadajuce
        :answer_a: DESCENDING
        :answer_b: REVERSE
        :answer_c: REVERSED
        :answer_d: DESC
        :answer_e: DECREASING
        :correct: d

        Коју реч треба дописати иза колоне по којој се сортирају подаци, ако желимо опадајући редослед?

.. quizq::

    .. mchoice:: sortiranje_po_vise_kolona
        :answer_a: По азбучном редоследу презимена, а они са истим презименом по азбучном редоследу имена
        :answer_b: По азбучном редоследу имена, а они са истим презименом по азбучном редоследу презимена
        :answer_c: По азбучном редоследу имена (а они са истим именом у произвољном редоследу)
        :answer_d: По азбучном редоследу презимена (а они са истим презименом у произвољном редоследу)
        :answer_e: Упит се неће извршити јер је неисправан.
        :correct: b

        Ако се као податак по коме сортирамо ученике наведе „ime, prezime“, како ће подаци бити сортирани?

.. quizq::

    .. fillintheblank:: ogranicavanje_klauzula

        Претпоставимо да хоћемо само да проверимо да ли смо неки упут добро написали и не желимо комплетан резултат упита, него само првих 10 редова.
        
        Коју клаузулу треба додати упиту да бисмо ово постигли? Одговор упиши ВЕЛИКИМ СЛОВИМА.
       
        Одговор: |blank|

        - :^\s*LIMIT\s+10\s*$: Одговор је тачан.
          :x: Одговор није тачан.

.. quizq::

    .. mchoice:: ogranicavanje_mala_tabela
        :answer_a: Последњи ред ће бити поновљен потребан број пута, да би резултат имао тражени број редова.
        :answer_b: Резултати се понављају у круг док се добије тражени број редова.
        :answer_c: Резултат ће бити допуњен празним редовима.
        :answer_d: Биће приказано 4 реда.
        :answer_e: Биће пријављена грешка.
        :correct: d

        Шта ће се догодити ако резултат упита ограничимо на 10 редова, а у резултату има само 4 реда?

.. quizq::

    .. mchoice:: bez_ponavljanja
        :answer_a: SELECT datum FROM izostanak
        :answer_b: SELECT DISTINCT datum FROM izostanak
        :answer_c: SELECT UNIQUE datum FROM izostanak
        :answer_d: SELECT datum FROM izostanak UNIQUE 
        :answer_e: SELECT datum FROM izostanak DISTINCT
        :correct: b

        Којим од наведених упита добијамо све датуме када су прављени изостанци, али без понављања?



.. comment

        Ограничавање броја врста у резултату са приказом од средине (уместо од почетка)?
