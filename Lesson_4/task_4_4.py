from utils import currency_rates_advanced, currency_rates

print(currency_rates("http://www.cbr.ru/scripts/XML_daily.asp", "eur"))

print(currency_rates_advanced("http://www.cbr.ru/scripts/XML_daily.asp", "eur"))