from requests import get, utils
from datetime import datetime


def currency_rates(url_api, currency):
    """ Функция принимает в качестве аргумента ссылку и код валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю."""
    currency = currency.upper()
    currency_rate = float
    response = get(url_api)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency = f'<CharCode>{currency}</CharCode>'
    if currency in content:
        my_list = content.split('Valute')
        for i in my_list:
            if currency in i:
                rate_str = i.split('Value>')
                currency_rate = f'{rate_str[1][:-2]}'
                currency_rate = float(currency_rate.replace(',', '.'))
    else:
        currency_rate = None
    return currency_rate


def currency_rates_advanced(url_api, currency):
    """
    Функция принимает в качестве аргумента ссылку и код валюты (например, USD, EUR, GBP, ...) и возвращающую
    курс этой валюты по отношению к рублю и дату из ответа сервера.
    """
    currency = currency.upper()
    currency_rate = float
    response = get(url_api)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency = f'<CharCode>{currency}</CharCode>'

    if currency in content:
        my_list = content.split('Valute')
        server_date = content.split('<ValCurs Date="')[1][:10]
        datetime_obj = datetime.strptime(server_date, '%d.%m.%Y').date()
        for i in my_list:
            if currency in i:
                rate_str = i.split('Value>')
                currency_rate = f'{rate_str[1][:-2]}'
                currency_rate = float(currency_rate.replace(',', '.'))
        currency_rate_data = (datetime_obj, currency_rate)
    else:
        currency_rate_data = None
    return currency_rate_data