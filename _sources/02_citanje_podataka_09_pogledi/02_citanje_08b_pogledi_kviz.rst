Погледи - квиз
==============

.. quizq::

    .. mchoice:: pogled_pojam
        :answer_a: Именовани упит, који може да се користи као табела за читање података.
        :answer_b: Стање свих података у бази у датом тренутку.
        :answer_c: Начин на који базу података види одређени корисник.
        :answer_d: Резултат неког упита, какав је био у датом тренутку.
        :correct: a

        Шта је поглед на базу података?

.. quizq::

    .. mchoice:: pogled_zasto
        :multiple_answers:
        :answer_a: Резултат упита У може да се види без његовог извршавања.
        :answer_b: Поједностављује се писање угнежђених упита, који користе упит У као свој подупит.
        :answer_c: Лакше се прати историја промена података у бази.
        :answer_d: Поједностављује се писање упита пројекције и селекције над упитом У.
        :correct: b,d

        На који начин дефинисање погледа за неки упит *У* може да буде корисно? Означи све тачне одговоре.

.. quizq::

    Нека смо дефинисали поглед ocene_detaljno на следећи начин:
    
    .. code-block:: sql
    
        CREATE VIEW ocene_detaljno AS
            SELECT o.id as oid, u.id as uid, p.id as pid, o.ocena, o.datum, o.vrsta, u.ime, u.prezime, u.razred, u.odeljenje, p.naziv as predmet
            FROM ocena o
                JOIN ucenik u ON u.id = o.id_ucenik
                JOIN predmet p ON p.id = o.id_predmet

    
    .. mchoice:: pogled_kako
        :answer_a: SELECT * FROM ocene_detaljno
        :answer_b: SELECT ocene_detaljno
        :answer_c: VIEW ocene_detaljno
        :answer_d: VIEW * FROM ocene_detaljno
        :correct: a

        Којим једноставнијим упитом сада можемо да видимо резултат упита који дефинише поглед ocene_detaljno?



.. quizq::

    Нека смо дефинисали поглед ocene_detaljno на следећи начин:
    
    .. code-block:: sql
    
        CREATE VIEW ocene_detaljno AS
            SELECT o.id as oid, u.id as uid, p.id as pid, o.ocena, o.datum, o.vrsta, u.ime, u.prezime, u.razred, u.odeljenje, p.naziv as predmet
            FROM ocena o
                JOIN ucenik u ON u.id = o.id_ucenik
                JOIN predmet p ON p.id = o.id_predmet

    .. dragndrop:: pogled_opisi_i_upiti
        :match_1: SELECT razred, predmet, count(*) <br/>FROM ocene_detaljno <br/>GROUP BY pid ||| број оцена по предметима
        :match_2: SELECT razred, predmet, count (distinct uid) <br/>FROM ocene_detaljno <br/>GROUP BY pid ||| број оцењених ученика по предметима
        :match_3: SELECT count (distinct pid) <br/>FROM ocene_detaljno ||| број предмета из којих постоје оцене
      
        Упари упите са њиховим описима:
