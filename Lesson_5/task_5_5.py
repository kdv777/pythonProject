# 5. Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
# Техническое задание
# Здесь нет условия создавать итератор/генератор или comprehensions.
# Сохранение исходного порядка в результирующем списке обязательно.
# Не используйте Counter из модуля collections или аналогичные.

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# 1) Вариант решения "в лоб" (т.к. вложенный цикл - очень низкая производительность при больших списках).  (Сложность O(N2)?):
result = []
for num in range(len(src)):
    count = 0
    for i in range(len(src)):
        if src[i] == src[num]:
            count += 1
    if count == 1:
        result.append(src[num])
print('result1 = ', result)

print([num for num in src if src.count(num) == 1])

# 2) Вариант решения c использованием методов множества и сравнением исходного списка со множеством.
# Получаем всего 2 цикла + проверки in. Сложность O(N) вместо O(N2) или другая?
uniq_nums = set()
for el in src:
    if el not in uniq_nums:
        uniq_nums.add(el)
    else:
        uniq_nums.discard(el)

#  Сравнаем исходный список и элементы множества. Создаем новый список
new_src = []
for num in range(len(src)):
    if src[num] in uniq_nums:
        new_src.append(src[num])
print('result2 = ', new_src)

# 3) тоже что и 2) но с использованием Comprehension
uniq_nums = set()
for el in src:
    if el not in uniq_nums:
        uniq_nums.add(el)
    else:
        uniq_nums.discard(el)
new_src_comp = [src[num] for num in range(len(src)) if src[num] in uniq_nums]
print('result3 = ', new_src_comp)

# 4) Вариант решения методами списков. По тестам в 10 раз быстрее варианта 1) и на 50% быстрее варианта 2)
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniq_list = []
for el in src:
    if el not in uniq_list:
        uniq_list.append(el)
    else:
        uniq_list.remove(el)
print('result4 = ', uniq_list)
