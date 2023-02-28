from utils import my_print, probability_in_binomial_distribution, probability_in_puasson_distribution, \
    BinomialRandomValue, PuassonRandomValue
# -----------------------------формула Бернулли-----------------------------------------

my_print(msg="найти распределение вероятностей числа выпадений орла при трехкратном подбрасывании монетки",
         color='green', separator_before=True, separator_after=False)

for i in range(0, 4):
    my_print(msg=f"вероятность того, что орел выпадет {i} раз: "
                 f"{probability_in_binomial_distribution(k=i, n=3, p=0.5)}", color='blue', separator_after=False)

rand_val_1 = BinomialRandomValue(3, 0.5)

my_print(msg=f"С помощью классов: ", color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность наступления 3 событий при числе экспериментов 3: {rand_val_1.probability_m(3)}",
         color='фиолетовый',
         separator_after=False)
my_print(msg=f"Описательная статистика СВ: {rand_val_1}", color='фиолетовый', separator_after=False)

# -----------------------------формула Пуассона-----------------------------------------

my_print(msg="найти вероятность того, что среди 1000 писем, поступающих на почтовыя ящик за месяц встретиться 11 "
             "писем со спамом при условии, что вероятность поступления письма со спамом составляет 0.01",
         color='green', separator_before=True, separator_after=False)

for i in range(5, 15):
    my_print(msg=f"вероятность того, что поступит {i} спам-писем: "
                 f"{probability_in_puasson_distribution(lamb=1000*0.01, m=i)}", color='blue',
             separator_after=False)

rand_val_2 = PuassonRandomValue(1000, 0.01)

my_print(msg=f"С помощью классов: ", color='фиолетовый', separator_after=False)
my_print(msg=f"Вероятность наступления 7 событий: {rand_val_2.probability_m(7)}",
         color='фиолетовый',
         separator_after=False)
my_print(msg=f"Описательная статистика СВ: {rand_val_2}", color='фиолетовый', separator_after=False)
