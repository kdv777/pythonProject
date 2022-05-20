# получить список кортежей вида: (<remote_addr>, <request_type>,
# <requested_resource>).
# Например:
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

# Можно получить данные с сайта:
# from requests import get, utils
#
# response = get('https://github.com/elastic/examples/raw/master/
# Common%20Data%20Formats/nginx_logs/nginx_logs')
# encodings = utils.get_encoding_from_headers(response.headers)
# content = response.content.decode(encoding=encodings)
# print(content)

result = []
f = open('nginx_logs.txt', mode='r', encoding='utf-8')
for line in f:
    # парсим по разделютелю кавычки (как вариант можно по пробелам).
    my_list = line.split('"')
    # создаем кортеж из элементов.
    my_tuple = (my_list[0].split(' '))[0], ((my_list[1].split(' '))[0]), ((my_list[1].split(' '))[1])
    # Добавляем кортеж в итоговый список.
    result.append(my_tuple)
print(*result, sep='\n')
f.close()
