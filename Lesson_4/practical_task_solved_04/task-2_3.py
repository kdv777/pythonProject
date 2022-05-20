from requests import get, utils
import decimal as dec
from datetime import date


# Решение задачи 2 "в лоб"
def currency_rates(url, cur_name):
    """
    :param url: - Адресс с которого забираем инфу
    :param cur_name: имя валюты - строка
    :return: курс валюты тип float
    """
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    cur_name_index = content.find(cur_name.upper()) # Здесь приводим к заглавным буквам

    if cur_name_index != -1:
        # Каждое следующее значение мы ищем, начиная от предыдущего
        tag_open = content.find("<Value>",cur_name_index)
        tag_close = content.find("</Value>",tag_open)
        # Несмотря на то, что эта цифра используется один раз, правильно ее выделить в переменную и дать осмысленное имя
        tag_value_length = 7 # Длина тага <Value>
        currency = float(content[tag_open + tag_value_length : tag_close ].replace(",", "."))
        # Или так: currency_dec = dec.Decimal(currency)
        return currency

# Решение задачи 3 - усложненной. Ее также можно решить "в лоб". Но это не путь джедая.
# Т.к. примеры учебные, предположим, что нам нужны обе функции сразу (почему-то)
# Иногда нужно с датой, иногда без. Конечно можно решить общий случай и дату выкинуть.
# Но извлечение даты из ответа сервера это тоже время выполнения.

# Выделим в отдельную функцию часть алгоритма, общую для обеих функций
# Это будет извлечение курса валюты, по уже готовой строке:
def get_currency_rate_from_content(content, cur_name):
    """
    :param content: Готовая строка ответа сервера, из которой берем курс
    :param cur_name: имя валюты - строка
    :return: курс валюты тип float
    """
    cur_name_index = content.find(cur_name.upper()) # Здесь приводим к заглавным буквам

    if cur_name_index != -1:
        # Каждое следующее значение мы ищем, начиная от предыдущего
        tag_open = content.find("<Value>",cur_name_index)
        tag_close = content.find("</Value>",tag_open)
        # Несмотря на то, что эта цифра используется один раз, правильно ее выделить в переменную и дать осмысленное имя
        tag_value_length = 7 # Длина тага <Value>
        currency = float(content[tag_open + tag_value_length :
                                 tag_close ].replace(",", "."))
        # Или так: currency_dec = dec.Decimal(currency)
        return currency

# Аналогично get_currency_rate_from_content сделаем и для даты
def get_date_from_content(content):
    """
    :param content: Готовая строка ответа сервера, из которой берем курс
    :return: объект date пакета datetime
    """
    date_index = content.find("Date=")
    tag_date_length = 5
    date_length = 10
    date_str = content[ date_index + tag_date_length + 1:
                        date_index + tag_date_length + 1 + date_length]
    return [date.fromisoformat(f"{date_str[6:]}-{date_str[3:5]}-{date_str[:2]}")]


# В результате финальная функция умещается в несколько строк
# Мы не нарушили принцип DRY: у нас нет повторяющегося кода.
def currency_rates_advanced(url, cur_name):
    """
    :param url: - Адресс с которого забираем инфу
    :param cur_name: имя валюты - строка, в xml обрамлена тегами CharCode
    :return: список: дата тип datetime.date, курс валюты тип float
    """
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    currency_rate = get_currency_rate_from_content(content, cur_name )
    response_date = get_date_from_content(content)
    return response_date, currency_rate


url = "http://www.cbr.ru/scripts/XML_daily.asp"
print("------- Test currency_rates ")
print(currency_rates(url, "A"))
print(currency_rates(url, "EuR"))
print(currency_rates(url, "GBP"))
print(currency_rates(url, "GBP2"))

print("------- Test currency_rates_advanced ")
print(currency_rates_advanced(url, "US"))
print(currency_rates_advanced(url, "EuR"))
print(currency_rates_advanced(url, "GBP"))
print(currency_rates_advanced(url, "GBP2"))

currency_rates_advanced(url, "U")
currency_rates_advanced(url, "EuR")
currency_rates_advanced(url, "GBP")
currency_rates_advanced(url, "GBP2")


