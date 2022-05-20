
# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200. Все остальное как в основном задании.

def iterator_without_yield_sqr_less_200(n):
    return (num for num in range(1, n+1) if num % 2 != 0 and num * num < 200)


next_gen = iterator_without_yield_sqr_less_200(20)
print(type(next_gen), *next_gen)
while next_gen:
    next(next_gen)


