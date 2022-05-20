# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield. Полностью истощить генератор.
# Техническое задание
# Все пункты ТЗ задания 1 остаются в силе.
# Отличие от задания 1 - только в использовании yield.


def iterator_with_yield(n):
    for num in range(1, n + 1, 2):
        # можно с шагом 2, а можно с условным оператором
        # if num % 2 != 0:
        yield num


next_gen = iterator_with_yield(11)
print(type(next_gen), *next_gen)
while next_gen:
    next(next_gen)
