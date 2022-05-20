# 3. Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
# 'директор аэлита']. Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Техническое задание
#
# Список может содержать произвольное количество элементов.
# Имя сотрудника - всегда последнее слова в строке. Может содержать заглавные или строчные буквы в любом порядке.
# В результате имя сотрудника пишется строчными буквами и первая буква - заглавная.

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in my_list:
    name = (i.split()[-1]).capitalize()
    # name = name.capitalize()
    print(f'Привет, {name}!')



print('\n', 'усложненный вариант', '\n')

for i in my_list:
    name = i.split()[-1]
    name = name.capitalize()
    position_list = i.split()[0: -1]
    position = ''
    for el in position_list:
        position = position + el + ' '

    print(f'Привет, {position}{name}!')


print('\n', 'усложненный вариант #2', '\n')

for i in my_list:
    my_string  = i.split()
    name = (my_string[-1]).capitalize()
    pos = " ".join(my_string[0: -1])
    print(f'Привет, {pos} {name}!')
