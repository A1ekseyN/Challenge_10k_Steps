# Version - 0.0.4b

# Фичи:
# + Пройденое расстояние в км
# + Пройденое расстояние в среднем в день
# + Выполняется ли условие по прохождению 10.000 шагов в день Yes / No
# + Дописать калькулятор, который считае на сколько % перевыполнен план по количеству шагов в 10000
# + Добавить тексту цветов. Что бы информация визуально выделялась
# + Добавить отображение Min / Max количества шагов на протяжении дня за время челенджа
# + Добавить км за вчера и цветовую индикацию как у пройденых шагов
# + Добавить расчёт пройденого растояния, по разным городам. От Киева, и в сторону Львова. Добавил расстояние от Житомира, так, как лучше ориентируюсь в этом направлении
# + Количество kcal (1 kcal = 35 шагов) (Нужно уточнить сколько шагов нужно сделать что бы сжечь 1 ккал)
# + Добавить сколько шагов нужно сделать для прибытия в следующий город
# + Переписать код f" формат. Без использования кучи "+". А то, сложно править код, и нифига не понятно

# В среднем kcal в день. Пока не понятно или это вообще стоит считать.

# Поправить отображения цветов (В Среднем за день), возможно и в других местах. Прописан постоянный цвет, а нужно, что бы цвет менялся в зависимости от выполнения условия или его не выполнения
# Добавить отрисовку графиков (Пока, вообще не понимаю как это работает)
# Разобраться с окончаниями переменных: "дней", "шагов".
# Дописать код, который будет менять окончание переменной "дней", "шагов", в зависимости от нужного окончания


#############################################################
# Сама программа
#############################################################


from colorama import Fore, Back, Style
import math


# Список количества шагов по дням + основные переменные, которые вычисляются
STEPS = [10360, 16765, 10527, 16828, 10230, 10203, 10691, 10258, 10331, 13555, 13111, 10148, 11006, 10956, 11183, 10308, 10270, 10791, 10391, 10193, 10786, 10008, 10064, 10724, 12560, 13188, 10057, 10831, 10314, 10811]   # Масив по количеству пройденных шагов в день
steps_sum = sum(STEPS)  # Общие количество пройденых шагов
steps_average = int(steps_sum / len(STEPS))        # Среднее количество пройденых шагов в день
steps_max = max(STEPS)  # Показывает максимальное число пройденых шагов на протяжении одного дня
steps_min = min(STEPS)  # Показывает минимальное число пройденых шагов на протяжении одного дня

STEP_ONE_DISTANCE = 0.0007 # Длина одного шага в км
distance_km_sum = (round(steps_sum * STEP_ONE_DISTANCE, 1))     # Пройденая дистанкия в км
distance_km_average = (round(distance_km_sum / len(STEPS), 1))  # Средняя пройденая дистанция в км
distance_day_km = (round(STEPS[-1] * STEP_ONE_DISTANCE, 2))     # Пройденое расстояние за последний день
percentage_difference = (STEPS[-1] - steps_average) / steps_average * 100   # Разница в % между количеством шагов пройденых вреча, и общим средним количеством шагов
percentage_difference_round = (round(percentage_difference, 2))

# Вычисляет % на сколько больше хожу шагов, чем 10k. Пока нормально не работает, не понимаю, как считаются %.
percentage_difference_10k = (round(steps_average / 10000 * 10, 2))   # Разница в % между 10.000 шагами и средним кол-вом пройденых шагов за все время

# Проверка или выполняется challenge, и переменная стрелочек
challenge_last_day = None     # Проверяет или за последний день пройдено более 10к шагов
challenge_average = None     # Проверяет или среднее значение за все дни более 10к шагов
challenge_row = None     # Переменная для стрелочек вниз и вверх в юникоде

# Переменные для городов, которые высчитываются из общего пройденого расстояния в км:
travel_city = None      # Переменная для постройки пройденных городов
travel_next_city_distance_km = None     # Сколько осталось км до следующего города
travel_next_city = None     # Название следующего города
travel_predict_next_city_days = None    # Сколько дней идти до следующего города. Высчитывается из среднего кол-ва шагов в день
travel_predict_word_ending_days = None      # Уточнения окончания день/дня/дней, в переменной travel_predict_next_city_days
travel_steps_next_city = None      # Переменная для расчета кол-ва шагов до следующего города

# Переменные для kcal. + расчеты для кВт и литров бензина (1 kcal = 35 шагов), (1л бензина = 10500 ккал)
STEPS_FOR_ONE_KCAL = 35    # Сколько шагов на 1 kcal
kcal_sum = int(steps_sum / STEPS_FOR_ONE_KCAL)    # Общее кол-во затраченых kcal, за все время
kcal_last_day = int(STEPS[-1] / STEPS_FOR_ONE_KCAL)    # Кол-во kcal потраченых за последний день
KCAL_TO_KWT = 0.859845    # Коефициент для расчета, сколько ккал на один Ватт. 1 ккал = 1,163 Вт
kwt_sum = (round((kcal_sum * KCAL_TO_KWT) / 1000, 2))    # Расчёт, столько всего затрачено кВт, за все время
petrol_economy_liter = (round(kcal_sum / 10500, 3))   # Расчёт, сколько бензина съекономлена за все время. В 1л бензина - 10500 ккал

# Проверяет или за последний день пройдено более 10к шагов
if STEPS[-1] >= 10000:
    challenge_last_day = Fore.GREEN + "выполняются" + Style.RESET_ALL
else:
    challenge_last_day = Fore.RED + "НЕ выполняются" + Style.RESET_ALL

# Проверяет или среднее значение за все дни более 10к шагов
if STEPS[-1] >= steps_average:
    challenge_average = Fore.CYAN + "+"
else:
    challenge_average = Fore.RED

# Проверяет или за последний день пройдено более 10к шагов
if STEPS[-1] >= steps_average:
    challenge_row = "🠕"
else:
    challenge_row = "🠗"

# Вычисление из общего пройденного растояния город, в который я на данный момент дошел. Старт из Житомира.
# Города: Житомир, Новоград, Ровно, Дубно, Львов, Краковец.
# Затем высчитывает дистанцию до следующего города, и прогнознозированное время прибытия в днях.

if distance_km_sum >= 84.8:
    travel_city = "Житомир => Новоград"
if distance_km_sum >= 188:
    travel_city = "Житомир => Новоград => Ровно"
    travel_next_city_distance_km = round(237 - (distance_km_sum), 2)
    travel_next_city = "Дубно"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 237:
    travel_city = "Житомир => Новоград => Ровно => Дубно"
    travel_next_city_distance_km = round(402 - (distance_km_sum), 2)
    travel_next_city = "Львов"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 402:
    travel_city = "Житомир => Новоград => Ровно => Дубно => Львов"
    travel_next_city_distance_km = round(469 - (distance_km_sum), 2)
    travel_next_city = "Краковец"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 469:
    travel_city = "Житомир => Новоград => Ровно => Дубно => Львов => Краковец"

# Вычисление количества шагов до следующего города
travel_steps_next_city = round(travel_next_city_distance_km / STEP_ONE_DISTANCE)

# Вычисление окончания в слове "День" для прогнозиварония времени прибытья в следующий город.
if travel_predict_next_city_days == 1:
    travel_predict_word_ending_days = "день"
elif travel_predict_next_city_days < 5:
    travel_predict_word_ending_days = "дня"
else:
    travel_predict_word_ending_days = "дней"


# Вывод информции на экран

print("🏃 🚗")
print(Fore.CYAN + "===============================================" + Style.RESET_ALL + Fore.MAGENTA + "===" + Style.RESET_ALL)


print(f"Всего за {str(len(STEPS))} дня пройдено - {Fore.GREEN}{str(steps_sum)}{Style.RESET_ALL} шагов. (Вчера: + {Fore.MAGENTA}{str(STEPS[-1])}{Style.RESET_ALL}) ({challenge_average}{str(percentage_difference_round)} %{Style.RESET_ALL}) {challenge_row} :: (Min: {str(steps_min)} / Max: {str(steps_max)})")

print(f"В среднем в день: {Fore.GREEN}{str(steps_average)}{Style.RESET_ALL} шагов.")

print(f"\nОбщее расстояние: {Fore.CYAN}{str(distance_km_sum)}{Style.RESET_ALL} км (+ {str(distance_day_km)} км)")
print(f"В среднем: {str(distance_km_average)} км в день.")
print(f"Маршрут прошел по городам: {travel_city}")
print(f"До города {travel_next_city} осталось: {Fore.CYAN}{str(travel_next_city_distance_km)}{Style.RESET_ALL} км, или {travel_steps_next_city} шага. Прогнозированное, прибытие через {travel_predict_next_city_days} {travel_predict_word_ending_days}.")

print(f"\nНа ходьбу затрачено: {Fore.CYAN}{kcal_sum}{Style.RESET_ALL} kcal, (вчера {kcal_last_day} kcal).")
print(f"Эквивалент: {Fore.CYAN}{kwt_sum}{Style.RESET_ALL} кВт, или {Fore.CYAN}{petrol_economy_liter}{Style.RESET_ALL} л бензина.")

print(f"\nУсловия испытания {challenge_last_day} на протяжении {str(len(STEPS))}.")


print(Fore.CYAN + "==============================================="+ Style.RESET_ALL)

