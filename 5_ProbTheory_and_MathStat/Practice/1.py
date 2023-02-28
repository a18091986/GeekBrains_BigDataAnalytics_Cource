import numpy as np
from utils import my_print, my_combinations, my_arrangements
 
# -------------------------------------------------------------------------------------------
test_array = np.random.randint(0, 10, 1000000)

my_print(msg=f"Массив: {test_array}",
         color='green', separator_sym='*', separator_before=True, separator_after=False)
my_print(msg=f"Относительная частота события 'генерация числа 3': {len(test_array[test_array==3]) / len(test_array)}",
         color='blue', separator_sym='*', separator_before=False, separator_after=True)

# -------------------------------------------------------------------------------------------
my_print(msg='Подбрасываются две игральные кости, подсчитать частоту события, при котором на первой игральной кости '
             'выпала 1, а на второй 6', separator_before=False, separator_after=False)

cube_1 = np.random.randint(1, 7, 10000)
cube_2 = np.random.randint(1, 7, 10000)
event = cube_1[(cube_1 == 1) & (cube_2 == 6)]
my_print(msg=f'Частота интересующего события: {len(event) / len(cube_1)}', color='blue',
         separator_after=True, separator_before=False)

# -------------------------------------------------------------------------------------------
my_print(msg='сколькими способами можно выбрать 4 карты из колоды в 36 карт',
         separator_before=False, separator_after=False)

my_print(msg=f'{my_combinations(36, 4)}', color='blue', separator_before=False, separator_after=True)

# -------------------------------------------------------------------------------------------
my_print(msg='сколькими способами можно выстроить очередь из 5 человек при общем количестве людей - 20',
         separator_before=False, separator_after=False)

my_print(msg=f'{my_arrangements(20, 5)}', color='blue', separator_before=False, separator_after=True)

# ------------------------------------------------------------------------------------------
my_print(msg='сколькими способами  5 человек могут организовать очередь',
         separator_before=False, separator_after=False)

my_print(msg=f'{my_arrangements(5, 5)}', color='blue', separator_before=False, separator_after=True)

# ------------------------------------------------------------------------------------------
my_print(msg='из колоды состоящей из 36 карт случайным образом выбрано 5. Сколькими способами можно выбрать эти карты '
             'так, чтобы среди них оказалось от 2 до 3 тузов',
         separator_before=False, separator_after=False)

my_print(msg=str(my_combinations(4, 2) * my_combinations(32, 3) + my_combinations(4, 3) * my_combinations(32, 2)),
         separator_before=False, color='blue', separator_after=True)

# ------------------------------------------------------------------------------------------
my_print(msg='Какова вероятность выбрать из колоды в 36 карт 5 карт так, чтобы среди них было 2 туза',
         separator_before=False, separator_after=False)

my_print(msg=f"{round(my_combinations(4, 2) * my_combinations(32, 3) / my_combinations(36, 5) * 100, 2)}%",
         separator_before=False, color='blue', separator_after=True)
