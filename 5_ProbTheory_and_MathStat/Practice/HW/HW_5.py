from scipy import stats
import numpy as np
from utils import conf_interval_calculate, my_print, z_criteria_calculate, p_value_calculate, z_criteria_from_alpha, \
    t_criteria_calculate, t_criteria_from_alpha

# -------------------------------------------------------------------------------------------
task = 'Известно, что генеральная совокупность распределена нормально со средним квадратическим отклонением, ' \
       '\nравным 16. Найти доверительный интервал для оценки математического ожидания a с надежностью 0.95,' \
       '\n если выборочная средняя M = 80, а объем выборки n = 256.'

my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)
conf_interval = conf_interval_calculate(sample_mean=80, alpha=0.05, n=256, sigma=16,
                                        side='two_sided', distribution='norm')
my_print(msg=f"Доверительный интервал: {conf_interval}",
         color='синий', separator_after=False)

# -------------------------------------------------------------------------------------------
task = 'В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,\n' \
       'получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты \n' \
       'измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение величины \n' \
       'X при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95.'

my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)
sample = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
variance = sum((sample - np.mean(sample))**2) / (len(sample) - 1)
conf_interval = conf_interval_calculate(sample_mean=np.mean(sample), sigma=np.sqrt(variance), alpha=0.05, n=10,
                                        side='two_sided', distribution='t')

my_print(msg=f"Доверительный интервал: {conf_interval}", color='синий', separator_after=False)

# -------------------------------------------------------------------------------------------
task = 'Утверждается, что шарики для подшипников, изготовленные автоматическим станком, \nимеют средний диаметр 17 мм' \
       'Используя односторонний критерий с α=0,05, проверить эту гипотезу,\n' \
       'если в выборке из n=100 шариков средний диаметр оказался равным 17.5 мм, а дисперсия известна и равна 4 кв. мм.'

my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)
z_value = z_criteria_calculate(sample_mean=17.5, math_expect=17, std_dev=2, n=100)
p_value = p_value_calculate(criteria_value=z_value, distribution='norm')
my_print(msg=f"z-value: {z_value}\np-value: {p_value}\nH0, состоящая в том, что шарики для подшипников имеют диаметр "
             f"17 мм может быть отвергнута", color='синий', separator_after=False)


# -------------------------------------------------------------------------------------------
task = 'Продавец утверждает, что средний вес пачки печенья составляет 200 г. \n' \
       'Из партии извлечена выборка из 10 пачек. Вес каждой пачки составляет: \n' \
       '202, 203, 199, 197, 195, 201, 200, 204, 194, 190. Известно, что их веса распределены нормально. \n' \
       'Верно ли утверждение продавца, если учитывать, что доверительная вероятность равна 99%?'

my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

sample = [202, 203, 199, 197, 195, 201, 200, 204, 194, 190]
variance = sum((sample - np.mean(sample))**2) / (len(sample) - 1)
t_value = t_criteria_calculate(sample_mean=np.mean(sample),
                               math_expect=200, std_dev=np.sqrt(variance), n=10)
t_value_alpha = t_criteria_from_alpha(alpha=0.005, n=10)

p_value = p_value_calculate(criteria_value=t_value, distribution='t', n=10) / 2

my_print(msg=f"t-value расчетный: {t_value}\n"
             f"t-value по уровню значимости: {t_value_alpha}\n"
             f"p-value: {p_value}\nH0, состоящая в том, что средний вес пачки печень "
             f"составляет 200 г не может быть отвергнута",
         color='синий', separator_after=True)