# 5. [Задача со звездочкой]: усложненный вариант задания 4.
# Добавить возможность редактирования данных при помощи отдельного скрипта.


def edit_sale(argv):
    """
    аргумент 1 это номер редактируемой строки. 0 - последняя строка, -1 предпоследняя
    аргумент 2 это новое значение
    """
    if len(argv) == 3 and argv[1].isdigit():
        my_list = []
        count = 0
        path1 = join('.', 'task_4', 'bakery.csv')
        with open(path1, 'r', encoding='utf-8') as f:
            for el in f:
                my_list.append(el.strip())
                # Считаем количество строк в файле.
                count += 1
            # проверка на неправильный ввод номера строки.
            if int(argv[1]) > count:
                print('Ошибка ввода строки! ')
                exit()
            # Изменяем нужную строку на заданное значение
            old_sum = my_list[int(argv[1]) - 1]
            my_list[int(argv[1]) - 1] = argv[2]

        with open(path1, 'w', encoding='utf-8') as f:
            for el in my_list:
                f.write(el + '\n')
            print(f'Запись {argv[1]} изменена c {old_sum} на {argv[2]}')
    else:
        print('Ошибка ввода строки! ')
    return


if __name__ == '__main__':
    from sys import argv, exit
    from os.path import join

    exit(edit_sale(argv))
