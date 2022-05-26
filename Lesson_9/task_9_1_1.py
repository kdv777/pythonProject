# 1. Создать класс TrafficLight (светофор).
# Тайминги передаются при создании экземпляра светофора в виде трех чисел.
# Внутри конструктора их надо соединить в единую структуру с цветами, так, чтобы было максимально понятно и лаконично.
# Ограничение на количество итераций в методе running убрать.
# Прерывание работы светофора реализовать через нажатие Crtl-C (или stop в IDE) в процессе выполнения.
# Найти какое исключение при этом возникает. Обработать его и завершить программу с выводом диагностического сообщения.

import time
from itertools import cycle


class TrafficLight:

    __color = 'off'
    colors = ['red', 'yellow', 'green', 'yellow']

    def __init__(self, duration=[7, 2, 5]):
        self.duration = duration
        self.duration.append(self.duration[1])
        self.color_dur = list(zip(self.colors, self.duration))

    def state(self, __color):
        str_color = self.__color[0]
        return str_color

    def running(self):
        # Ограничение на количество итераций в методе running убрать. Прерывание работы светофора реализовать через нажатие Crtl-C
        # (или stop в IDE) в процессе выполнения. Найти какое исключение при этом возникает. Обработать его и завершить программу
        # с выводом диагностического сообщения.
        iter_color = cycle(self.color_dur)
        while True:
            try:
                self.__color = next(iter_color)
                # print(self.__color[0])
                print(TrafficLight.state(self, self.__color[0]))
                time.sleep(self.__color[1])
            except KeyboardInterrupt:
                print('Светофор был выключен пользователем.')
                break
        return self.__color


trafficLight1 = TrafficLight([1, 2, 3])
trafficLight1.running()
