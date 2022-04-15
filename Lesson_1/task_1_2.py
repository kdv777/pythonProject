# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

cube_list = []
sum_div_7 = 0
sum_number = 0

for i in range(1, 1001):
    if i % 2 != 0:
        cube_number = i ** 3
        cube_list.append(cube_number)
        string_number = str(cube_number)

        for x in string_number:
            sum_number += int(x)
        if sum_number % 7 == 0:
            print(f'сумма цифр числа {cube_number} равна {sum_number} делится на 7 без остатка')
            sum_div_7 += cube_number
        sum_number = 0

print('список, состоящий из кубов нечётных чисел от 1 до 1000', cube_list)
print('Сумма чисел, сумма цифр которых делится нацело на 7: ', sum_div_7)

sum_div_7 = 0

# Решаем задачу под пунктом b, не создавая новый список

for i in cube_list:
    string_number = str(i + 17)

    for x in string_number:
        sum_number += int(x)
    if sum_number % 7 == 0:
        print(f'сумма цифр числа {string_number} равна {sum_number} делится на 7 без остатка')
        sum_div_7 += int(string_number)
    sum_number = 0
    string_number = 0
print('b) Сумма чисел, сумма цифр которых делится нацело на 7: ', sum_div_7)