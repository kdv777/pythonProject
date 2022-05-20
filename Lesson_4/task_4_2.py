from requests import get, utils


def currency_rates(url_api, currency):
    """ Функция принимает в качестве аргумента ссылку и код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю."""
    currency = currency.upper()
    # Получаем контет от сайта.
    # currency_rate = float
    response = get(url_api)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    # Парсим строку, ищем валюту, есть как минимум пара вариантов:
    # 1) составить словарь валют с их курсами?  но делать это при каждом запросе нерационально
    # 2) вырезать блок с нужной валютой <CharCode>+currency</CharCode> и получить значения. Выбираем этот вариант.

    # Составляем ключ для определения блока с валютой.
    currency = f'<CharCode>{currency}</CharCode>'
    if currency in content:
        # По ключу 'Valute' составляем список с блоками валют.
        my_list = content.split('Valute')
        print(my_list)
        for i in my_list:
            if currency in i:
                # Нашли нужный блок, берем значение курса.
                rate_str = i.split('Value>')
                currency_rate = f'{rate_str[1][:-2]}'
                # Надо преобразовать курс во float.
                currency_rate = float(currency_rate.replace(',', '.'))
    else:
        currency_rate = None
    return currency_rate


url = "http://www.cbr.ru/scripts/XML_daily.asp"

print(currency_rates(url, "USd"))
print(currency_rates(url, "EuR"))
print(currency_rates(url, "GBP"))
print(currency_rates(url, "GBP2"))
currency_input = input('Введите код валюты (например, USD, EUR, GBP и т.п.): ')
print(currency_rates(url, currency_input))