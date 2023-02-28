import numpy as np
from utils import my_print, PuassonRandomValue, BinomialRandomValue, my_combinations, my_arrangements

# -------------------------------------------------------------------------------------------
task = 'Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. \n' \
       'Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.'
my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)
rand_val = BinomialRandomValue(100, 0.8)

my_print(msg=f"Вероятность наступления 85 событий: {rand_val.probability_m(85)}",
         color='фиолетовый', separator_after=False)
my_print(msg=f"Описательная статистика СВ: {rand_val}", color='фиолетовый', separator_after=True)

# -------------------------------------------------------------------------------------------
task = 'Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004. \n' \
       'В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность, \n' \
       'что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?'
my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)
rand_val = PuassonRandomValue(5000, 0.0004)

my_print(msg=f"Вероятность наступления 0 событий: {rand_val.probability_m(0)}",
         color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность наступления 2 событий: {rand_val.probability_m(2)}",
         color='фиолетовый', separator_after=False)
my_print(msg=f"Описательная статистика СВ: {rand_val}", color='фиолетовый', separator_after=True)

# -------------------------------------------------------------------------------------------

task = "Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?"
my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)
rand_val = BinomialRandomValue(144, 0.5)

my_print(msg=f"Вероятность наступления 70 событий: {rand_val.probability_m(70)}",
         color='фиолетовый', separator_after=False)
my_print(msg=f"Описательная статистика СВ: {rand_val}", color='фиолетовый', separator_after=True)

# -------------------------------------------------------------------------------------------

task = "В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых. \n" \
       "Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?\n" \
       "Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?"
my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)

my_print(msg=f"Вероятность вытащить два белых мяча из первого ящика: {my_arrangements(7, 2) / my_arrangements(10, 2)}",
         color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность вытащить два белых мяча из второго ящика: {my_arrangements(9, 2) / my_arrangements(11, 2)}",
         color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность вытащить белые мячи из обоих ящиков: "
             f"{my_arrangements(9, 2) / my_arrangements(11, 2) * my_arrangements(7, 2) / my_arrangements(10, 2)}",
         color='красный', separator_after=False)

rand_val_1 = BinomialRandomValue(1, 7/10)
rand_val_2 = BinomialRandomValue(1, 9/11)
rand_val_3 = BinomialRandomValue(1, 6/9)
rand_val_4 = BinomialRandomValue(1, 8/10)
p_1_2 = rand_val_1.probability_m(1)*rand_val_2.probability_m(1)*rand_val_3.probability_m(1)*rand_val_4.probability_m(1)
my_print(msg=f"Вероятность вытащить белые мячи из обоих ящиков через бернулли: {p_1_2}", color='красный',
         separator_after=False)

p_1_3 = 7/10 * 6/9 * 9/11 * 8/10

my_print(msg=f"Вероятность вытащить белые мячи из обоих ящиков третий способ: {p_1_3}", color='красный',
         separator_after=False)


p_2 = my_combinations(7, 2) / my_combinations(10, 2) * my_combinations(2, 2) / my_combinations(11, 2) + \
      my_combinations(3, 2) / my_combinations(10, 2) * my_combinations(9, 2) / my_combinations(11, 2) + \
      my_combinations(7, 1) * my_combinations(3, 1) / my_combinations(10, 2) * my_combinations(9, 1) * my_combinations(2, 1) / my_combinations(11, 2)

my_print(msg=f"Вероятность вытащить ровно 2 белых мяча из первого ящика и 0 из второго:"
             f" {my_combinations(7, 2) / my_combinations(10, 2) * my_combinations(2, 2) / my_combinations(11, 2)}",
             color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность вытащить ровно 0 белых мячей из первого ящика и ровно 2 из второго:"
             f" {my_combinations(3, 2) / my_combinations(10, 2) * my_combinations(9, 2) / my_combinations(11, 2)}",
             color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность вытащить ровно 1 белый мяч из первого ящика и ровно 1 белый мяч из второго ящика:"
             f"{my_combinations(7, 1) * my_combinations(3, 1) / my_combinations(10, 2) * my_combinations(9, 1) * my_combinations(2, 1) / my_combinations(11, 2)}",
             color='фиолетовый', separator_after=False)

p_2_2 = 7/10 * 6/9 * 2/11 * 1/10 + 3/10 * 2/9 * 9/11 * 8/10 + \
        (7/10 * 3/9 + 3/10 * 7/9) * (9/11 * 2/10 + 2/11 * 9/10)

my_print(msg=f"Вероятность вытащить ровно 2 белых мяча: {p_2}", color='красный', separator_after=False)
my_print(msg=f"Вероятность вытащить ровно 2 белых мяча второй способ: {p_2_2}", color='красный', separator_after=False)


p_3 = 1 - my_combinations(3, 2) / my_combinations(10, 2) * my_combinations(2, 2) / my_combinations(11, 2)

my_print(msg=f"Вероятность вытащить хотя бы 1 белый мяч: {p_3}", color='красный', separator_after=False)

