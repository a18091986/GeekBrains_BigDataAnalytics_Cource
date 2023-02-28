import math

from colorama import Fore, Style


def my_print(msg: str, color='green', separator_sym="*", separator_before=False, separator_after=False) -> None:
    colors = {'yellow': Fore.YELLOW, 'желтый': Fore.YELLOW,
              'green': Fore.GREEN, 'зеленый': Fore.GREEN,
              'red': Fore.RED, 'красный': Fore.RED,
              'blue': Fore.BLUE, 'синий': Fore.BLUE,
              'magenta': Fore.MAGENTA, 'фиолетовый': Fore.MAGENTA,
              '1': Fore.WHITE
              }
    if separator_before:
        print(f"{Fore.RED}{separator_sym * 300}{Style.RESET_ALL}")
    if color in colors:
        print(f"{colors[color]}{msg}{Style.RESET_ALL}")
    else:
        print(f"{msg}")
    if separator_after:
        print(f"{Fore.RED}{separator_sym * 300}{Style.RESET_ALL}")

# ------------------------------------------------math--------------------------------------------------


def my_factorial(n: int) -> int:
    """Подсчет факториала числа n"""
    if n == 0:
        return 1
    else:
        return n * my_factorial(n-1)


def my_combinations(n: int, k: int) -> int:
    """Подсчет числа сочетаний из n элементов по k"""
    return int(my_factorial(n) / (my_factorial(k) * my_factorial(n - k)))


def my_arrangements(n: int, k: int) -> int:
    """Подсчет числа размещений из n элементов по k"""
    return int(my_factorial(n) / (my_factorial(n - k)))


def my_permutations(n: int) -> int:
    """Подсчет числа перестановок из n элементов"""
    return my_arrangements(n, n)


def probability_in_binomial_distribution(k: int, n: int, p: float) -> float:
    """"Возвращает вероятность возникновения случайного события к раз в серии из n экспериментов. p - вероятность
    наступления события A в независимых испытаниях"""
    q = 1 - p
    return my_combinations(n, k) * pow(p, k) * pow(q, n - k)

def probability_in_puasson_distribution(lamb: float, m: int) -> float:
    """Возвращает вероятность возникновения случайного события m раз за фиксированную единицу измерения
    количества/времени"""
    return (pow(lamb, m) / my_factorial(m)) * math.exp(-lamb)


# ------------------------------------------------classes--------------------------------------------------


class BinomialRandomValue:
    """определяет класс дискретных случайных величин, распределенных по Биномиальному закону
    n - количество испытаний
    p - вероятность наступления события в одном испытании
    """
    def __init__(self, n: int, p: float):
        self.n = n
        self.p = p
        self.q = 1 - p
        self.math_expectation = self.n * self.p
        self.variance = self.n * self.p * self.q
        self.sd = math.sqrt(self.variance)

    def probability_m(self, m):
        if self.n >= m >= 0:
            return my_combinations(self.n, m) * pow(self.p, m) * pow(self.q, self.n - m)
        elif m < 0:
            return "Число событий не может быть меньше нуля"
        else:
            return "Количество событий не может быть больше числа испытаний"

    def __repr__(self):
        return f"М(Х): {self.math_expectation}, D(X): {self.variance}, StandDev: {self.sd}"


class PuassonRandomValue:
    """определяет класс дискретных случайных величин, распределенных по закону Пуассона
    lamb - средняя интенсивность наступления событий в единицу измерения
    """
    def __init__(self, n=None, p=None, lamb=None):
        if n and p:
            self.lamb = n * p
        else:
            self.lamb = lamb
        self.math_expectation = self.lamb
        self.variance = self.lamb
        self.sd = math.sqrt(self.variance)

    def probability_m(self, m):
        if m >= 0:
            return (pow(self.lamb, m) / my_factorial(m)) * math.exp(-self.lamb)
        else:
            return "Число событий не может быть меньше нуля"

    def __repr__(self):
        return f"М(Х): {self.math_expectation}, D(X): {self.variance}, StandDev: {self.sd}"