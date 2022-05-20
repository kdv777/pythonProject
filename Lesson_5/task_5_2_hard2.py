# Усложнение [две звездочки]:
# С ключевым словом yield: Вычислять и возвращать само число и накопительную сумму этого и предыдущих чисел.

def iterator_with_yield(n):
    sum = 0
    for num in range(1, n+1):
       if num % 2 != 0:
           sum += num
           yield num, sum


next_gen = iterator_with_yield(14)

print(type(next_gen))
print(*next_gen)
while next_gen:
    next(next_gen)