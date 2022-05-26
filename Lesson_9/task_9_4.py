# 4. Реализуйте класс Car (машина).
# Техническое задание:
#
# атрибуты: speed, color, name, 'is_police': (булево). speed - текущая скорость машины. Внимательно
# по отношению выбора атрибут класса/экземпляра.
# методы: go, stop, turn(direction), которые должны сообщать(выводить на экран), что машина поехала, остановилась,
# повернула (куда). turn(direction) - метод, принимающий параметр: направление поворота.
# Сами определите как вызов этих методов меняет скорость машины. На ваше усмотрение.
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar
# добавьте в базовый класс Car метод show_speed, который должен показывать текущую скорость автомобиля
# для классов TownCar и WorkCar переопределите метод 'show_speed'.
# При значении скорости машины свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Ограничения на скорость - очевидно данные. Где их нужно хранить?
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:

    speed = 0
    is_police = False
    speed_limit = 0

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def go(self, accelerate=0):
        print(f"Машина {self.color} {self.name} поехала")
        self.speed += accelerate

    def stop(self):
        print(f"Машина {self.color} {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.color} {self.name} повернула {direction}")

    def show_speed(self):
        print(f'Скорость машины {self.color} {self.name} {self.speed} км/ч')


class TownCar(Car):
    speed_limit = 60

    def show_speed(self):
        self.speed_limit = 60
        if self.speed > self.speed_limit:
            print(f'Превышение скорости 60 км/ч!!! Скорость машины {self.color} {self.name} {self.speed} км/ч')
        else:
            print(f'Скорость машины {self.color} {self.name} {self.speed} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):
    speed_limit = 40

    def show_speed(self):
        if self.speed > self.speed_limit:
            print(f'Превышение скорости 60 км/ч!!! Скорость машины {self.color} {self.name} {self.speed} км/ч')
        else:
            print(f'Скорость машины {self.color} {self.name} {self.speed} км/ч')


class PoliceCar(Car):
    is_police = True


x = Car("белая", "Тойота")
print(x.color, x.name)
x.go(20)
x.turn("налево")
x.stop()
x.show_speed()
x.go(30)
z = WorkCar("зеленая", "Volvo")
z.go(50)
z.show_speed()
