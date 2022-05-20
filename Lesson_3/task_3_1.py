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
    result = num_dict.get(num.lower())
    return result


print(num_translate('zero', my_dict))
print(num_translate('SEveN', my_dict))
print(num_translate('TEn', my_dict))
print(num_translate('eleven', my_dict))