# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv, которая корректно
# обработает числительные, начинающиеся с заглавной буквы. Если перевод сделать невозможно, вернуть объект None.
# Техническое задание
# Функция возвращает строку перевод. Или возвращает None, если перевести невозможно.
# Считаем, что только первая буква может быть заглавной.
# Обратите внимание, что функция возвращает перевод в том же регистре как и приняла.
# Выполнить вызов функции для нескольких слов и вывести на экран результаты.

my_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate(num, num_dict):
    """ Переводит числительные от 0 до 10 c английского на русский язык. """
    num_dict_low = num_dict.get(num.lower())
    if not num_dict_low or not num.istitle():
        result = num_dict_low
    else:
        result = num_dict_low.title()
    return result


print(num_translate('One', my_dict))
print(num_translate('seven', my_dict))
print(num_translate('Two', my_dict))
print(num_translate('Eleven', my_dict))