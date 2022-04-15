# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

procent = {
    '1': 'процент',
    '2': 'процента',
    '3': 'процента',
    '4': 'процента',
    '5': 'процентов',
    '6': 'процентов',
    '7': 'процентов',
    '8': 'процентов',
    '9': 'процентов',
    '0': 'процентов',
    '11': 'процентов',
    '12': 'процентов',
    '13': 'процентов',
    '14': 'процентов',
    }
while True:
    number = input('Введите количество процентов: ')
    if number in procent:
        print(number, procent[number])
    elif number[-1] in procent:
        print(number, procent[number[-1]])
    else:
        print('Ошибка ввода процентов!')
