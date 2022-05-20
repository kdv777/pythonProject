def main(argv):
    if len(argv) == 1 or len(argv) > 2:
        print('argv = ', argv)
        print('len(argv) = ', len(argv))
        return "Ошибка. Не указана валюта или указана не корректно!"
    else:
        program, arg = argv
        result = currency_rates("http://www.cbr.ru/scripts/XML_daily.asp", arg)
        if result:
            print(f'{arg}: {result}')
        else:
            print(f'{arg}: Не найдена валюта')

    return 0


if __name__ == '__main__':
    from utils import currency_rates_advanced, currency_rates
    import sys

    exit(main(sys.argv))