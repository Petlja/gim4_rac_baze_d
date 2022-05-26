SQLite и SQLite Studio - квиз
=============================

.. quizq::

    .. mchoice:: SQLite_sta_je_SQLite
        :answer_a: Један упитни језик
        :answer_b: Фајл који у себи садржи базу података
        :answer_c: Окружење за писање програма који користе базу података
        :answer_d: Један систем за управљање базом података
        :correct: d

        Шта је SQLite?


.. quizq::

    .. mchoice:: SQLite_interfejs
        :multiple_answers:
        :answer_a: апликативни
        :answer_b: мрежни
        :answer_c: кориснички
        :answer_d: интерни (локални)
        :answer_e: приватни
        :correct: a,c

        Путем којих интерфејса може да се користи SQLite?

.. quizq::

    .. mchoice:: SQLite_commit_str_ch
        :answer_a: да финализује структуру базе података и забрани даље измене
        :answer_b: да запамти измене направљене у структури базе података
        :answer_c: да одбаци измене направљене у структури базе података од последњег чувања базе
        :answer_d: да дозволи мењање структуре базе података
        :correct: b

        Чему служи команда Commit structure changes?

.. quizq::

    .. mchoice:: SQLite_kreiranje_tabele
        :multiple_answers:
        :answer_a: све колоне морају одмах да се дефинишу, јер не могу касније да се додају
        :answer_b: колона која представља примарни кључ може да се одабере накнадно
        :answer_c: додатна ограничења за колоне (Not null, Default и сл.) могу да се дефинишу накнадно
        :correct: b,c

        Означи сва тврђења која важе за SQLite студио приликом креирања табеле.

.. comment

            Приликом додавања нове колоне у табелу, поребно је дефинисати: (име колоне, тип податка, величина, опције (Primary key, Autoincrement, Not null, Collate, Default...))
