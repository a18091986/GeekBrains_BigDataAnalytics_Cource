import math
import numpy as np
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
        return n * my_factorial(n - 1)


def my_combinations(n: int, k: int) -> int:
    """Подсчет числа сочетаний из n элементов по k"""
    return int(my_factorial(n) / (my_factorial(k) * my_factorial(n - k)))


def my_arrangements(n: int, k: int) -> int:
    """Подсчет числа размещений из n элементов по k"""
    return int(my_factorial(n) / (my_factorial(n - k)))


def my_permutations(n: int) -> int:
    """Подсчет числа перестановок из n элементов"""
    return my_arrangements(n, n)


def full_probability(prob_list: list, cond_prob_list: list) -> float:
    return (np.array(prob_list)*np.array(cond_prob_list)).sum()

def conditional_probability(prob_1: float, prob_2: float, cond_prob_1_2: float) -> float:
    """"Рассчитывает условную вероятность события 2 при условии события 1
    prob_2 - вероятность события 2
    prob_1 - вероятность события 1
    cond_prob_1_2 - вероятность события 1 при условии 2
    """
    return prob_2 * cond_prob_1_2 / prob_1

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


class RandomSample:
    def __init__(self, sample: np.array):
        self.sample = sample
        self.math_expect = self.math_expect_calculate()
        self.variance_not_biased = self.variance_calculate(ddof=1)
        self.variance_biased = self.variance_calculate(ddof=0)
        self.std_not_biased = self.std_calculate(ddof=1)
        self.std_biased = self.std_calculate(ddof=0)
        self.median = self.median_calculate()
        self.moda = self.moda_calculate()
        self.spread = self.sample.max() - self.sample.min()
        self.quartiles = self.quartiles_calculate()

    def __repr__(self):
        return f"Оценка математического ожидания: {self.math_expect}\n" \
               f"Несмещенная оценка дисперсии: {self.variance_not_biased}\n" \
               f"Смещенная оценка дисперсии: {self.variance_biased}\n" \
               f"Несмещенная оценка СКО: {self.std_not_biased}\n" \
               f"Смещенная оценка СКО: {self.std_biased}\n" \
               f"Медиана: {self.median}\n" \
               f"Мода: {self.moda}\n" \
               f"Размах: {self.spread}\n" \
               f"Квартили: {self.quartiles}\n"

    def __str__(self):
        return f"Оценка математического ожидания: {self.math_expect}\n" \
               f"Несмещенная оценка дисперсии: {self.variance_not_biased}\n" \
               f"Смещенная оценка дисперсии: {self.variance_biased}\n" \
               f"Несмещенная оценка СКО: {self.std_not_biased}\n" \
               f"Смещенная оценка СКО: {self.std_biased}\n" \
               f"Медиана: {self.median}\n" \
               f"Мода: {self.moda}\n" \
               f"Размах: {self.spread}\n" \
               f"Квартили: {self.quartiles}\n"

    def math_expect_calculate(self):
        return sum(self.sample) / len(self.sample)

    def std_calculate(self, ddof=0):
        if ddof:
            result = np.sqrt(self.variance_not_biased)
        else:
            result = np.sqrt(self.variance_biased)
        return result

    def variance_calculate(self, ddof=0):
        if ddof:
            result = sum(pow(self.sample - self.math_expect, 2)) / (len(self.sample) - 1)
        else:
            result = sum(pow(self.sample - self.math_expect, 2)) / len(self.sample)
        return result

    def median_calculate(self):
        if len(self.sample) % 2:
            result = sorted(self.sample)[len(self.sample) // 2]
        else:
            result = (sorted(self.sample)[len(self.sample) // 2 - 1] + sorted(self.sample)[len(self.sample) // 2]) / 2
        return result

    def moda_calculate(self):
        return np.argmax(np.bincount(self.sample))

    def percentiles_calculate(self, percentiles: list):
        result = []
        sample = sorted(self.sample.copy())
        for percentile in [x / 100 for x in percentiles]:
            temp = percentile * len(sample)
            if int(temp) == temp:
                temp = int(temp)
                result.append((sample[temp-1] + sample[temp]) / 2)
            else:
                print(temp)
                result.append((sample[int(temp) - 1] + sample[int(temp)]) / 2)
        return result

    def quartiles_calculate(self):
        return self.percentiles_calculate([25, 50, 75])
