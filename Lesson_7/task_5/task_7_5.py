# 5. [Задача со звездочкой]: усложненный вариант задания 4. Написать скрипт,
# который для заданной папки выводит статистику размеров файлов по расширениям.
# Техническое задание
#
# Директорию с файлами 'some_data_adv' можно скачать из прикрепленных к уроку файлов.
# Результат формируется в виде словаря
# ключи — верхняя граница размера файла (пусть будет кратна 10) - как в задании 4.
# значения — списки вида '[<files_quantity>, [<files_extensions_list>]]'.
# В список '<files_extensions_list>' заносятся все расширения для файлов
# удовлетворяющих условию размера, без повторений.
# Словарь сохраните в файл '<folder_name>_summary.json' в той же папке, где запустили скрипт.

from os import walk, stat
from os.path import join

root_dir = 'some_data_adv'
# Создаем исходный список с границами и словарь-заготовку.
# При необходимости можно сгенерировать список и словарь автоматически.
sizes = [100, 1000, 10000, 100000]
dict_tmp = {100: [0, []], 1000: [0, []], 10000: [0, []], 100000: [0, []]}

for path, dirs, files in walk(root_dir):
    for file in files:
        # Получаем расширение файла.
        extens = file.split('.')[1]
        # Считаем размер файла.
        fs = stat(join(path, file)).st_size
        for size in sizes:
            if fs <= size:
                dict_tmp[size][0] += 1
                if extens not in dict_tmp[size][1]:
                    dict_tmp[size][1].append(extens)
                break

for key, value in dict_tmp.items():
    print(f'{key}: {value}')

# Был еще вариант алгоритма по аналогии task_7_4 с использованием словарей defaultdict (один int, другой list),
# но отбросил этот вариант, посчитав слияние двух словарей слишком замороченной схемой. Как вы считаете, так лучше?