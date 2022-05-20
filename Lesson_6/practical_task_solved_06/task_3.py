# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
# Известно, что при хранении данных используется принцип:
# одна строка — один пользователь, разделитель между значениями — запятая.
#
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл.
# Проверить сохранённые данные.
# Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
# Если наоборот — формируем словарь, исходя количества ФИО  и выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# ```
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# ```
# ### Фрагмент файла с данными о хобби  (hobby.csv):
# ```
# скалолазание,охота
# горные лыжи

import json

def initials(fio):
    """
    :param fio: массив строк вида ["Фамилия","Имя","Отчество"]
    :return: строка инициалов ФИО
    """
    fio = fio.strip().split(",")
    return "".join([fio[0][0], fio[1][0], fio[2][0]])

with open("task_3_4_FIO.txt",encoding="UTF-8", mode="rt") as file_fio:
    fio_data = file_fio.readlines()
with open("task_3_4_hobby.txt",encoding="UTF-8", mode="rt") as file_hobby:
    hobby_data = file_hobby.readlines()

fio_data_len = len(fio_data)
hobby_data_len = len(hobby_data)
dict_man3 = {}

# Запишем все в один цикл, используем максимум из двух длин
# тогда придется делать проверки:
# Индекс выйдет за пределы какого списка
for idx in range(max(fio_data_len, hobby_data_len)):
    if idx > fio_data_len-1:
        exit(1)
    if idx > hobby_data_len-1:
        value = None
    else:
        value = hobby_data[idx].strip().replace(",",";")
    fio = fio_data[idx]
    dict_man3[initials(fio)] = value


print(dict_man3)
# Сериализацию в Json никто не требовал
with open("task_3_4_output.txt",encoding="UTF-8", mode="wt") as file_out:
    file_out.write(str(dict_man3))

# И в json
with open("task_3_4_output.json",encoding="UTF-8", mode="wt") as file_out:
    json.dump(dict_man3, file_out, indent=4, ensure_ascii = False)


