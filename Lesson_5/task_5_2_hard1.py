# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат
# которых меньше 200.


def iterator_with_yield_sqr_less_200(n):
    for num in range(1, n + 1):
        if num % 2 != 0 and num * num < 200:
            yield num


next_gen = iterator_with_yield_sqr_less_200(20)
print(type(next_gen), *next_gen)
while next_gen:
    next(next_gen)
