from Practice.utils import my_print, grad_descent, koef_lin_regres_mnk_method_calculation, \
    koef_lin_regr_matrix_method_calculation
import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------------------------------------------------
task = "Даны значения величины заработной платы заемщиков банка (zp) \n" \
       "и значения их поведенческого кредитного скоринга (ks): \n" \
       "zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110], \n" \
       "ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]. \n" \
       "Используя математические операции, посчитать коэффициенты линейной регрессии, \n" \
       "приняв за X заработную плату (то есть, zp - признак), \n" \
       "а за y - значения скорингового балла (то есть, ks - целевая переменная). \n" \
       "Произвести расчет как с использованием intercept, так и без."

my_print(msg=task, separator_before=True, separator_after=False, color='зеленый')
x = np.array([1, 2, 3, 4, 5])

y_true = 2 + 3 * x

b0_gd_int, b1_gd_int = grad_descent(b0_start=1, b1_start=2, x=x, y_true=y_true,
                                    n_epoch=50000, lr=0.001)
b0_gd_not_int, b1_gd_not_int = grad_descent(b0_start=0, b1_start=2, x=x, y_true=y_true,
                                            n_epoch=50000, lr=0.001, intercept=False)
b0_mnk_int, b1_mnk_int = koef_lin_regres_mnk_method_calculation(x, y_true)
b0_mnk_not_int, b1_mnk_not_int = koef_lin_regres_mnk_method_calculation(x, y_true, intercept=False)
b0_mk_int, b1_mk_int = koef_lin_regr_matrix_method_calculation(x, y_true)
b0_mk_not_int, b1_mk_not_int = koef_lin_regr_matrix_method_calculation(x, y_true, intercept=False)


my_print(msg=f"Коэффициенты ЛР методом градиентного спуска c intercept: {b0_gd_int, b1_gd_int}\n"
             f"Коэффициенты ЛР методом градиентного спуска без intercept: {b0_gd_not_int, b1_gd_not_int}\n"
             f"Коэффициенты ЛР матричным способом c intercept: {b0_mk_int, b1_mk_int}\n"
             f"Коэффициенты ЛР матричным способом без intercept: {b0_mk_not_int, b1_mk_not_int}\n"
             f"Коэффициенты ЛР МНК c intercept: {b0_mnk_int, b1_mnk_int}\n"
             f"Коэффициенты ЛР МНК без intercept: {b0_mnk_not_int, b1_mnk_not_int}\n",
         color='синий')



# ----------------------------------------------------------------------------------------------------------------
task = "Посчитать коэффициент линейной регрессии при заработной плате (zp), \n" \
       "используя градиентный спуск (без intercept).\n" \
       "Произвести расчет как с использованием intercept, так и без."

my_print(msg=task, separator_before=True, separator_after=False, color='зеленый')

# ----------------------------------------------------------------------------------------------------------------
task = "В каких случаях для вычисления доверительных интервалов и проверки статистических гипотез \n" \
       "используется таблица значений функции Лапласа, а в каких - таблица критических точек распределения Стьюдента?\n"
my_print(msg=task, separator_before=True, separator_after=False, color='зеленый')

# ----------------------------------------------------------------------------------------------------------------
task = "Произвести вычисления как в пункте 2, но с вычислением intercept. \n" \
       "Учесть, что изменение коэффициентов должно производиться на каждом шаге одновременно \n" \
       "(то есть изменение одного коэффициента не должно влиять на изменение другого во время одной итерации)."

my_print(msg=task, separator_before=True, separator_after=False, color='зеленый')
