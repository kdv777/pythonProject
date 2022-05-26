class Auto:
    # auto_name = "Lexus"
    # auto_model = "RX 350L"
    # auto_year = 2019
    auto_count = 0

    def __init__(self):
        Auto.auto_count +=1
        print(Auto.auto_count)


    def get_class_info(self):
        print("Детальная инфа")

# a = Auto()
# a.get_class_info()

class Transport:
    def transport_method(self):
        print("Это родительский метод из класса Transport")


class Auto(Transport):
    def auto_method(self):
        print("Это метод дочернего класса")

a = Auto()
a.transport_method()

#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("Автомобиль заведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count +=1
#
#
#     def on_auto_stop(self):
#         print("Останавливаем работу двигателя")
#
#
# a = Auto()
# a.on_auto_start("Lexus", "RX 350L", "2019")
# print(a.auto_name)
# print(a.auto_count)
#
# a_2 = Auto()
# a_2.on_auto_start("Mazda", "CX 9", 2018)
# print(a_2.auto_name)
# print(a_2.auto_count)