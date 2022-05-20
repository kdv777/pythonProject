# 4. [Задача со звездочкой]: усложненный вариант задания 3.
# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и возвращающую
# словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме предыдущего задания и
# содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Условие задачи
# Техническое задание
#
# Количество передаваемых строк в функцию может быть любым. Считаем, что переданы будут только корректные строки.
# Вернуть словарь, с ключами, отсортированными в алфавитном порядке.


def thesaurus_adv(*args):
    surnames_dict = {}
    for i in sorted(args):
        # Берем первую букву в фамилии.
        first_letter = (i.split()[-1])[0]
        if first_letter not in surnames_dict:
            surnames_dict.setdefault(first_letter, [i])
        else:
            names_list = surnames_dict.get(first_letter)
            names_list.append(i)
            surnames_dict[first_letter] = names_list
        surnames_dict.setdefault(first_letter, [i])

    my_dict = {}
    for keys in surnames_dict:
        for i in surnames_dict[keys]:
            name = i.split()[0]
            first_letter = name[0]
            if first_letter not in my_dict:
                my_dict.setdefault(first_letter, [i])
            else:
                names_list = my_dict.get(first_letter)
                names_list.append(i)
                my_dict[first_letter] = names_list
            my_dict.setdefault(first_letter, [i])
        surnames_dict[keys] = my_dict
        my_dict = {}

    sorted_dict = {}
    for el in sorted(surnames_dict):
        sorted_dict[el] = surnames_dict[el]
    return sorted_dict


print(thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
           "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков"))
print()
for key, val in thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова",
           "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Василий Суриков").items():
    print(f"'{key}' : {val}")