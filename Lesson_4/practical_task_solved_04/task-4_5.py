from sys import argv
from utils import currency_rates

# Задача 4 здесь элементарно: currency_rates доступна
#url = "http://www.cbr.ru/scripts/XML_daily.asp"
#print("------- Test currency_rates ")
#print(currency_rates(url, "USd"))
#print(currency_rates(url, "EuR"))
#print(currency_rates(url, "GBP"))
#print(currency_rates(url, "GBP2"))

# Задача 5.
# Лучше избежать сообщений об ошибках в командной строке.
# Будем считать, что наш скрипт предназначен для работы пользователя
# а не для запуска как последовательности скриптов, т.о.
#   1) exit() нам не нужен
#   2) Сделаем обработку вводимых данных и сообщения
#       Вообще без параметров запустили скрипт
#       Передали некорректный код валюты, тут None не подойдет


if len(argv) == 1:
    print("Код валюты не введен")
else:
    # Ради интереса сделаем обработку множества переданных валют
    # Хотя функция currency_rates для этого не подходит,
    # ведь запрос будет сделан каждый раз, а это время выполнения
    for idx in range(1,len(argv)): # Нам нужен не весь список, первый элемент выкинуть
        cur_name = argv[idx]
        cur_rates = currency_rates('http://www.cbr.ru/scripts/XML_daily.asp', cur_name)
        if cur_rates is  None:
            cur_rates = "Не найдена валюта"
        print(f"{cur_name:>10s}: {cur_rates}")





