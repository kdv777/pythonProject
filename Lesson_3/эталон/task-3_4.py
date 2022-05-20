# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи – первые буквы имен,
# а значения – списки, содержащие имена, начинающиеся с соответствующей буквы. Например:
# thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"],
#     "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки.
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

# Используем структуру *args, т.к. заранее неизвестно сколько имен будет в аргументах функции
def thesaurus(*args):
    rez_dict = dict()
    for name in args:
        first_char = name[0]
        if first_char in rez_dict:
            rez_dict[first_char].append(name)   # Если такая буква уже есть - добавляем имя в список
        else:
            rez_dict[first_char] = [name]       # Если такой буквы еще нет - создаем список с одним именем

    # Возвращаем отсортированный по ключам словарь
    sort_dict = dict()
    for key in sorted(rez_dict): # можно и явно указать sorted(rez_dict.keys())
        sort_dict[key] = rez_dict[key]
    return sort_dict


print("Часть 1. Только имена:")
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Кирилл", "Андрей"))


# 4. *(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# “Имя Фамилия” и возвращающую словарь, в котором ключи – первые буквы фамилий, а значения – словари,
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": "[Петр Алексеев]"
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Сможете ли вы вернуть отсортированный по ключам словарь?


def thesaurus_adv(*args):
    rez_dict = dict()
    for person in args:
        name, surname = person.split()
        first_char_name = name[0]
        first_char_surname = surname[0]
        # Буква-фамилии встретилась первый раз - создаем для нее словарь
        if first_char_surname not in rez_dict.keys():
            rez_dict[first_char_surname] = {}
        # Здесь ПО ЛЮБОМУ словарь для буквы-фамилии уже создан.
        # Создаем список для буквы-имени - если раньше не встречалась
        if first_char_name not in rez_dict[first_char_surname].keys():
            rez_dict[first_char_surname][first_char_name] = []
        # Здесь ПО ЛЮБОМУ словарь для буквы-фамилии и список для буквы-имени уже созданы. Спокойно добавляем.
        rez_dict[first_char_surname][first_char_name].append(person)
    # Сортируем по Буква-фамилии и буква-имени
    sort_dict = dict()
    for surname in sorted(rez_dict.keys()):
        sort_dict[surname] = {}
        for name in sorted(rez_dict[surname].keys()):
            sort_dict[surname][name] = rez_dict[surname][name]
    return sort_dict


print("\nЧасть 2. Имена и фамилии:")
persons = ["Иван Сергеев", "Алла Сидорова", "Инна Серова",
           "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков"]
#  распаковка - это удобно
rez = thesaurus_adv(*persons)
for p_surname in rez.keys():
    print(p_surname, ":")
    for p_name in rez[p_surname].keys():
        print(f"\t{p_name}: {rez[p_surname][p_name]}")
