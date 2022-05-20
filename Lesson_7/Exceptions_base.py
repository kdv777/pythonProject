from math import sqrt


# - Вычислить сумму двух чисел
# - Каждое из которых - решение уравнения $ax^2 + b = 0$ и  $ax^2 + с = 0$
# - Параметры: a - одинаковое, b,c - различные
# - Занести в список решения для заданых (a,b,c)
# - Обработка ошибок:
  # - ZeroDivisionError - использовать "zero"
  # - ValueError - использовать "comlex"
  # - Возможно что-то еще в будущем: При корне меньшем, чем 0.1 использовать "inf"


# Только код для выполнения задачи
# Выкидывает исключения ZeroDivisionError, ValueError в случае неправильных данных

# def mult_solve(a, b):
#     return sqrt(-b/a)
#
#
# def global_solve(a, b, c):
#     r1 = mult_solve(a, b)
#     r2 = mult_solve(a, c)
#     return round(r1 + r2, 2)
#
#
# def list_fill_value():
#     lst = list()
#     # for a,b,c in [(a, b, c) for a in range(0,200,25) for b in [-2,-1] for c in [-3,1]]: - будут исключения
#     # for a,b,c in [(a, b, c) for a in [1,3] for b in [-2,-1] for c in [-3,-1]]: - не будет исключений
#     for a,b,c in [(a, b, c) for a in [1,3] for b in [-2,-1] for c in [-3,-1]]:
#         rez = global_solve(a, b, c)
#         lst.append(rez)
#     return lst
#
# print(list_fill_value())


#  --------------------------------------------------------------------------------------------------------
# Код в стиле LBYL: "Look Before You Leap"
# Перед выполнением действий проверяем на возможные ошибки

def mult_solve(a, b):
    # Возвращаем статусы "ошибок" когда значение вернуть не можем.
    # "Обходим" возникновение исключений ZeroDivisionError, ValueError
    if a == 0:
        return "zero"
    if b / a > 0:
        return "complex"
    return sqrt(-b/a)


def global_solve(a, b, c):
    r1 = mult_solve(a, b)
    r2 = mult_solve(a, c)
    # Вынуждены "протаскивать" наверх статусы ошибок.
    # В этой функции мы еще не знаем, как их обработать (в нашей задаче не знаем, в принципе можем и знать)
    if r1 == "zero" or r2 == "zero":
        return "zero"
    if r1 == "complex" or r2 == "complex":
        return "complex"
    return round(r1 + r2, 2)


def list_fill_value():
    lst = list()
    for a,b,c in [(a, b, c) for a in range(0,200,25) for b in [-2,-1] for c in [-3,1]]:
        rez = global_solve(a, b, c)
        # Только здесь (в нашей задаче) мы можем обработать ошибки
        if rez =="zero":
            lst.append(None)
        elif rez == "complex":
            lst.append("complex")
        else:
            lst.append(rez)
    return lst

print(list_fill_value())

#  --------------------------------------------------------------------------------------------------------
# Код в стиле EAFP: "Easier to Ask for Forgiveness than Permission"
# Делай, будут проблемы - будем разбираться.
# Использование исключений

# def mult_solve(a, b):
#     # Исключения ZeroDivisionError, ValueError возникают здесь. Здесь не делаем ничего
#     # return sqrt(-b/a)
    if rez <= 0.1:
        # Это пример поднятия исключения самостоятельно. 
        # это избавляет нас от той же трудности: "протащить" статус rez <= 0.1 до места формирования списка.
        # Надо понимать, что с точки зрения python это не ошибка, мы делаем ее исключительной/ошибочной, чтобы нам было удобно.
        raise OverflowError  
    return rez
#
#
# def global_solve(a, b, c):
#     r1 = mult_solve(a, b)
#     r2 = mult_solve(a, c)
#     return round(r1 + r2, 2)
#
#
# def list_fill_value():
#     lst = list()
#     for a,b,c in [(a, b, c) for a in range(0,200,25) for b in [-2,-1] for c in [-3,1]]:
#         # Только здесь (в нашей задаче) мы можем обработать ошибки
#         # Но обработка через try-exept
#         try:
#             rez = global_solve(a, b, c)
#             lst.append(rez)
#         except ZeroDivisionError:
#             lst.append(None)
#         except ValueError:
#             lst.append("complex")
#         except OverflowError:
#             lst.append("inf")
#
#     return lst
#
# print(list_fill_value())


