def thesaurus(*args):
    """
    Функция, принимающая в качестве аргументов имена сотрудников и возвращающая словарь,
    в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
    """
    names_dict = {}
    for i in sorted(args):
        first_letter = i[0]
        if first_letter not in names_dict:
            names_dict.setdefault(first_letter, [i])
        else:
            # Наверное это дубовый вариант добавления дополнительного имени в значение словаря?
            # names_list = names_dict.get(first_letter)
            names_dict.get(first_letter).append(i)
            # names_dict[first_letter] = names_list
        names_dict.setdefault(first_letter, [i])
    return names_dict


print(thesaurus("Иван", "Андрей", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий"))
print()
for key, val in thesaurus("Иван", "Андрей", "Мария", "Петр", "Илья", "Артем", "Вадим", "Анатолий").items():
    print(f"'{key}': {val}")