import numpy as np
from scipy.stats import mode
from utils import RandomSample, my_print

test_sample = np.array([1, 4, 5, 7, 7, 10, 10, 20])
print(f"Исследуемая выборка: {' '.join(map(str, test_sample.tolist()))}")
random_sample = RandomSample(test_sample)

my_print(str(f"MY_CALCULATIONS:\n{random_sample}"), color='зеленый', separator_before=True, separator_after=False)

my_print(f"NUMPY:\n"
         f"Оценка математического ожидания: {test_sample.mean()}\n"
         f"Несмещенная оценка дисперсии: {test_sample.var(ddof=1)}\n"
         f"Смещенная оценка дисперсии: {test_sample.var()}\n"
         f"Несмещенная оценка СКО: {test_sample.std(ddof=1)}\n"
         f"Смещенная оценка СКО: {test_sample.std()}\n"
         f"Медиана: {np.median(test_sample)}\n"
         f"Мода: {mode(test_sample, keepdims=True)}\n"
         f"Размах: {np.max(test_sample) - np.min(test_sample)}\n",
         color='желтый', separator_after=True)