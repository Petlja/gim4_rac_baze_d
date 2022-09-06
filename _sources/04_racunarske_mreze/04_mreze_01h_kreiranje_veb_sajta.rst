Креирање веб-сајта
==================

Веб-сајт се најчешће састоји од више веб-страна. За веб-сајт је потребно
креирати посебан фолдер, а међу веб-странама се увек једна издваја као почетна.

На сам почетак сваке веб-стране, након отвореног тага ``<body>``, а пре
наслова, можемо да додамо линкове ка свим веб-странама сајта.

.. code-block:: html

 <a href="pocetna_racunarske_mreze.html">Почетна страна</a>
 <a href="strana1_mrezni_slojevi_protokoli.html">Мрежни слојеви и протоколи</a>
 <a href="strana2_adrese.html">Адресе</a>
 <a href="strana3_detaljnije_mrezni_slojevi_protokoli.html">Детаљније о протоколима</a>

Елемент ``a`` омогућава читаоцу да одабере (кликне, тапне) на текст унутар
``a`` елемента и том акцијом пређе на *HTML* документ који је наведен као
вредност ``href`` атрибута. На овај начин можемо да направимо везе од једног
*HTML* документа ка осталима.

У сваку веб-страну веб-сајта треба додати исти ред који веб-страну повезује са
дефинисаним дизајном. Један *CSS* документ је потребан за цео сајт. На тај
начин је уједначен дизајн целог сајта и визуелно је јасно да све веб-стране
чине једну целину.

Слике је добро одојити у ново креирани фолдер унутар фолдера за веб-сајт, па ће
онда и елемент ``img`` изгледати другачије, тј. уз име фајла треба навести и
име фолдера.

.. code-block:: html

 <img src="slike/strana1_slika1.jpg" alt="Klijent server komunikacija"/>

.. questionnote::

 **Задатак**

 У претходном задатку је било потребно да се креира фолдер за веб-сајт и да се
 у њему нађе већ неколико фајлова потребних за креирање једне странице сајта.

 Унутар тог већ креираног фолдера за веб-сајт додати фолдер slike. У овај
 фолдер преместити две слике и урадити одговарајуће измене у документу
 ``strana1_mrezni_slojevi_protokoli.html`` тако да поред назива слика у
 елеметну ``img`` стоји и назив новог фолдера у којем се слике налазе slike.

 У фолдер са сликама додати и слике које можеш да преузмеш овде:

 `pocetna_slika1.jpg <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/baze_IV/pocetna_slika1.jpg>`_  

 `pocetna_slika2.jpg <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/baze_IV/pocetna_slika2.jpg>`_

 `pocetna_slika3.jpg <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/baze_IV/pocetna_slika3.jpg>`_

 .. figure:: ../../_images/Picture20.png
    :width: 780px
    :align: center
    :class: screenshot-shadow

 У фолдер ставити и следеће фајлове које можеш да преузмеш овде:

 `pocetna_racunarske_mreze.txt <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/baze_IV/pocetna_racunarske_mreze.txt>`_

 `strana2_adrese.txt <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/baze_IV/strana2_adrese.txt>`_

 `strana3_detaljnije_mrezni_slojevi_protokoli.txt <https://petljamediastorage.blob.core.windows.net/root/Media/Default/Kursevi/baze_IV/strana3_detaljnije_mrezni_slojevi_protokoli.txt>`_

 Сваки од ова три фајла отворити у едитору текста, а затим урадити
 File/Save As...

 Сваки од ова три фајла сачувати у другом формату да бисмо могли од њих да
 добијемо веб-странице. У едитору текста изабрати са менија ``File/Save As...``,
 а затим је потребно да изаберете ``All Files`` под ``Save as type``, наведете
 назив фајла са .html (на пример: pocetna_racunarske_mreze.html), и проверите да
 ли је под ``Encoding`` изабран ``UTF-8``.

 .. figure:: ../../_images/Picture21.png
    :width: 780px
    :align: center
    :class: screenshot-shadow

 Из фолдера обрисати почетне ``txt`` фајлове. Садржај фолдера би требало да буде
 као на следећој слици:

 .. figure:: ../../_images/Picture22.png
    :width: 457px
    :align: center
    :class: screenshot-shadow

 Сваки од *HTML* докумената поново отворити у едитору текста на један од следећа
 два начина: отворити едитор, па изабрати са менија ``File/Open`` и пронаћи фајл
 (обавезно изабрати ``All Files`` и ``Encoding/UTF-8``); или урадити десни клик
 мишем над фајлом и изабрати ``Open with/Notepad``.

 У документа додати ознаке, тј. тагове, за све наслове, поднаслове, пасусе,
 набрајања, слике, речи које треба да буду приказане подебљано (нпр. нове
 појмове), речи које треба да буду приказане искошено (нпр. речи на енглеском
 језику), и слике.

 Обавезно у сваки документ додати ред којим се повезује са креираним дизајном,
 као и линкове ка свим веб-странама сајта, како је раније описано.

 Погледати како креиране веб-стране изгледају у прегледачу, нпр. прегледачу
 Chrome. Уколико има неких недостатака, вратити се у едитор текста и поправити
 уочене пропусте.
