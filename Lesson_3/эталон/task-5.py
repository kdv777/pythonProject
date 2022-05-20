# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#             Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import choice, sample

def get_jokes_simple(joke_number, lst1, lst2, lst3):
    """
    random create list of joke string from three list of string, WITHOUT unique
    :param joke_number: number of jokes
    :param lst1: first words for joke
    :param lst2: second words for joke
    :param lst3: third words for joke
    :return: list of joke(str)
    """

    # Простой алгоритм: выбираем случайное слово из каждого списка.
    jokes_list = []
    for i in range(joke_number):
        jokes_list.append(f"{choice(lst1)} {choice(lst2)} {choice(lst3)}")
    return jokes_list


def get_jokes_unique(joke_number, lst1, lst2, lst3, unique=False):
    """
    random create list of joke string from three list of string
    :param joke_number: number of jokes
    :param lst1: first words for joke
    :param lst2: second words for joke
    :param lst3: third words for joke
    :param unique: use only unique words in jokes
    :return: list of joke(str)
    """
    # Вариант 1.
    # Требуемый алгоритм можно реализовать с помощью choice,
    # тогда выбранное слово надо сразу удалять из списка(метод remove), чтобы оно не было выбрано еще раз.
    # Списки lst1, lst2, lst3 менять нельзя, т.к. это параметры и получим side effects
    # Придется создавать копию списков.
    # Если при этом joke_number сильно меньше длины списков lst1, lst2, lst3,
    # т.е. если слов много, а шуток нужно мало, то мы скопируем кучу лишних данных
    # т.о. алгорит может быть не эффективен.

    # Вариант 2.
    # Очевидно, что шуток будет не больше, чем длина самого короткого списка
    # Сразу готовим списки нужной длины. Просто обрезать нельзя - потеряем часть случайного выбора, хоть и не весь
    # Используем random.sample
    if unique:
        min_lenght = min(joke_number, len(lst1), len(lst2), len(lst3))
        lst1_ready = sample(lst1, min_lenght)
        lst2_ready = sample(lst2, min_lenght)
        lst3_ready = sample(lst3, min_lenght)
    else:
        # Если требований на уникальность нет, то можно просто взять алгоритм get_jokes_simple
        # Но в качестве учебного примера, пойдем другим путем: перемешаем списки
        lst1_ready = sample(lst1, len(lst1))
        lst2_ready = sample(lst2, len(lst2))
        lst3_ready = sample(lst3, len(lst3))
    # Но теперь choice не нужен: все уже случайно перемешано.
    total_jokes = zip(lst1_ready,lst2_ready,lst3_ready)
    # Если вы не знаете, что делают функции zip и join - поищите сами.
    jokes_list = []
    for joke in total_jokes:
        jokes_list.append(" ".join(joke))
    return jokes_list

def print_jokes(joke_list):
    for joke in joke_list:
        print(joke)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print("\n=== 3 Jokes")
print_jokes(get_jokes_simple(joke_number=3, lst1=nouns, lst2=adverbs, lst3=adjectives))
print("\n=== 8 Jokes")
print_jokes(get_jokes_simple(8, nouns, adverbs, adjectives))
print("\n=== 8 Unique Jokes")
print_jokes(get_jokes_unique(8, nouns, adverbs, adjectives, unique=True))

