"""

Создать класс светофор TrafficLight
- определить у него аттрибут color и метод running
- атрибут реализовать как приватный
- в рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый
- продолжительность первого состояния (красный) - 7 секунд, второго (желтый) - 2 секунды, третьего (зеленый) - 4 секунды
- переключение между режимами должно осуществляться только в указанном порядке
- проверить работу примера, создав экземпляр и вызвав описанный метод

Задачу можно усложнить реализовав проверку порядка режимов. При его нарушении - выводить соответствующее сообщение и
завершать скрипт

"""
# import time
#
#
# class TrafficLight:
#     colors_time = [('Зеленый', 4), ('Желтый', 2), ('Красный', 7)]
#
#     def __init__(self):
#         self.__color = 'Зеленый'
#
#     def change_color(self):
#         current_color_time = list(filter(lambda x: x[0] == self.__color, self.colors_time))[0]
#         current_color_time_index = self.colors_time.index(current_color_time)
#         while True:
#             self.__color, time_value = self.colors_time[current_color_time_index % 3]
#             print(self.__color)
#             time.sleep(time_value)
#             current_color_time_index += 1
#
#
# test_traffic_light = TrafficLight()
# test_traffic_light.change_color()

"""

2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""


# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def asphalt_amount(self):
#         print(f"Для асфальтирования дороги длиной {self._length}м и шириной {self._width}м потребуется "
#               f"{int(self._width * self._length * 5 * 25) / 10000}т асфальта")
#
#
# road = Road(5000, 20)
# road.asphalt_amount()

"""

3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров

"""

# class Worker:
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = dict(wage=wage, bonus=bonus)
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return f"{self.surname} {self.name}"
#
#     def get_total_income(self):
#         return f"Доход: {self._income.get('wage') + self._income.get('bonus')}"
#
#
# employee = Position(name="Ivan", surname="Ivanov", position="Junior Developer", wage=15000, bonus=10000)
# print(f"{employee.name, employee.surname, employee.position, employee._income}")
# print(f"{employee.get_full_name()}\n{employee.get_total_income()}")

"""
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
"""


class Car:
    pass


"""
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
"""


class Stationery:
    pass

