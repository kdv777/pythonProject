# 1. Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield,
#  полностью истощить генератор.
# Усложнение(*):
def iterator_without_yield_1(n):
    return (i for i in range(1, n+1, 2))

# Без использования ключевого слова yield: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
def iterator_without_yield_2(n):
    return (i for i in range(1, n+1, 2) if i**2 < 200)

# gen1 = iterator_without_yield_1(11)
# next(gen1)


# 2. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield.
# Полностью истощить генератор.
def iterator_with_yield_1(n):
    for i in range(1, n+1, 2):
        yield i

# Усложнение(*):
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно),
# для чисел, квадрат которых меньше 200.
def iterator_with_yield_2(n):
    for i in range(1, n+1, 2):
        if i**2 < 200:
            yield i

# Усложнение(**):
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.
def iterator_with_yield_3(n):
    number_sum = 0
    for i in range(1, n+1, 2):
        if i**2 < 200:
            number_sum += i
            yield i, number_sum


