import numpy as np
from utils import my_print, my_combinations, my_arrangements, my_permutations

# -------------------------------------------------------------------------------------------
task = 'Из колоды в 52 карты извлекаются случайным образом 4 карты.\n' \
       'a) Найти вероятность того, что все карты – крести. \n' \
       'б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.'

my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)
my_print(msg=f"число возможныx сочетаний 4 карт из 13 (всех возможных крести): {my_combinations(13, 4)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число возможныx сочетаний 4 карт из 52 (всех возможных карт): {my_combinations(52, 4)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Ответ a): {my_combinations(13, 4) / my_combinations(52, 4)}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Другой вариант 13/52*12/51*11/50*10/49: {13 / 52 * 12 / 51 * 11 / 50 * 10 / 49}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=False)

b_combinations = my_combinations(4, 1) * my_combinations(48, 3) + my_combinations(4, 2) * my_combinations(48, 2) + \
                 my_combinations(4, 3) * my_combinations(48, 1) + my_combinations(4, 4) * my_combinations(48, 0)

my_print(msg=f"число возможных способов составить 4 карты среди которых есть хотя бы один туз: "
             f"{b_combinations}", color="blue", separator_before=False, separator_after=False)
my_print(msg=f"число возможныx сочетаний 4 карт из 52 (всех возможных карт): {my_combinations(52, 4)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Ответ б): {b_combinations / my_combinations(52, 4)}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=True)

# -------------------------------------------------------------------------------------------
task = f'На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9. \n' \
       f'Код cодержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек, не знающий ' \
       f'код, откроет дверь с первой попытки?'

my_print(msg=task,
         color='green', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число благоприятствующих исходов - 1",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число возможныx сочетаний 3 кнопок из 10 (всех возможных): {my_combinations(10, 3)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Ответ: {1 / my_combinations(10, 3)}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=True)

# -------------------------------------------------------------------------------------------
task = f'В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали. \n' \
       f'Какова вероятность того, что все извлеченные детали окрашены?'

my_print(msg=task,
         color='green', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число благоприятствующих исходов - число размещений 3 деталей из 9: {my_arrangements(9, 3)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число возможныx исходов - число размещений 3 деталей из 15: {my_arrangements(15, 3)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Ответ: {my_arrangements(9, 3) / my_arrangements(15, 3)}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Другой подход к решению 9/15*8/14*7/13: {9/15*8/14*7/13}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=True)

# -------------------------------------------------------------------------------------------
task = f'В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что ' \
       f'2 приобретенных билета окажутся выигрышными?'

my_print(msg=task,
         color='green', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число благоприятствующих исходов - число перестановок 2 билетов: {my_permutations(2)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"число возможныx исходов - число размещений 2 билетов из 100: {my_arrangements(100, 2)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Ответ: {my_permutations(2) / my_arrangements(100, 2)}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=False)
my_print(msg=f"Другой подход к решению 1/100*1/99: {2/100*1/99}",
         color='magenta', separator_sym='*', separator_before=False, separator_after=True)

