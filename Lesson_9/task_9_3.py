# 3. Реализовать класс Worker (работник).
# Техническое задание:
#
# определить атрибуты: name, surname, position (должность), income (доход)
# атрибут income должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, '{"wage": wage, "bonus": bonus}'
# При создании экземпляра параметры wage, bonus передаются как числа.
# создать класс Position (должность) на базе класса Worker. Это наследование.
# в классе Position реализовать методы получения полного имени сотрудника '(get_full_name)' и дохода с учётом премии
# '(get_total_income)'. Методы возвращают соответсвующие значения. Подумайте, корректно ли в классе наследнике напрямую
# обращаться к защищенному атрибуту income. Или нужен getter? Аргументируйте ответ.
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    name = 'Ivan'
    surname = 'Ivanov'
    position = 'manager'

    def __init__(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        # Подумайте, корректно ли в классе наследнике напрямую обращаться к защищенному атрибуту income.
        # Или нужен getter? Аргументируйте ответ.

        total_income = self.wage + self.bonus
        return total_income


w = Worker(3000, 777)
print(w._income)
p = Position(4000, 1000)
print(p.get_full_name())
print(p.get_total_income())
