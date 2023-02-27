from colorama import Fore, Style


def my_print(msg: str, color='green', separator_sym="*", separator_before=False, separator_after=False) -> None:
    colors = {'yellow': Fore.YELLOW, 'green': Fore.GREEN, 'red': Fore.RED,
              'blue': Fore.BLUE, 'magenta': Fore.MAGENTA, '1': Fore.WHITE}
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

