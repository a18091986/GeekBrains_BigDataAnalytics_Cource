import numpy as np
from scipy.stats import mode
from utils import my_print, PuassonRandomValue, BinomialRandomValue, my_combinations, my_arrangements, RandomSample, \
    full_probability, conditional_probability

# -------------------------------------------------------------------------------------------
task = 'Даны значения зарплат из выборки выпускников: \n' \
       '100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150. \n' \
       'Посчитать (желательно без использования статистических методов наподобие std, var, mean) \n' \
       'среднее арифметическое, среднее квадратичное отклонение, \n' \
       'смещенную и несмещенную оценки дисперсий для данной выборки.'
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)
sample = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])
arr_graduate = RandomSample(sample)

my_print(str(f"MY_CALCULATIONS:\n"
             f"{arr_graduate}"
             f"Персентили 27, 57: {arr_graduate.percentiles_calculate([27, 57])}"), color='зеленый',
         separator_before=True,
         separator_after=False)

my_print(f"NUMPY:\n"
         f"Оценка математического ожидания: {sample.mean()}\n"
         f"Несмещенная оценка дисперсии: {sample.var(ddof=1)}\n"
         f"Смещенная оценка дисперсии: {sample.var()}\n"
         f"Несмещенная оценка СКО: {sample.std(ddof=1)}\n"
         f"Смещенная оценка СКО: {sample.std()}\n"
         f"Медиана: {np.median(sample)}\n"
         f"Мода: {mode(sample, keepdims=True)}\n"
         f"Размах: {np.max(sample) - np.min(sample)}\n"
         f"Квартили: {np.percentile(sample, [25, 50, 75], method='midpoint')}\n"
         f"Персентили 27, 57: {np.percentile(sample, [27, 57], method='midpoint')}",
         color='желтый', separator_after=True)
# -------------------------------------------------------------------------------------------
task = 'В первом ящике находится 8 мячей, из которых 5 - белые. Во втором ящике - 12 мячей, из которых 5 белых. \n' \
       'Из первого ящика вытаскивают случайным образом два мяча, из второго - 4. \n' \
       'Какова вероятность того, что 3 мяча белые?'
my_print(msg=task, color='green', separator_sym='*', separator_before=False, separator_after=False)

p_1 = my_combinations(5, 2) * my_combinations(3, 0) / my_combinations(8, 2) * \
      my_combinations(5, 1) * my_combinations(7, 3) / my_combinations(12, 4)
p_2 = my_combinations(5, 1) * my_combinations(3, 1) / my_combinations(8, 2) * \
      my_combinations(5, 2) * my_combinations(7, 2) / my_combinations(12, 4)
p_3 = my_combinations(5, 0) * my_combinations(3, 2) / my_combinations(8, 2) * \
      my_combinations(5, 3) * my_combinations(7, 1) / my_combinations(12, 4)

my_print(msg=f"Answer: {p_1 + p_2 + p_3}", color='синий', separator_sym='*', separator_before=False,
         separator_after=False)
# -------------------------------------------------------------------------------------------
task = "На соревновании по биатлону один из трех спортсменов стреляет и попадает в мишень. \n" \
       "Вероятность попадания для первого спортсмена равна 0.9, для второго — 0.8, для третьего — 0.6. \n" \
       "Найти вероятность того, что выстрел произведен: \n" \
       "a). первым спортсменом б). вторым спортсменом в). третьим спортсменом."
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

fp = full_probability(prob_list=[1/3, 1/3, 1/3], cond_prob_list=[.9, .8, .6])
my_print(msg=f"Полная вероятность наступления события 'попадание в мишень': {fp}", color='синий',
         separator_after=False, separator_before=False)
my_print(f"Вероятность выстрела первым спортсменом: "
         f"{conditional_probability(prob_1=fp, prob_2=1/3, cond_prob_1_2=0.9)}", color='синий',
         separator_before=False, separator_after=False)
my_print(f"Вероятность выстрела вторым спортсменом: "
         f"{conditional_probability(prob_1=fp, prob_2=1/3, cond_prob_1_2=0.8)}", color='синий',
         separator_before=False, separator_after=False)
my_print(f"Вероятность выстрела третьим спортсменом: "
         f"{conditional_probability(prob_1=fp, prob_2=1/3, cond_prob_1_2=0.6)}", color='синий',
         separator_before=False, separator_after=False)
# -------------------------------------------------------------------------------------------

task = "В университет на факультеты A и B поступило равное количество студентов, \n" \
       "а на факультет C студентов поступило столько же, сколько на A и B вместе. \n" \
       "Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8. \n" \
       "Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. \n" \
       "Студент сдал первую сессию. Какова вероятность, что он учится: \n" \
       "a). на факультете A б). на факультете B в). на факультете C?"
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

fp = full_probability([1/4, 1/4, 1/2], [0.8, 0.7, 0.9])
my_print(msg=f"Полная вероятность наступления события 'сдал сессию': {fp}", color='синий',
         separator_after=False, separator_before=False)
my_print(f"Вероятность что студент учится на факультете А: "
         f"{conditional_probability(prob_1=fp, prob_2=1/4, cond_prob_1_2=0.8)}", color='синий',
         separator_before=False, separator_after=False)
my_print(f"Вероятность что студент учится на факультете Б: "
         f"{conditional_probability(prob_1=fp, prob_2=1/4, cond_prob_1_2=0.7)}", color='синий',
         separator_before=False, separator_after=False)
my_print(f"Вероятность что студент учится на факультете С: "
         f"{conditional_probability(prob_1=fp, prob_2=1/2, cond_prob_1_2=0.9)}", color='синий',
         separator_before=False, separator_after=False)
# -------------------------------------------------------------------------------------------

task = "Устройство состоит из трех деталей. Для первой детали вероятность выйти из строя в первый месяц равна 0.1\n " \
       "для второй - 0.2, для третьей - 0.25. Какова вероятность того, что в первый месяц выйдут из строя:\n" \
       "а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?"
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

my_print(f"Вероятность поломки всех деталей: "
         f"{0.2 * 0.25 * 0.1}", color='синий',
         separator_before=False, separator_after=False)

my_print(f"Вероятность поломки двух деталей: "
         f"{0.9 * 0.2 * 0.25 + 0.75 * 0.1 * 0.2 + 0.8 * 0.25 * 0.1}", color='синий',
         separator_before=False, separator_after=False)

my_print(f"Вероятность поломки хотя бы одной детали: "
         f"{1 - 0.9 * 0.8 * 0.75}", color='синий',
         separator_before=False, separator_after=False)

my_print(f"Вероятность поломки от одной до двух деталей: "
         f"{1 - 0.9 * 0.8 * 0.75 - 0.2 * 0.25 * 0.1}", color='синий',
         separator_before=False, separator_after=False)