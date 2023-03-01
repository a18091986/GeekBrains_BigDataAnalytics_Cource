from utils import NormalDistributionRandomValue, my_print, UniformDistributionRandomValue
# -----------------------------------------------------------------------------------------
ndv = NormalDistributionRandomValue(0, 1)

# for x in range(-10, 11, 1):
#     print(f"{x}:{ndv.distribution_density(x)}")

# -----------------------------------------------------------------------------------------

ndv_1 = NormalDistributionRandomValue(5, 0.6)
task = f'Диаметр гаек следует нормальному распределению с МО = 5 мм и D = 0.36мм^2.\n' \
       f'Найти пропорцию гаек с размером менее 3.78 мм'

my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)

my_print(msg=f"Значение z-статистики для гаек с размером 3.78: {ndv_1.z_calculate(3.78)}\n"
             f"Искомая пропорция (вероятность): {ndv_1.probability_calculate(3.78)}", color='синий',
         separator_after=True)

# -----------------------------------------------------------------------------------------

udv_1 = UniformDistributionRandomValue(0, 30)
task = f'Посадка на самолет задерживается на величину до 30 минут. Найти вероятность того, что посадка начнётся в ' \
       f'промежутке от 20 до 30 минут'

my_print(msg=task,
         color='green', separator_sym='*', separator_before=True, separator_after=False)

my_print(msg=f"МО СВ: {udv_1.m}, \nДисперсия: {udv_1.var}, \nСКО: {udv_1.std}\n"
             f"Искомая вероятность: {udv_1.probability_calculate(20)}", color='синий',
         separator_after=True)

