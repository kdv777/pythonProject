# Усложнение:
# Выполните запись результирующего словаря в файл json формата.
# Сделайте так чтобы русские буквы читались как обычный текст, без преобразования в коды unicode.
import json

with open('users.csv', 'r') as f_users, open('hobby.csv', 'r') as f_hobby:
    result = {}
    for line in f_users:
        users_str = line.strip()
        # Составляем список ФИО
        users_list = users_str.split(',')
        # Взять первые только первые буквы ФИО.
        users_str = users_list[0][0] + users_list[1][0] + users_list[2][0]
        hobbys_str = f_hobby.readline().replace('\n', '').replace(',', ';')
        if not hobbys_str:
            hobbys_str = None
        result[users_str] = hobbys_str
    if f_hobby.readline():
        print('Error code №1')

    # Записываем результат в файл json
    with open('result.json', 'w', encoding='utf-8') as f:
        # Используем параметр ensure_ascii=False, чтобы русские буквы читались, как обычный текст
        json.dump(result, f, ensure_ascii=False)
