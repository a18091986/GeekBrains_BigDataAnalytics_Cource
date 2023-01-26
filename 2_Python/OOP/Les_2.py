"""

# перегрузка операторов - переопределение стандартных операторов, определяемых для всех классов

__init__() - конструктор
__del__() - деструктор
__str__() - преобразование к строке (срабатывает при передаче объекта функциям str и print
__add__() - оператор сложения, срабатывае при цчастии объекта в операции сложения с левой стороны
__setattr__() - срабатывает при выполнении операции присваивания значения аттрибуту
__getitem__() - срабатывает при извлечении элемента по индексу
__call__() - срабатывает при обращении к экземпляру класса как к функции

# переопределение методов

механизм, позволяющий использовать метод класса-родителя в классе-потомке с добавлением некоторой функциональности

# интерфейсы

описание поведения объекта, т.е. совокупность публичных методов объекта, которые могут применяться в других частях
программы для взаимодействия с ним

интерфейс не может иметь объектов (своего класса) - он служит для того, что определить как будут рабоать потомки
этого класса

методы в интерфейсе не реализованы - они лишь определены и показывают какие параметры принимают. тела метода нет.
таким образом мы создаем стандарт для дочерних классов

# интерфейс итерации

под итераторами понимаются специальные объекты, обеспечивающие пошаговый доступ к данным из контейнера. В привязке
к итераторам работают циклы перебора (for in), встроенные функции (map(), filter(), zip()), операция распаковки
итератор - объект, реализующий метод __next__() без аргументов, возвращающий очередной элемент или исключение
StopIteration.

# собственные объекты-итераторы



# декоратор

функция, которая навешивается на другую функцию и "обертывает" её. это делается для дополнения функционала обертываемой
функции

# декоратор @property

позволяет работать с методом некоторого класса как с атрибутом

# композиция

в концепции ООП существует возможность реализации композиционного подхода, в соответствии с которым создается
класс-контейнер, включающий вызов других классов (в него попадают объекты этих классов)
и при этом никак не будет наследовать другие классы

"""

# -----------------------------------ПЕРЕГРУЗКА МЕТОДОВ-------------------------------------

class Package:

    def __init__(self, content, weight):
        self.content = content
        self.weight = weight

    def __str__(self):
        return f'{self.content} {self.weight}'

    def __repr__(self):
        return f'{self.content} {self.weight}'

    # def __sub__ = "-"
    # def __mul__ = "*"
    # def __truediv__ = "/"
    def __add__(self, new_package):
        return Package(f'{self.content} and {new_package.content}', self.weight+new_package.weight)

    # def __lt__ "<"
    # def __le__ "<="
    # def __gt__ ">"
    # def __ge__ ">="
    def __eq__(self, other):
        return (self.content == other.content) & (self.weight == other.weight)


my_obj_1 = Package('Books', 20)
my_obj_11 = Package('Books', 20)
my_obj_2 = Package('Cups', 30)
print(my_obj_1)
my_list = [my_obj_1, ]
print(my_list)
print(my_obj_1 + my_obj_2)
print(my_obj_1 == my_obj_2)
print(my_obj_11 == my_obj_1)

# ----------------------------------ИНТЕРФЕЙС----------------------------------------

# from abc import ABC, abstractmethod
#
# class Animal(ABC): # наследуемся от класса ABC для задания методов, которые должны быть реализованы в дочерних классах (для создания интерфейса)
#
#     @abstractmethod #для создания интерфейса - показываем, что этот метод должен быть реализован в дочернем классе
#     def make_sound(self):
#         pass
#
#     @abstractmethod #для создания интерфейса - показываем, что этот метод должен быть реализован в дочернем классе
#     def eat(self, meal):
#         pass
#
#
# class Giraffe(Animal):
#     def make_sound(self):
#         print("Я жираф")
#
#     def eat(self, meal):
#         print("Жираф кушает")
#
# my_giraffe = Giraffe()
# my_giraffe.make_sound()
# my_giraffe.eat('еда')


# -----------------------------------------------ИТЕРАТОР-------------------------------------------

class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1

    def __next__(self):
        self.current += 1
        if self.current < self.end:
            return self.current

        else:
            raise StopIteration


class MyObject:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyIterator(self.start, self.end)


my_object = MyObject(0, 10)
for el in my_object: # my_object = my_object.__iter__() = MyIterator(0, 10); el = MyIterator(0, 10).__next__()
    print(el) #


# -----------------------------------------------декоратор @property-------------------------------------------

class Book:

    count = 0

    def __init__(self, title, author, year=2000, count_pages=None):
        self.title = title
        self._author = author
        self._year = year

        if count_pages and type(count_pages) == int:
            self.count_pages = count_pages

        Book.count += 1

    @property
    def _get_full_name(self):
        return f'{self.title} - {self._author}[{self._year}] (books count: {Book.count})'


my_book = Book('test_book', 'test_author')
print(my_book._get_full_name)


# -----------------------------------------------композиция-------------------------------------------

class Reader:

    def __init__(self):
        self.books = []

    def take_book(self, book):
        self.books.append(book)


class Library:

    def get_book_to_reader(self, reader, book):
        reader.take_book(book)


reader = Reader()
library = Library()
library.get_book_to_reader(reader, my_book)

print(reader.books[0].title)