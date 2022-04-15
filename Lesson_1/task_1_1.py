### 1. Реализовать вывод информации о промежутке времени в зависимости
# от его продолжительности duration в секундах:
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

duration = 400153

if duration < 60:
    print(duration, 'сек')
elif duration < 3600:
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин', seconds, 'сек')
elif duration < 86400:
    hours = duration // 3600
    minutes = (duration - hours * 3600) // 60
    seconds = duration % 60
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    days = duration // 86400
    hours = (duration - days * 86400) // 3600
    minutes = (duration - days * 86400 - hours * 3600) // 60
    seconds = duration % 60
    print(days, 'дн',  hours, 'час', minutes, 'мин', seconds, 'сек')