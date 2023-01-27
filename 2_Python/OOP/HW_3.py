"""

1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

"""
# class Data:
#     def __init__(self, data_string):
#         self.data_string = data_string
#
#     @classmethod
#     def convert_data_to_day_month_year(cls, data_string):
#         return tuple(map(int, data_string.split('-')))
#
#     @staticmethod
#     def validate_date(data_string):
#         day, month, year = Data.convert_data_to_day_month_year(data_string)
#         if day <= 31 and day >= 1 and month <= 12 and month >= 1 and year > 0:
#             print("Date correct")
#         else:
#             print("Wrong date")
#
# date_1 = "100-13-2013"
# Data.validate_date(date_1)

"""

2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 

Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

"""

# class MyZeroDevisionException(Exception):
#     def __init__(self, text):
#         self.text = text
#
# divider = int(input("input number:\n"))
# if divider == 0:
#     print(MyZeroDevisionException("Нельзя делить на ноль"))
# else:
#     print(1/divider)



"""

3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.

"""

# class DigitValidationException(Exception):
#     def __init__(self, text):
#         self.text = text
#
# result = []
# while True:
#     current_input = input("Введите число или q для завершения\n")
#     if current_input == 'q':
#         break
#     if not current_input.isdigit():
#         print(DigitValidationException("Это не число\n"))
#     else:
#         result.append(current_input)
#
# print(result)


"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад 
и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру (например, словарь).

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, 
изученных на уроках по ООП.
"""

# class ValidateModelFormat(Exception):
#     def __init__(self, text):
#         self.text = text
#
# class Warehouse:
#     technic = dict()
#
#     @classmethod
#     def take_technic(cls, in_technic):
#         for el, count in in_technic.items():
#             if Warehouse.validate_model(el.model):
#                 if el.model in Warehouse.technic:
#                     Warehouse.technic[el.model] += count
#                 else:
#                     Warehouse.technic[el.model] = count
#
#     @classmethod
#     def give_technic(cls, out_technic):
#         for el, count in out_technic.items():
#             if Warehouse.validate_model(el.model):
#                 if el.model in Warehouse.technic:
#                     if Warehouse.technic[el.model] >= count:
#                         Warehouse.technic[el.model] -= count
#                     else:
#                         print(f"На складе недостаточно техники, выдал то, что есть {el.model}: {Warehouse.technic[el.model]}")
#                         Warehouse.technic[el.model] = 0
#                 else:
#                     print(f"На складе отсутствует такая позиция {el.model}")
#
#     @staticmethod
#     def validate_model(model):
#         if not all(tuple(map(lambda x: x.isdigit(), model.split('-')))):
#             return True
#         else:
#             ValidateModelFormat("Неправльный формат модели")
#             return False
#
#     def __str__(self):
#         return f"Warehouse technic: {Warehouse.technic}"
#
#     def __repr__(self):
#         return f"Warehouse technic: {Warehouse.technic}"
#
#
# class OfficeTechnic:
#     number = 0
#     def __init__(self, cost: float, model='nn-aa'):
#         self.cost = cost
#         self.model = model
#         self.id = OfficeTechnic.number
#         OfficeTechnic.number += 1
#
#     def __str__(self):
#         return f"Стоимость: {self.cost}, model: {self.model}"
#
#     def __repr__(self):
#         return f"Стоимость: {self.cost}, model: {self.model}"
#
# class Printer(OfficeTechnic):
#     def __init__(self, cost: float, black_and_white: bool, model="nn-aa"):
#         super().__init__(cost, model)
#         self.black_and_white = black_and_white
#
#     def __str__(self):
#         return f"Принтер. Ч/б: {self.black_and_white}, {super().__str__()}"
#
# class Scaner(OfficeTechnic):
#     def __init__(self, cost: float, paper_format: str, model="nn-aa"):
#         super().__init__(cost, model)
#         self.paper_format = paper_format
#
#     def __str__(self):
#         return f"Сканер. Формат сканирования: {self.paper_format}, {super().__str__()}"
#
# scaner_1 = Scaner(100, 'A4')
# scaner_2 = Scaner(200, 'A4')
# scaner_3 = Scaner(300, 'A4')
# scaners = {scaner_1: 3, scaner_2: 2, scaner_3: 3}
# print(scaner_1)
# printer_1 = Printer(200, True)
# print(printer_1)
# warehouse = Warehouse()
# warehouse.take_technic(scaners)
# print(warehouse)
# warehouse.take_technic({Scaner(500, 'A4', "ff-aa"): 2})
# print(warehouse)
# warehouse.give_technic({Scaner(500, 'A4', "ff-aa"): 3})
# print(warehouse)
# warehouse.take_technic({Scaner(500, 'A4', "ff-aa"): 2})
# warehouse.take_technic({Scaner(500, 'A4', "ff-aa"): 2})
# print(warehouse)
# warehouse.give_technic({Scaner(500, 'A4', "ff-aa"): 3})
# print(warehouse)


"""

7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), 
выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""

class Complex:
    def __init__(self, real, illusion):
        self.real = real
        self.illusion = illusion

    def __add__(self, other):
        return Complex(self.real + other.real, self.illusion + other.illusion)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.illusion - other.illusion)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.illusion * other.illusion,
                       self.real * other.illusion + self.illusion * other.real)

    def __truediv__(self, other):
        znam = pow(other.real, 2) + pow(other.illusion, 2)
        tchisl_1 = self.real * other.real + self.illusion * other.illusion
        tchisl_2 = self.illusion * other.real - self.real * other.illusion
        return Complex(tchisl_1 / znam, tchisl_2 / znam)

    def __str__(self):
        if self.illusion == 0:
            return f"{self.real}"
        elif self.illusion < 0:
            return f"{self.real} {self.illusion}i"
        else:
            return f"{self.real} + {self.illusion}i"


num_1 = Complex(1, 1)
num_2 = Complex(2, 3)
num_3 = num_1 + num_2
print(num_3)
num_3 = num_1
print(num_3)
num_3 = num_1 * num_2
print(num_3)
num_3 = num_1 / num_2
print(num_3)