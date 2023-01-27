"""

- статические методы класса

@staticmethod - декоратор для статического метода. такой метод вызывается напрямую через имя класса
@classmethod - декоратор для метода класса. такой метод получает класс в качестве первого аргумента
методы для запуска которых не нужны экземпляры класса

- атрибуты и встроенные методы объектов класса

__name__ - имя класса
__module__ - имя модуля
__dict__ - словарь с атрибутами класса
__base__ - кортеж с базовыми классами
__doc__ - строка документации класса
__class__ - объект-класс, экземпляром которого является данный интстанс
__init__ - конструктор
__dell__ - деструктор
__hash__ - возвращает хеш-значение объекта, равное 32-битному числу

- примеры ООП программ

- создание собственных исключений

- библиотека psutil

- pip & virtualenv

pip list, pip show....

pip install virtualenv
virtualenv my_proj
my_proj\Scripts\activate
my_proj\Scripts\deactivate

- requests

"""


# class Book:
#     __count = 0
#
#     def __init__(self, title, author, year=2000, count_pages=None):
#         self.title = title
#         self._author = author
#         self._year = year
#         if count_pages and type(count_pages) == int:
#             self.count_pages = count_pages
#         Book.__count += 1
#
#     @property
#     def full_name(self):
#         return f'{self.title} - {self._author} [{self._year}] (count of all books: {Book.__count})'
#
#     @staticmethod
#     def get_sum_pages(p_1, p_2):
#         return p_1 + p_2
#
#     @classmethod
#     def get_books_count(cls):
#         return cls.__count
#
#
# book = Book('testbook', 'Testauthor')
#
# print(Book.get_sum_pages(1, 2))
# print(Book.get_books_count())
#
# print(book.__dict__)


# class Book:
#     cur_id = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.id = Book.cur_id
#         Book.cur_id += 1
#
#     def __str__(self):
#         return f'{self.title} - {self.author}'
#
#     def __repr__(self):
#         return f'{self.title} - {self.author}'
#
#
# class Reader:
#     cur_id = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.id = Reader.cur_id
#         Reader.cur_id += 1
#
#     def take_book(self, book):
#         if len(self.books) >= 3:
#             return False
#         self.books.append(book)
#         return True
#
#     def return_book(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             return True
#         return False
#
#     def __str__(self):
#         return f'{self.name} - {self.books}'
#
#     def __repr__(self):
#         return f'{self.name} - {self.books}'
#
# class Terminal:
#
#     def __init__(self):
#         self.books = {}
#
#     def take_book(self, books):
#         for key, value in books.items():
#             if key in self.books:
#                 self.books[key] += 1
#             else:
#                 self.books[key] = value
#
#     def give_book_to_reader(self, reader, book):
#         if book.id in self.books and self.books[book.id] > 0:
#             if reader.take_book(book):
#                 self.books[book.id] -= 1
#                 return True
#             else:
#                 print("Reader already have three books")
#         else:
#             print("Terminal don't have this book")
#         return False
#
#     def take_book_from_reader(self, reader, book):
#         if reader.return_book(book):
#             book_dict = {book.id: 1}
#             self.take_book(book_dict)
#             return True
#         else:
#             print("Reader don't have this book")
#             return False
#
#
# book_1 = Book('Test_book_1', 'test_author_1')
# book_2 = Book('Test_book_2', 'test_author_2')
# book_3 = Book('Test_book_3', 'test_author_3')
# book_4 = Book('Test_book_4', 'test_author_4')
# book_5 = Book('Test_book_5', 'test_author_5')
#
# books = {
#     book_1.id: 1, book_2.id: 3, book_3.id: 1, book_4.id: 2, book_5.id: 1
# }
#
# reader = Reader('Reader_1')
# terminal = Terminal()
# terminal.take_book(books)
#
# print(terminal.books)
# print(reader)
#
# terminal.give_book_to_reader(reader=reader, book=book_2)
# print(terminal.books)
# print(reader)
#
# terminal.give_book_to_reader(reader=reader, book=book_1)
# print(terminal.books)
# print(reader)
#
# terminal.give_book_to_reader(reader=reader, book=book_1)
# print(terminal.books)
# print(reader)
#
# terminal.give_book_to_reader(reader=reader, book=book_4)
# print(terminal.books)
# print(reader)
#
# terminal.give_book_to_reader(reader=reader, book=book_5)
# print(terminal.books)
# print(reader)
#
# terminal.take_book_from_reader(reader=reader, book=book_1)
# print(terminal.books)
# print(reader)
#
# terminal.take_book_from_reader(reader=reader, book=book_1)
# print(terminal.books)
# print(reader)

class MyException(Exception):

    def __init__(self, text):
        self.text = text

number = input("Write number")
if not number.isdigit():
    raise MyException('Not number')