tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

len_groups = len(groups)
gen_tuple = ((tutors[x], groups[x]) if x < len_groups else (tutors[x], 'None') for x in range(len(tutors)))
print(type(gen_tuple))
print('1) учеников меньше: ', *gen_tuple)

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В'
]

len_groups = len(groups)
gen_tuple = ((tutors[x], groups[x]) if x < len_groups else (tutors[x], 'None') for x in range(len(tutors)))
print(type(gen_tuple))
print('2) учеников больше: ', *gen_tuple)

# Вариант 2) Делаем через функцию.

len_groups = len(groups)


def gen_tuple_func(tutors, groups):
    for x in range(len(tutors)):
        if x < len_groups:
            yield (tutors[x], groups[x])
        else:
            yield (tutors[x], 'None')


next_tuple = gen_tuple_func(tutors, groups)
print(type(next_tuple))
print('3) функция: ', *next_tuple)
