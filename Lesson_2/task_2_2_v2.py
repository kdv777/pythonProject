# 2. Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку

my_list = ['в', '9,0', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#my_list = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
my_list = ['+9', 'примерно в', '23', 'часа', '8', 'минут', '03', '05', 'секунд', 'температура', 'воздуха', 'была', '5', 'градусов Цельсия', 'темп','воды','+2.0','градусов','Цельсия' ,'-2', '11']
new_list = my_list[:]
result_string =''
count = 0  #счетчик элементов

for i, el in enumerate(my_list):

    result = int(ord(el[0]))  #получаем код первого символа элемента, чтобы понять тип элемента (температуа, время или текст)
    if 48 <= result <= 58:    #если это цифра
        if len(el) <2: # если число однозначное, то добавляем в начало элемента 0
            new_list[count] = '0' + el
        new_list.insert(count, '"')
        new_list.insert(count+2, '"')
        count +=3

    elif result == 43 or result == 45:  #если это плюс или минус
        if '.' not in el:  # если число целое, то проверяем количество цифр
            if len(el) < 3:  # если число однозначное, то добавляем в начало элемента 0
                new_list[count] = f'{new_list[count][0]}0{new_list[count][1]}'
            new_list.insert(count, '"')
            new_list.insert(count + 2, '"')
            count += 3
        else:               # если число с точкой или запятой, то кавычки не ставим
            count += 1
    else:
        count += 1

print(new_list)   # 4.5 Новый список вывести на экран

for i, el in enumerate(new_list):
    if el == '"' and i < (len(new_list) - 1):
        next_el = new_list[i + 1] # берем следующий за кавычками элемент
        if next_el.isdigit() or next_el[0] == '+' or next_el[0] == '-': # проверяем следующий за кавычками элемент
            result_string += el
        else:
            result_string += el + ' '
    elif '.' in el:
        result_string += el + ' '
    elif el.isdigit() or el[0] == '+' or el[0] == '-':
        result_string += el
    else:
        result_string += el + ' '

print(result_string)