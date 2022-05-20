from requests import get, utils
from datetime import datetime


def currency_rates_advanced(url_api, currency):
    """
    Функция принимает в качестве аргумента ссылку и код валюты (например, USD, EUR, GBP, ...) и возвращающую
    курс этой валюты по отношению к рублю и дату из ответа сервера.
    """
    currency = currency.upper()
    # Получаем контет от сайта.
    currency_rate = float
    response = get(url_api)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    # Составляем ключ для определения блока с валютой
    currency = f'<CharCode>{currency}</CharCode>'

    if currency in content:
        # По ключу 'Valute' составляем список с блоками валют.
        my_list = content.split('Valute')
        # Вырезаем дату.
        server_date = content.split('<ValCurs Date="')[1][:10]
        # Получаем значение даты
        datetime_obj = datetime.strptime(server_date, '%d.%m.%Y').date()
        # Получаем значение курса.
        for i in my_list:
            if currency in i:
                # Нашли нужный блок, берем значение курса.
                rate_str = i.split('Value>')
                currency_rate = f'{rate_str[1][:-2]}'
                # Надо преобразовать курс во float.
                currency_rate = float(currency_rate.replace(',', '.'))
        # Создаем кортеж и добавляем дату.
        currency_rate_data = (datetime_obj, currency_rate)
    else:
        currency_rate_data = None
    return currency_rate_data


url = "http://www.cbr.ru/scripts/XML_daily.asp"

print(currency_rates_advanced(url, "USd"))
print(currency_rates_advanced(url, "EuR"))
print(currency_rates_advanced(url, "GBP"))
print(currency_rates_advanced(url, "GBP2"))
currency_input = input('Введите код валюты (например, USD, EUR, GBP и т.п.): ')
print(currency_rates_advanced(url, currency_input))