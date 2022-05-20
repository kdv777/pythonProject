from sys import argv

def show_lines(file, begin = None, end = None):
    """
    Функция для вывода на экран нужных строк файла
    file - файловый объект
    begin - индикатор первой записи:    число или None, если не учитываем
    end   - индикатор последней записи: число или None, если не учитываем
    """
    # В этой функции мы используем несколько интересных моментов:
    # 1.Параметры begin,end могут принимать разные типы данных.
    # Функция корректно обрабатывает число или None
    # Так удобнее: если begin не нужен - просто передадим None. Если нужен - число
    # Но цена такой динамической типизации - нам надо корректно проверять, что передали в функцию.
    #
    # 2. Условные выражения выносим в отдельные переменные, т.к. они достатоно громоздки
    # 3. is_begin_norm/is_end_norm
    #   Если передан None ИЛИ (передан не None и индекс в нужных пределах)
    #   Обратите внимание на порядок проверок в переменных is_begin_norm, is_end_norm
    #   та часть, которая в скобках. Попробуйте поменять местами проверки
    #   и запустить скрпит без параметров - будет ошибка сравнения:
    #   unsupported operand type(s) for -: 'NoneType' and 'int'
    #   Здесь мы используем свойство "ленивости" оператора сравнения
    #   Об этом надо почитать отдельно, что такое ленивость в принципе

    #   Для оператора сравнения коротко это выглядит так:
    #   Если условные выражения соединены оператором and
    #   и первое из них ложь, то второе выражение даже проверяться не будет, т.к. смысла нет.

    for idx, line in enumerate(file):
        is_begin_norm = (begin is not None and idx >= begin-1) or begin is None
        is_end_norm = (end is not None and idx <= end-1) or end is None
        if is_begin_norm and is_end_norm:
            print(line.strip())

# Чтобы не отлаживать в консоли, можно делать так:
# argv = ["bla-bla-bla"]
# argv = ["bla-bla-bla",1]
# argv = ["bla-bla-bla",1,3]
len_argv = len(argv)


with open("bakery.csv", encoding="UTF-8", mode="rt") as file:
    if len_argv == 1:
        print("Show all records:")
        show_lines(file, begin = None, end = None)
    elif len_argv == 2:
        record_begin = int(argv[1])
        print(f"Show records from record {record_begin}:")
        show_lines(file, begin = record_begin, end = None)
    else:
        record_begin = int(argv[1])
        record_end = int(argv[2])
        print(f"Show records from record {record_begin} to record {record_end}")
        show_lines(file, begin = record_begin, end = record_end)