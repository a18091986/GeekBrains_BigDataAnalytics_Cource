import numpy as np
from scipy.stats import mode
from utils import NormalDistributionRandomValue, my_print, UniformDistributionRandomValue
# -------------------------------------------------------------------------------------------
task = 'Случайная непрерывная величина A имеет равномерное распределение на промежутке (200, 800].\n' \
       'Найдите ее среднее значение и дисперсию.'
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

urv = UniformDistributionRandomValue(200, 800)

my_print(msg=f"МО СВ: {urv.m}, \nДисперсия: {urv.var}, \nСКО: {urv.std}\n", color='синий', separator_after=True)
# -------------------------------------------------------------------------------------------
task = 'О случайной непрерывной равномерно распределенной величине B известно, что ее дисперсия равна 0.2.\n' \
       'Можно ли найти правую границу величины B и ее среднее значение зная, что левая граница равна 0.5? \n' \
       'Если да, найдите ее.'
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)
my_print(msg=f"Правая граница СВ: {np.sqrt(12*0.2) + 0.5}, \nМО: {(np.sqrt(12*0.2) + 0.5 + 0.5) / 2}", color='синий',
         separator_after=True)
# -------------------------------------------------------------------------------------------
task = 'Непрерывная случайная величина X распределена нормально и задана плотностью распределения\n' \
       'f(x) = (1 / (4 * sqrt(2*pi))) * (exp(-(x+2)**2) / 32).\n' \
       'Найдите: а). M(X) б). D(X) в). std(X) (среднее квадратичное отклонение)'
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

nrv = NormalDistributionRandomValue(-2, 4)
my_print(f"M(X): {nrv.mu}\nD(X): {nrv.var}\nstx(X): {nrv.sigma}", color='синий', separator_after=False)

# -------------------------------------------------------------------------------------------
task = f'Рост взрослого населения города X имеет нормальное распределение.\nПричем, средний рост равен 174 см, ' \
       f'а среднее квадратичное отклонение равно 8 см. \nКакова вероятность того, что случайным образом выбранный ' \
       f'взрослый человек имеет рост: \nа)больше 182 см \nб)больше 190 см \nв)от 166 см до 190 см \nг)от 166 ' \
       f'см до 182 см \nд)от 158 см до 190 см \nе)не выше 150 см или не ниже 190 см \nё)не выше 150 см или не ниже ' \
       f'198 см \nж)ниже 166 см.'
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

nrv = NormalDistributionRandomValue(174, 8)
my_print(f" - больше 182: {1 - nrv.probability_calculate(182)}\n"
         f" - больше 190: {1 - nrv.probability_calculate(190)}\n"
         f" - от 166 до 190: {1 - nrv.probability_calculate(166) - (1 - nrv.probability_calculate(190))}\n"
         f" - от 166 до 182: {1 - nrv.probability_calculate(166) - (1 - nrv.probability_calculate(182))}\n"
         f" - от 158 до 190: {1 - nrv.probability_calculate(158) - (1 - nrv.probability_calculate(190))}\n"
         f" - до 150 или от 190: {nrv.probability_calculate(150) + (1 - nrv.probability_calculate(190))}\n"
         f" - до 150 или от 198: {nrv.probability_calculate(150) + (1 - nrv.probability_calculate(198))}\n"
         f" - до 166: {nrv.probability_calculate(166)}"
         , color='синий', separator_after=False)

# -------------------------------------------------------------------------------------------
task = f'На сколько сигм (средних квадратичных отклонений) отклоняется рост человека, равный 190 см, ' \
       f'от математического ожидания роста в популяции, в которой M(X) = 178 см и D(X) = 25 кв.см?'
my_print(msg=task, color='green', separator_sym='*', separator_before=True, separator_after=False)

nrv = NormalDistributionRandomValue(178, 5)
my_print(msg=f"z: {nrv.z_calculate(190)}", color='blue', separator_sym='*', separator_before=False,
         separator_after=True)