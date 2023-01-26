"""

Реализовать класс Matrix. Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать
данные (список списков) для формирования матрицы.

Реализовать перегрузку метода str для вывода матрицы в привычном виде

Реализовать перегрузку метода add для реализации сложения двух объектов класса Matrix. Результатом сложения дб новая
матрица

"""


class Matrix:

    def __init__(self, rows: list):
        self.rows = rows

    def __str__(self):
        result_str = ''
        for row in self.rows:
            for index in range(len(row)):
                if index != len(row) - 1:
                    result_str += f'{row[index]} '
                else:
                    result_str += f'{row[index]}'
            result_str += '\n'
        return result_str

    def __add__(self, other):
        result_matrix = []
        if len(self.rows) == len(other.rows) and len(self.rows[0]) == len(other.rows[0]):
            for i in range(len(self.rows)):
                current_result_row = []
                for j in range(len(self.rows[0])):
                    current_result_row.append(self.rows[i][j] + other.rows[i][j])
                result_matrix.append(current_result_row)
        return Matrix(result_matrix)


matrix_1 = Matrix([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
matrix_2 = Matrix([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]])
matrix_3 = matrix_1 + matrix_2
print(matrix_1)
print(matrix_2)
print(matrix_3)

"""

реализовать проект расчета суммарного расхода ткани на производство одежды. основная сущность (класс) этого проекта -
одежда, которая может иметь определенное название. к типам одежды в данном проекте относятся пальто и костюм. у этих 
типов одажды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа V и H 
соответственно. 

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V / 0.65 + 0.5), для костюма: 
(2H + 0.3). Проверить работу метода на реальных данных.

Реализовать общий подсчет расхода ткани. Реализовать абстрактные классы для основных классов проекта, проверить на 
практике работу декоратора @property

"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    count_coat = 0
    count_suit = 0
    textile_all = 0

    def __init__(self, size: float, type: str):
        if type == 'coat':
            Clothes.count_coat += 1
        if type == 'suit':
            Clothes.count_suit += 1
        self.size = size


class Coat(Clothes):
    textile_all = 0

    @property
    def textile_consumption(self):
        result = self.size / 0.65 + 0.5
        Clothes.textile_all += result
        return result


class Suit(Clothes):
    textile_all = 0

    @property
    def textile_consumption(self):
        result = 2 * self.size + 0.3
        Clothes.textile_all += result
        return result


coat_1 = Coat(0.65, 'coat')
suit_1 = Suit(0.35, 'suit')
coat_2 = Coat(0.65, 'coat')
suit_2 = Suit(0.35, 'suit')

print(coat_1.textile_consumption)
print(suit_1.textile_consumption)
print(coat_2.textile_consumption)
print(suit_2.textile_consumption)

print(Clothes.count_suit)
print(Suit.count_coat)

print(Suit.textile_all)
print(Coat.textile_all)
print(Clothes.textile_all)

"""

реализовать программу работы с органическими клетками, состоящими из ячеек. необходимо создать класс клетка. 

в его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
быть реализованы методы перегрузки арифметических операторов. Данные методы должны применяться только к клеткам
и выполнять увеличение, уменьшение, умножение и целочисленное (с округление до целого) деление клеток, соответственно. 

- сложение - объединение. число ячеек общей клетки должно равняться сумме ячеек исходной клетки
- вычитание - выполнять только если разность количества ячеек клеток больше 0 иначе выводить соответствующее сообщение
- умножение - создается общая клетка из двух. число ячеек общей клетки определяется как произведение количества ячеек.
- деление  - количество ячеек итоговой клетки определяется целочисленным делением ячеек исходных клеток.

реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду, данный метод позволяет организовать
ячейки по рядам. метод должен возвращать строку вида *****\n*****\n******, где количество ячеек между \n равно переданному
аргументу.  

"""


class Cell:

    def __init__(self, part: int):
        self.part = part

    def __add__(self, other):
        return Cell(self.part + other.part)

    def __sub__(self, other):
        if self.part >= other.part:
            return Cell(self.part - other.part)
        else:
            print(f"Невозможно произвести вычитание")

    def __mul__(self, other):
        return Cell(self.part * other.part)

    def __truediv__(self, other):
        return Cell(self.part // other.part)

    def make_order(self, n):
        result = ''
        for i in range(self.part // n):
            result += f"{'*' * n}\n"
        result += f"{self.part % n * '*'}"
        return result


cell_1 = Cell(10)
cell_2 = Cell(20)

cell_1 = cell_1 + cell_2

cell_2 - cell_1
cell_1 *= cell_2
cell_1 /= cell_2
print(cell_1.make_order(15))
