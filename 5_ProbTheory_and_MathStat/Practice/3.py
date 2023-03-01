import numpy as np
from scipy.stats import mode
from utils import RandomSample, my_print

test_sample = np.array([1, 4, 5, 7, 10, 15, 20, 30])
print(f"Исследуемая выборка: {' '.join(map(str, test_sample.tolist()))}")
random_sample = RandomSample(test_sample)

my_print(str(f"MY_CALCULATIONS:\n"
             f"{random_sample}"
             f"Персентили 27, 57: {random_sample.percentiles_calculate([27, 57])}"), color='зеленый',
         separator_before=True,
         separator_after=False)

my_print(f"NUMPY:\n"
         f"Оценка математического ожидания: {test_sample.mean()}\n"
         f"Несмещенная оценка дисперсии: {test_sample.var(ddof=1)}\n"
         f"Смещенная оценка дисперсии: {test_sample.var()}\n"
         f"Несмещенная оценка СКО: {test_sample.std(ddof=1)}\n"
         f"Смещенная оценка СКО: {test_sample.std()}\n"
         f"Медиана: {np.median(test_sample)}\n"
         f"Мода: {mode(test_sample, keepdims=True)}\n"
         f"Размах: {np.max(test_sample) - np.min(test_sample)}\n"
         f"Квартили: {np.percentile(test_sample, [25, 50, 75], method='midpoint')}\n"
         f"Персентили 27, 57: {np.percentile(test_sample, [27, 57], method='midpoint')}",
         color='желтый', separator_after=True)
