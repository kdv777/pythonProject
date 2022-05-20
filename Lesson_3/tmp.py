# 6. [Задача со звездочкой]: усложненный вариант задания 5.
# Условие задачи
# Техническое задание
#
# Добавьте в функцию еще один аргумент, разрешающий или запрещающий повторы слов в шутках: каждое слово можно использовать
# только в одной шутке. Тогда этот параметр логично сделать типом boolean.
# Функция должна вернуть список строк-шуток сколько потребовали или сколько получилось из условия уникальности.
# Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается только один раз.

from random import randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num, list_1, list_2, list_3, uniq=False):
    """
    Функция, возвращающая n шуток, сформированных из трех случайных слов, взятых из трёх заданных списков.
    uniq - если True, то используем уникальные слова.
    """
    jokes = []
    uniq_str = []
    # Вычисляем максимальное возможное количество шуток и если входной параметр больше, то присваеваем ему макс. возм. число
    if uniq and (num > len(list_1) or num > len(list_2) or num > len(list_3)):
        num = sorted([len(list_1), len(list_2), len(list_3)])[0]
        print('Максимальное количество уникальных шуток = ', num)


    for i in range(num):
        if not uniq:
            joke_str = f'{list_1[randrange(len(list_1))]} {list_2[randrange(len(list_2))]} {list_3[randrange(len(list_3))]}'
        else:
            joke_1 = list_1[randrange(len(list_1))]
            while joke_1 in uniq_str:
                joke_1 = list_1[randrange(len(list_1))]
            uniq_str.append(joke_1)

            joke_2 = list_2[randrange(len(list_2))]
            while joke_2 in uniq_str:
                joke_2 = list_2[randrange(len(list_2))]
            uniq_str.append(joke_2)

            joke_3 = list_3[randrange(len(list_3))]
            while joke_3 in uniq_str:
                joke_3 = list_3[randrange(len(list_3))]
            uniq_str.append(joke_3)
            joke_str = f'{joke_1} {joke_2} {joke_3}'

        jokes.append(joke_str)
    return jokes


print(get_jokes(6, nouns, adverbs, adjectives))
print()

print(get_jokes(7, nouns, adverbs, adjectives, uniq=True))
print()

print(*get_jokes(4, list_1 = ["автомобиль", "лес", "огонь", "город", "дом"],
    list_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
    list_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"], uniq=True), sep='\n')
print()
for i in get_jokes(3, nouns, adverbs, adjectives):
    print(i)
print()
print('\n'.join(get_jokes(2, nouns, adverbs, adjectives, uniq=True)))
