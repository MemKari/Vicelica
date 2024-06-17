from random import choice

words_tuple = (
    'апельсин', 'зеркало', 'озеро', 'воробей', 'жизнь', 'ястреб', 'груша', 'белка', 'бабушка', 'песня', 'футбол',
    'школа', 'сигнал', 'шар', 'человек', 'алмаз', 'щука', 'ракета', 'ежевика', 'вишня', 'звезда', 'ремень', 'холм',
    'заяц', 'папка', 'кирка', 'городок', 'альбом', 'радио', 'фабрика', 'ил', 'камень', 'зонтик', 'диапазон', 'детство',
    'сумка', 'лицо', 'ангел', 'жар', 'ягода', 'тропинка', 'экспресс', 'аквариум', 'шапка', 'череп', 'фура', 'тыква',
    'юбка', 'холод', 'грусть', 'капля', 'волк', 'игрушка', 'изучение', 'океан', 'новости', 'щелк', 'лимон', 'шахта',
    'марка', 'вагон', 'вокзал', 'горшок', 'шахматы', 'поле', 'часы', 'цветок', 'площадь', 'лев', 'горох', 'катер',
    'контур', 'авария', 'работа', 'карандаш', 'гроб', 'флаг', 'нос', 'бабочка', 'шарик', 'антенна', 'фрукт', 'щель',
    'дым', 'свеча', 'еж', 'фотоаппарат', 'чай', 'туман', 'ночь', 'виноград', 'фильм', 'бег', 'иллюзия', 'игла', 'этаж',
    'экран', 'амфора', 'река', 'жир', 'нож', 'осень', 'ягодка', 'палка', 'борода', 'остановка', 'капуста', 'липа',
    'трактор', 'диван', 'электроника', 'чайник', 'небо', 'ручка', 'лифт', 'час', 'плечо', 'фонарик', 'палец', 'хлопок',
    'чашка', 'майка', 'роща', 'хата', 'метеор', 'колбаса', 'топор', 'химия', 'жидкость', 'зебра', 'рыба', 'иголка',
    'фургон', 'солнце', 'алфавит', 'песок', 'лодка', 'часовщик', 'монета', 'единорог', 'сладость', 'море', 'капитан',
    'розетка', 'балерина', 'дворец', 'окно', 'облако', 'иней', 'арбуз', 'желание', 'остров', 'экспедиция', 'лапа',
    'улица', 'туча', 'фото', 'йогурт', 'плакат', 'шпагат', 'башня', 'ласточка', 'улитка', 'лиса', 'груз', 'каша',
    'дракон', 'телефон', 'магазин', 'тушь', 'деталь', 'танец', 'электрон', 'соль', 'свет', 'троллейбус', 'маяк',
    'небоскреб', 'трава', 'щетина', 'бумага', 'зуб', 'шнур', 'рак', 'график', 'борщ', 'кабан', 'парк', 'кино', 'голова',
    'молоко', 'стол', 'жердь', 'рука', 'бамбук', 'ворон', 'линия', 'улыбка', 'салют', 'клевер', 'жена', 'ягненок',
    'осьминог', 'автор', 'мед', 'носок', 'халат', 'фрукты', 'хлеб', 'шляпа', 'гитара', 'изюм', 'медведь', 'дрова',
    'задание', 'солдат', 'жук', 'ежик', 'утка', 'нитка', 'машина', 'береза', 'трамвай', 'памятник', 'рельсы', 'хвост',
    'опушка', 'чайка', 'елка', 'хор', 'новость', 'игра', 'чердак', 'балет', 'зонт', 'улей', 'желе', 'уровень', 'жираф',
    'гриб', 'замок', 'сапог', 'обувь', 'собака', 'буйвол', 'колесо', 'анализ', 'молоток', 'якорь', 'город', 'улов',
    'ворона', 'олень', 'дом', 'флейта', 'журнал', 'морковь', 'щавель', 'шланг', 'зима', 'снег', 'белок', 'искра',
    'жеребец', 'ножницы', 'плита', 'балкон', 'йог', 'метро', 'доска', 'лошадь', 'ферма', 'шоссе', 'день', 'лист',
    'шарф', 'йога', 'угол', 'шуба', 'гусеница', 'акция', 'вода', 'йод', 'автомобиль', 'цифра', 'горизонт', 'доктор',
    'щит', 'ложка', 'электричество', 'фонарь', 'электричка', 'живот', 'чернильница', 'европейка', 'щепка', 'унитаз',
    'октябрь', 'финик', 'экспонат', 'сирень', 'уголок', 'холст', 'пятка', 'дерево', 'арка', 'рюкзак', 'пещера',
    'экзамен', 'акула', 'ветер', 'ромашка', 'сахар', 'яблоко', 'кафе', 'кабина', 'диск', 'живопись', 'удочка',
    'носорог', 'укол', 'изба', 'лампа', 'воронка', 'ярмарка', 'чтение', 'сон', 'утюг', 'вихрь', 'таблетка')

your_word_is = choice(words_tuple)