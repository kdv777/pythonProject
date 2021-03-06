from sys import argv

# argv = ["dssd","3","596"]
len_argv = len(argv)
if len_argv < 3:
    print("Не передан номер записи или новая запись")
    exit(1)

# очевидный алгоритм такой задачи - "спасти хвост файла", 
#   по строкам доходим до нужной записи/строки (без запоминания)
#   считываем хвост файла после нужной записи - например в список 
#   меняем нужную запись  .write(...)
#   записываем хвост обратно в файл
#   Формально все честно - файл в память целиком не считывается. И мы избежали затирания последующих записей

#  Тут рассмотрим другой алгоритм: Примем что на запись мы выделяем определенное кол-во символов. 
# Часть из них будут цифрами, остальное - пробелами.
# Конечно надо определить сколько символов нужно. Для булочной сумма продаж вряд ли больше пятизначного числа.
# Этим и ограничимся. Но мы легко поменяем это число 
# Т.е. для ЛЮБОЙ записи мы выделяем 5 символов. Это позволит избежать затирания последующих записей.
# Фактически мы будем затирать пробелы текущей записи

# Это ограничение скрипта, т.е. значения записей не должны быть более 5 цифр
record_length = 5
# Здесь +2 это из двух символов в конце строки
line_length = record_length + 2

number = int(argv[1])
record_new = argv[2]
record_position = 0 + (number-1)*line_length

with open("bakery.csv", encoding="UTF-8", mode="r+") as file:
    # Так определим последнюю позицию в файле => кол-во записей
    # нетривиальная задача, найти в документации, что это означает
    end_of_file = file.seek(0, 2)
    if record_position <= end_of_file - line_length:
        file.seek(record_position)
        file.write(f"{record_new:>5s}\n")
    else:
        print("Incorrect record number")



