from requests import get, utils
import decimal as dec


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

if __name__ == "__main__":
    # Этот код оставляем для проверки того,насколько правильно импортируем
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    print("------- Test currency_rates ")
    print(currency_rates(url, "USd"))
    print(currency_rates(url, "EuR"))
    print(currency_rates(url, "GBP"))
    print(currency_rates(url, "GBP2"))