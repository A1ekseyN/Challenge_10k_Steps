# Version - 0.1.3b

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
# + Вычисление запаса шагов, до среднего значения в 10к.
# + Добавлена статистика по количеству сожжённых кг жира, и статистика по эквиваленту Big Mac
# + Изменено отображение общего кол-ва шагов
# + Добавлен показатель общего запаса шагов
# + Добавлено отображение кол-ва дней в которые пройдено более 10к шагов, и пересчет в %.
# + Добавлена статистика по дням недели.
# + Отображение количества последних дней, за которые пройдено более 10к шагов.
# + Добавить отрисовку графиков (Среднее число шагов + средняя медианная по дням)
# + Читаем данные из *.csv файла

#  Идеи:
# Визуализация маршрута с помощью Plotly Scattermapbox.
# Можно сделать анимацию графиков: по дням, по карте
# Поправить отображения цветов (В Среднем за день), возможно и в других местах. Прописан постоянный цвет, а нужно, что бы цвет менялся в зависимости от выполнения условия или его не выполнения
# Разобраться с окончаниями переменных: "дней", "шагов".
# Дописать код, который будет менять окончание переменной "дней", "шагов", в зависимости от нужного окончания
# Статистика по времени прогулок. В MiFit появилась статистика времени по дням. Сколько времени в день длилась прогулка. (Можно использовать вложенные словари)
# Добавить статистику по часам прогулок: в котором часу больше сделано шагов, относительно времени соток, времени в конкретный день.
# Влияние кол-ва пройденных шагов на количество сна.

# Начало Challenge - 26.08.2021 (Чт).


from colorama import Fore, Back, Style
import math
import time
import statistics
import matplotlib.pyplot as plt
import csv

start_time = time.time()

with open("ACTIVITY_STEPS_ALL_TIME.csv") as file_steps:
    # Создаем объект DirectRider, указываем разделитель ";"
    file_reader_steps = csv.DictReader(file_steps, delimiter=';')
    steps = []  # Переменная, для того, что бы прочитать кол-во шагов из файла

    # Считываем данные по шагам из файла
    for row in file_reader_steps:
        steps.append(int(row["steps"]))

# !!!!!! Начало в четверг!!!!!!! (22.02.2018)
#STEPS = [11250, 10129, 13325, 10903, 4283, 13402, 6001, 8433, 12340, 15317, 7331, 14092, 6529, 8929, 8590, 9016, 5176, 7964, 5041, 10447, 7748, 16176, 7354, 9748, 7404, 6185, 9049, 12302, 8499, 7304, 5944, 14642, 15029, 7825, 7820, 7725, 12096, 9241, 14665, 8663, 13457, 13689, 12042, 12492, 10047, 9084, 7876, 14702, 8321, 13574, 8091, 9607, 9322, 15743, 13160, 12149, 8339, 7670, 9130, 10577, 15922, 11067, 4878, 7849, 9254, 16903, 4635, 11003, 15838, 5250, 11170, 7778, 4833, 10242, 7750, 5983, 6888, 7767, 9230, 13041, 5703, 6417, 5059, 9492, 10403, 9229, 9197, 11142, 9994, 12215, 13026, 5160, 6735, 8595, 4043, 23900, 15544, 17496, 14280, 20023, 24675, 5253, 8814, 7815, 7015, 9443, 7652, 9340, 5429, 14233, 11331, 8183, 10062, 11720, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 6807, 21308, 29087, 21713, 13902, 9733, 5504, 8864, 5008, 8733, 10705, 8500, 6303, 11168, 13079, 8927, 13226, 10098, 9226, 10971, 10006, 13079, 17399, 2606, 6576, 6750, 6416, 8405, 8018, 14024, 5869, 4618, 10446, 11039, 9846, 10816, 10071, 5918, 12686, 5905, 10322, 7737, 7317, 7759, 3743, 10373, 9009, 9858, 5483, 4257, 5972, 7872, 10161, 9065, 6243, 4337, 8056, 21403, 23031, 4752, 14283, 4124, 6402, 7173, 4812, 5457, 10015, 9078, 5578, 6118, 11576, 4768, 7885, 4967, 4971, 10740, 5490, 16741, 21248, 13586, 13266, 10533, 13678, 17908, 12216, 14416, 8817, 11225, 23197, 3710, 4074, 4573, 4455, 2945, 7010, 7159, 6376, 5890, 2236, 12641, 5217, 11015, 5032, 7385, 9185, 14290, 7053, 4209, 12427, 1848, 5206, 6717, 8197, 6145, 8643, 5603, 6924, 8111, 4455, 2579, 4630, 5558, 5086, 10607, 4305, 12203, 8302, 7230, 7613, 5187, 8021, 4472, 5038, 8102, 8451, 4755, 2316, 1796, 2064, 5683, 2623, 5054, 6048, 5095, 7814, 12764, 13059, 10167, 10065, 15051, 19631, 8524, 8301, 7836, 10515, 10310, 10750, 9705, 17561, 9083, 11125, 11448, 9643, 10575, 20082, 13514, 11369, 10940, 15996, 7808, 11025, 6340, 8436, 8908, 7757, 7374, 5937, 27450, 8918, 7576, 11614, 10427, 11093, 4140, 14495, 8044, 10294, 15065, 7086, 10787, 9270, 9155, 11993, 2044, 10076, 10693, 10055, 9382, 9208, 12487, 12910, 6940, 15705, 13240, 16443, 14586, 10632, 7963, 8848, 11108, 9444, 6849, 9180, 14521, 12378, 7445, 8310, 7206, 9554, 8334, 7975, 10750, 9498, 13804, 15539, 24380, 19313, 10982, 3840, 16915, 10916, 6396, 6859, 5011, 5313, 7116, 7751, 4266, 5823, 8075, 2870, 3991, 8500, 6617, 7202, 7265, 7179, 11447, 5306, 10431, 9011, 5276, 10561, 10272, 6900, 12419, 3661, 5144, 20053, 13449, 18045, 10672, 7611, 10155, 11764, 8556, 4076, 5580, 4110, 2879, 6135, 5181, 12542, 10567, 16747, 10012, 4948, 5820, 12719, 10931, 9292, 10944, 8559, 5811, 16007, 5241, 17614, 9708, 4001, 3981, 15771, 3371, 6086, 3022, 12080, 8472, 7240, 5959, 5219, 6844, 3692, 5598, 4265, 6875, 9462, 15572, 3478, 4531, 4302, 8704, 6227, 10792, 4029, 7478, 7282, 12561, 6705, 6907, 7249, 6556, 7540, 11011, 9248, 5532, 10054, 9378, 17613, 8753, 5292, 13269, 11999, 14181, 8131, 14303, 8611, 9163, 4016, 10249, 9164, 15217, 9039, 4893, 6245, 7075, 7440, 8314, 12330, 7876, 6766, 8009, 8466, 8057, 8234, 12095, 9393, 8044, 10634, 13527, 7149, 14231, 19147, 10737, 11003, 6426, 6523, 5304, 5471, 6733, 14166, 10532, 8148, 6476, 6130, 7619, 10845, 12860, 9676, 10325, 8232, 7677, 12751, 8500, 10919, 10089, 7140, 7366, 7846, 6802, 12311, 9717, 10476, 5234, 7284, 7837, 13132, 10071, 14832, 14483, 4909, 6096, 6657, 8150, 10124, 4299, 6920, 6385, 3322, 12425, 10923, 9219, 7949, 11597, 9084, 5388, 8752, 11074, 5738, 3147, 7674, 7317, 8762, 9225, 7120, 12551, 7227, 9004, 7042, 8855, 6135, 5716, 11899, 7287, 6281, 9636, 2051, 11054, 15930, 10782, 8443, 3684, 9203, 12339, 13637, 14644, 9025, 8712, 8086, 8237, 5340, 10172, 8519, 5121, 4815, 5052, 5429, 7248, 7858, 7070, 4348, 2885, 6587, 11638, 6375, 8664, 8640, 3259, 7800, 5537, 8160, 6950, 10276, 7391, 10162, 8309, 6671, 5809, 7343, 5856, 7533, 5745, 6607, 6647, 11276, 9261, 3977, 7627, 9304, 6859, 5565, 5581, 9754, 8280, 25279, 23805, 19413, 18300, 13290, 7470, 5646, 9042, 5565, 3463, 6285, 10246, 10785, 4545, 12911, 5731, 5964, 6384, 3747, 5814, 3847, 10162, 6782, 3392, 4275, 4568, 5050, 6868, 6374, 11958, 7950, 11788, 12493, 6910, 11937, 12843, 14217, 7817, 8450, 5602, 6678, 9121, 6354, 6331, 5608, 7568, 6762, 5785, 6306, 12359, 6058, 4233, 9299, 8360, 22375, 22007, 12007, 14071, 14729, 12121, 7457, 7120, 9568, 7102, 11894, 6496, 4393, 10485, 5115, 6867, 5305, 4652, 6435, 5922, 9289, 6334, 6444, 4808, 7578, 7012, 7247, 6052, 5697, 6380, 5563, 8151, 2865, 13117, 6582, 3028, 3154, 15622, 6812, 10044, 8391, 11719, 4568, 9384, 12197, 4049, 5832, 5809, 3546, 12884, 9229, 9280, 9912, 5562, 5902, 10486, 8460, 9584, 11280, 13611, 3652, 4802, 5324, 7577, 11318, 4784, 3533, 9261, 5115, 7710, 4628, 3927, 4750, 3291, 15395, 10363, 3843, 3763, 14632, 13045, 2564, 18416, 6372, 2692, 2767, 5676, 6113, 5114, 6249, 4142, 4995, 6426, 7834, 7758, 7927, 13699, 7467, 7110, 3527, 4545, 7966, 7910, 15983, 4806, 2558, 5589, 3285, 9340, 6375, 10033, 4581, 4720, 3262, 7907, 5608, 8658, 4030, 2858, 4900, 5222, 4521, 6967, 4623, 5019, 3667, 3374, 2495, 11966, 3491, 10119, 4501, 2745, 7081, 5428, 9131, 6496, 5047, 7781, 9488, 4146, 5485, 6615, 9036, 8452, 5785, 4613, 11058, 5161, 6917, 6141, 11215, 6663, 12344, 4980, 3012, 5691, 4977, 5363, 3965, 5344, 8358, 11288, 4963, 6011, 9185, 5288, 6432, 6788, 10580, 4978, 13153, 8263, 8645, 16388, 10021, 10419, 11328, 13667, 6960, 7315, 4446, 8013, 5242, 4878, 9649, 14827, 11774, 3375, 6819, 6332, 6109, 4363, 7380, 7272, 4592, 5742, 7114, 5881, 5052, 7173, 18975, 11708, 14729, 16777, 5545, 4565, 5323, 3109, 4810, 4615, 4070, 5721, 6098, 4323, 6268, 10333, 6833, 6788, 8005, 6562, 8952, 5532, 7742, 10180, 7627, 3874, 10992, 17165, 8004, 4887, 12056, 3544, 11958, 8379, 5808, 10133, 6136, 7844, 5077, 5230, 14430, 11948, 8531, 8427, 8438, 6027, 3919, 5983, 5975, 9220, 8753, 9130, 9260, 7686, 6991, 11982, 6115, 4474, 6931, 3754, 15906, 6449, 10573, 4812, 12402, 12912, 13438, 7412, 10019, 27414, 36071, 15714, 6107, 5179, 10948, 19723, 7547, 3786, 7845, 3327, 4447, 4860, 6149, 8538, 6257, 10448, 4443, 11942, 1730, 14134, 4666, 5071, 6173, 11704, 4607, 6247, 6375, 4182, 16180, 7471, 12555, 5760, 9328, 5713, 14030, 6049, 5951, 6069, 12854, 4836, 14217, 5776, 2423, 4852, 2799, 4480, 12941, 4175, 4829, 5377, 4460, 6602, 4913, 9493, 7650, 8681, 11133, 2283, 6924, 8551, 5273, 5646, 8666, 12462, 8533, 6941, 5393, 7105, 10014, 14616, 17650, 12114, 9742, 9153, 6854, 7490, 6955, 5643, 8014, 4923, 4150, 8185, 7808, 2864, 4063, 9195, 5844, 8335, 21253, 4786, 6326, 9011, 7229, 7458, 8428, 6157, 7127, 13757, 5883, 9739, 2431, 5295, 9040, 6559, 2450, 7642, 7836, 5899, 3269, 8312, 8302, 5830, 10216, 3932, 7072, 8713, 6760, 11349, 9819, 11162, 7539, 7225, 7771, 6111, 11532, 11617, 2987, 6177, 7625, 11542, 19291, 17431, 4074, 908, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 15032, 5804, 9979, 6299, 10188, 10308, 11610, 5317, 2313, 5661, 12523, 6381, 6636, 3126, 11301, 7114, 6989, 3523, 13559, 6180, 5321, 11520, 7981, 5041, 6151, 9717, 4562, 3423, 3005, 2288, 14729, 8357, 4324, 3475, 8688, 6964, 3506, 8606, 10506, 10610, 13750, 6635, 2814, 9509, 8162, 21713, 14372, 13596, 3862, 3034, 11850, 2679, 7685, 4327, 3698, 16097, 3939, 13327, 8197, 5941, 8878, 5414, 3772, 10886, 10295, 7183, 8527, 9160, 8989, 11296, 8703, 14173, 10407, 12266, 10083, 6949, 8663, 4858, 4465, 10319, 10037, 6337, 4113, 7453, 15553, 6481, 6680, 13958, 14490, 15722, 9856, 2594, 7494, 10566, 6600, 8214, 9240, 4640, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 6913, 2634, 10301, 3434, 2866, 11327, 18068, 2480, 8688, 3033, 7554, 16120, 8445, 15145, 13148, 17328, 4215, 1611, 5837, 8646, 3793, 5408, 4350, 4839, 7490, 4302, 2667, 11191, 7562, 5340, 7524, 3714, 10671, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5026, 6971, 5522, 5254, 6392, 7085, 8821, 2698, 5029, 4933, 8290, 8454, 6608, 18942, 11899, 9875, 10741, 6886, 6269, 5691, 5496, 7663, 2710, 5325, 6300, 4014, 5459, 4413, 14453, 5396, 8647, 10913, 8562, 9222, 8842, 5925, 6442, 9348, 8394, 12344, 7911, 6263, 9085, 5120, 5224, 8204, 10360, 16765, 10527, 16828, 10230, 10203, 10691, 10258, 10331, 13555, 13111, 10148, 11006, 10956, 11183, 10308, 10270, 10791, 10391, 10193, 10786, 10008, 10064, 10724, 12560, 13188, 10057, 10831, 10314, 10811, 10226, 10055, 10705, 10272, 10617, 10153, 10299, 10867, 10796, 11196, 10669, 10452, 10594, 16675, 11161, 12918, 10315, 11860, 10334, 11126, 10279, 11065, 10523, 11553, 10425, 10089, 10618, 10567, 10888, 10463, 10845, 12171, 10107, 10101, 10221, 10199, 10716, 11570, 10054, 10250, 14385, 13306, 13232, 10037, 12036, 10288, 10075, 12174, 11660, 10642, 10393, 11421, 11523, 10506, 11644, 10001, 13336, 11975, 11096, 10006, 10457, 10676, 10075, 10546, 12568, 10542, 11138, 10284, 10095, 10362, 15955, 11461, 10592, 10680, 10809, 10034, 10633, 10636, 10396, 13052, 10313, 10692, 10063, 11012, 10033, 10299, 12011, 10615, 10964, 11159, 11485, 10466, 10619, 13599, 10579, 10172, 10322, 10400, 12236, 10437, 10639, 14110, 12101, 10022, 10027, 11260, 10449, 11072, 8220, 5987, 5723, 5117, 9531, 14491, 7639, 4393, 6999, 10099, 13892, 6532, 20215, 10036, 4608, 12357, 6813, 8030, 3047, 12059, 2133, 2968, 6151, 7106, 8160, 5799, 4577, 5183, 6791, 5828, 11233, 6063, 2919, 5762, 8229, 4725, 2325, 3093, 5859, 3621, 9186, 6197, 6892, 10081, 11918, 9817, 18567, 17743, 9443, 15476, 2902, 5928, 949, 965, 4258, 6479, 6078, 11259, 6542, 10124, 11722, 12180, 11601, 10583, 12855, 10491, 10055, 2260, 11390, 4276, 10730, 11807, 10005, 11876, 7303, 10592, 10014, 13469, 10006, 6392, 7756, 10055, 12014, 9041, 10050, 10305, 10043, 8992, 3127, 10034, 11065, 8661, 10052, 10411, 10398, 10030, 10031, 5640, 10152, 10064, 6926, 10765, 8092, 4227, 6689, 4746, 10028, 6016, 7649, 7398, 3973, 8094, 4747, 5897, 6190, 6191, 9446, 10664, 5878, 8838, 6426, 5119, 4190, 10224, 6228, 5417, 3689, 4328, 6491, 10313, 8257, 10951, 11751, 10451, 4834, 6437, 5138, 2997, 10394, 5205, 5608, 6524, 5580, 5681, 5502, 5798, 6201, 10640, 7014, 7410, 6188, 6695, 6466, 3045, 4134, 5067, 12088, 4490, 10136, 5688, 5570, 5013, 4643, 6619, 3746, 3150, 4171, 7306, 3830, 4576, 4080, 3105, 6727, 7088, 4622, 7145, 4020, 5865, 8072, 5305, 8522, 3278, 2880, 5166, 7625, 6200, 7791, 4122, 4738, 4600, 7793, 5365, 6708, 7521, 3620, 2432, 7622, 4392, 6389, 7614, 7114, 7023, 10264, 5074, 7150, 5273, 7953, 8147, 5434, 7152, 8076, 4501, 5962, 5900, 7669, 20882, 8289, 11909, 10057, 5622, 4190, 5771, 4865, 4177, 6767, 7070, 5347, 7494, 7442, 10303, 10170, 10131, 5885, 10101, 5600, 5372, 11234, 10338, 10122, ]
STEPS = steps + [10204, ]

steps_sum = sum(STEPS)  # Общие количество пройденых шагов
steps_average = int(steps_sum / len(STEPS))        # Среднее количество пройденых шагов в день
steps_average_last_30_days = int(sum(STEPS[-30:]) / 30)     # Среднее кол-во шагов за последние 30 дней
steps_average_last_90_days = int(sum(STEPS[-90:]) / 90)     # Среднее кол-во шагов за последние 90 дней
steps_average_last_180_days = int(sum(STEPS[-180:]) / 180)     # Среднее кол-во шагов за последние 180 дней
steps_average_last_360_days = int(sum(STEPS[-360:]) / 360)     # Среднее кол-во шагов за последние 360 дней
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

# Формула для расчёта запаса шагов до среднего значения в 10к
stock_steps_to_10k_per_day = ((steps_average - 10000) * len(STEPS))
#stock_days_steps_to_10k_per_day = (stock_steps_to_10k_per_day / 10000) # Формула расчёта количества дней в запасе.

# Цикл подсчёта количества дней, где шагов более 10к за день.
steps_more_10k = STEPS[:]
steps_more_10k.sort()

for steps_without_smaller_10k_cycle in steps_more_10k:
    if steps_more_10k[0] <= 10000:
        del steps_more_10k[0]

# Цикл для посчёта сколько последних дней выполняется челендж.
# Количество последних дней, за которые пройдено более 10к шагов на протяжении дня.
steps_flipped = STEPS[::-1] # Перевернутый список шагов по дням.
challenge_last_days_go_on = 0 # Переменная для вывода количества последних дней выполнения челенджа.

while steps_flipped [0] >= 10000:
    challenge_last_days_go_on += 1 # Кол-во последних дней, за которые пройдено более 10к шагов.
    del steps_flipped[0]

# Считает % дней, в которых пройдено более 10к шагов на протяжении дня
percent_steps_more_10k = ((len(steps_more_10k) / len(STEPS)) * 100)

# Переменные для городов, которые высчитываются из общего пройденого расстояния в км:
travel_city = None      # Переменная для постройки пройденных городов
travel_next_city_distance_km = None     # Сколько осталось км до следующего города
travel_next_city = None     # Название следующего города
travel_predict_next_city_days = None    # Сколько дней идти до следующего города. Высчитывается из среднего кол-ва шагов в день
travel_predict_word_ending_days = None      # Уточнения окончания день/дня/дней, в переменной travel_predict_next_city_days
travel_steps_next_city = None      # Переменная для расчета кол-ва шагов до следующего города

# Переменные для kcal. + расчёты для кВт и литров бензина (1 kcal = 35 шагов), (1л бензина = 10500 ккал)
STEPS_FOR_ONE_KCAL = 35    # Сколько шагов на 1 kcal
kcal_sum = int(steps_sum / STEPS_FOR_ONE_KCAL)    # Общее кол-во затраченых kcal, за все время
kcal_last_day = int(STEPS[-1] / STEPS_FOR_ONE_KCAL)    # Кол-во kcal потраченых за последний день
KCAL_TO_KWT = 0.859845    # Коефициент для расчета, сколько ккал на один Ватт. 1 ккал = 1,163 Вт
kwt_sum = (round((kcal_sum * KCAL_TO_KWT) / 1000, 2))    # Расчёт, столько всего затрачено кВт, за все время
petrol_economy_liter = (round(kcal_sum / 10500, 1))   # Расчёт, сколько бензина съекономлена за все время. В 1л бензина - 10500 ккал
BIG_MAC_KCAL = 257
big_mac_used = int(kcal_sum / BIG_MAC_KCAL)
kcal_to_fat = (round((kcal_sum / 9) / 1000, 2)) # Расчёт потреченных кг жира


# Подсчёт среднего значения шагов по дням + средння медианная.
days_average_steps = []
days_median_steps = []

def days_average_median():
    # Вычисления для средней медианной
    days = []
    for day in STEPS:
        days.append(int(day))
        days_average_steps.append(int(sum(days) / len(days)))
        days_median_steps.append(int(statistics.median(days)))

days_average_median()


# Вычисление среднего значения за 30, 90, 180, 360 последних дней.
days_average_30_graph = []       # Переменная для кол-ва шагов в среднем за последние 30 дней.
days_average_180_graph = []      # Переменная для кол-ва шагов в среднем за последние 180 дней.
days_average_360_graph = []      # Переменная для кол-ва шагов в среднем за последние 360 дней.

def days_average_30():
    # Вычисления для среднего значения за последние 30 дней.
    days_30_temp = []  # Переменная для временных вычислений
    for value in STEPS:
        days_30_temp.append(value)
        if len(days_30_temp) > 30:
            days_30_temp.remove(days_30_temp[0])
        average_30_temp = sum(days_30_temp) / len(days_30_temp)
        days_average_30_graph.append(int(average_30_temp))

days_average_30()

def days_average_180():
    # Вычисления для среднего значения за последние 180 дней.
    days_180_temp = []  # Переменная для временных вычислений
    for value in STEPS:
        days_180_temp.append(value)
        if len(days_180_temp) > 180:
            days_180_temp.remove(days_180_temp[0])
        average_180_temp = sum(days_180_temp) / len(days_180_temp)
        days_average_180_graph.append(int(average_180_temp))

days_average_180()

def days_average_360():
    # Вычисления для среднего значения за последние 180 дней.
    days_360_temp = []  # Переменная для временных вычислений
    for value in STEPS:
        days_360_temp.append(value)
        if len(days_360_temp) > 360:
            days_360_temp.remove(days_360_temp[0])
        average_360_temp = sum(days_360_temp) / len(days_360_temp)
        days_average_360_graph.append(int(average_360_temp))

days_average_360()

# Срезы данных для подсчёта статистики по конкретным дням недели.
# Начало Challenge - 26.08.2021 (Чт). # Важно для правильного подсчёта первого дня. Расчёт начинается с Четверга.

day_monday = STEPS[slice(4, None, 7)]
day_monday_average = int((sum(day_monday)) / (len(day_monday)))
day_monday_median = statistics.median(STEPS[slice(4, None, 7)])
day_tuesday = STEPS[slice(5, None, 7)]
day_tuesday_average = int((sum(day_tuesday)) / (len(day_tuesday)))
day_tuesday_median = statistics.median(STEPS[slice(5, None, 7)])
day_wednesday = STEPS[slice(6, None, 7)]
day_wednesday_average = int((sum(day_wednesday)) / (len(day_wednesday)))
day_wednesday_median = statistics.median(STEPS[slice(6, None, 7)])
day_thursday = STEPS[slice(0, None, 7)]
day_thursday_average = int((sum(day_thursday)) / (len(day_thursday)))
day_thursday_median = statistics.median(STEPS[slice(0, None, 7)])
day_friday = STEPS[slice(1, None, 7)]
day_friday_average = int((sum(day_friday)) / (len(day_friday)))
day_friday_median = statistics.median(STEPS[slice(1, None, 7)])
day_saturday = STEPS[slice(2, None, 7)]
day_saturday_average = int((sum(day_saturday)) / (len(day_saturday)))
day_saturday_median = statistics.median(STEPS[slice(2, None, 7)])
day_sunday = STEPS[slice(3, None, 7)]
day_sunday_average = int((sum(day_sunday)) / (len(day_sunday)))
day_sunday_median = statistics.median(STEPS[slice(3, None, 7)])

# Переменная для отображения среднего количества шагов за день + показатели Min и Max шагов за ден, средняя медианная .
# Словарь с информацией для статистики по дням.
avarage_steps_days_of_week = {
    "понедельник:": {
        "average_day": (day_monday_average),
        "median_day": int(day_monday_median),
        "min_day": min(day_monday),
        "max_day": max(day_monday),
        },
    "вторник:    ": {
        "average_day": (day_tuesday_average),
        "median_day": int(day_tuesday_median),
        "min_day": min(day_tuesday),
        "max_day": max(day_tuesday),
        },
    "среда:      ": {
        "average_day": (day_wednesday_average),
        "median_day": int(day_wednesday_median),
        "min_day": min(day_wednesday),
        "max_day": max(day_wednesday),
        },
    "четверг:    ": {
        "average_day": (day_thursday_average),
        "median_day": int(day_thursday_median),
        "min_day": min(day_thursday),
        "max_day": max(day_thursday),
        },
    "пятница:    ": {
        "average_day": (day_friday_average),
        "median_day": int(day_friday_median),
        "min_day": min(day_friday),
        "max_day": max(day_friday),
        },
    "суббота:    ": {
        "average_day": (day_saturday_average),
        "median_day": int(day_saturday_median),
        "min_day": min(day_saturday),
        "max_day": max(day_saturday),
        },
    "воскресение:": {
        "average_day": (day_sunday_average),
        "median_day": int(day_sunday_median),
        "min_day": min(day_sunday),
        "max_day": max(day_sunday),
        }
    }

#hour_stat_steps = []

# Подсчёт кол-ва шагов в конкретный час дня.
with open("ACTIVITY_MINUTE_ALL_TIME.csv") as r_file:
    file_reader = csv.DictReader(r_file, delimiter=";")

    hour_stat_steps = {
        '00:00-00:59': [], '01:00-01:59': [], '02:00-02:59': [], '03:00-03:59': [], '04:00-04:59': [], '05:00-05:59': [],
        '06:00-06:59': [], '07:00-07:59': [], '08:00-08:59': [], '09:00-09:59': [], '10:00-10:59': [], '11:00-11:59': [],
        '12:00-12:59': [], '13:00-13:59': [], '14:00-14:59': [], '15:00-15:59': [], '16:00-16:59': [], '17:00-17:59': [],
        '18:00-18:59': [], '19:00-19:59': [], '20:00-20:59': [], '21:00-21:59': [], '22:00-22:59': [], '23:00-23:59': [],
        }
    for row in file_reader:
        if int(row['time'][:-3]) == 0:
            hour_stat_steps['00:00-00:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 1:
            hour_stat_steps['01:00-01:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 2:
            hour_stat_steps['02:00-02:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 3:
            hour_stat_steps['03:00-03:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 4:
            hour_stat_steps['04:00-04:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 5:
            hour_stat_steps['05:00-05:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 6:
            hour_stat_steps['06:00-06:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 7:
            hour_stat_steps['07:00-07:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 8:
            hour_stat_steps['08:00-08:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 9:
            hour_stat_steps['09:00-09:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 10:
            hour_stat_steps['10:00-10:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 11:
            hour_stat_steps['11:00-11:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 12:
            hour_stat_steps['12:00-12:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 13:
            hour_stat_steps['13:00-13:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 14:
            hour_stat_steps['14:00-14:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 15:
            hour_stat_steps['15:00-15:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 16:
            hour_stat_steps['16:00-16:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 17:
            hour_stat_steps['17:00-17:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 18:
            hour_stat_steps['18:00-18:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 19:
            hour_stat_steps['19:00-19:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 20:
            hour_stat_steps['20:00-20:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 21:
            hour_stat_steps['21:00-21:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 22:
            hour_stat_steps['22:00-22:59'].append(int(row['steps']))
        if int(row['time'][:-3]) == 23:
            hour_stat_steps['23:00-23:59'].append(int(row['steps']))

    hour_stat_steps_sum = sum(sum(hour_stat_steps.values(), []))


# Проверяет или за последний день пройдено более 10к шагов.
if STEPS[-1] >= 10000:
    challenge_last_day = Fore.GREEN + "больше" + Style.RESET_ALL
else:
    challenge_last_day = Fore.RED + "меньше" + Style.RESET_ALL

# Проверяет или среднее значение за все дни более 10к шагов.
if STEPS[-1] >= steps_average:
    challenge_average = Fore.CYAN + "+"
else:
    challenge_average = Fore.RED

# Проверяет или за последний день пройдено более 10к шагов.
if STEPS[-1] >= steps_average:
    challenge_row = "🠕"
else:
    challenge_row = "🠗"

# Вычисление из общего пройденного растояния город, в который я на данный момент дошел. Старт из Житомира.
# Затем высчитывает дистанцию до следующего города, и прогнознозированное время прибытия в днях.

### Названия городов для правильного расчёта расстояния:
# Житомир => Львов => Краков => Dolny Kubin, Братислава, Грац (Австрия), Njivice, Венеция, Вокгур Итальянского полуострова, Ницца, Барселона, Тарифа (7391 км)
# https://www.google.com.ua/maps/dir/%D0%96%D0%B8%D1%82%D0%BE%D0%BC%D0%B8%D1%80/%D0%94%D0%BE%D0%BB%D0%BD%D1%8B+%D0%9A%D1%83%D0%B1%D0%B8%D0%BD/%D0%91%D1%80%D0%B0%D1%82%D0%B8%D1%81%D0%BB%D0%B0%D0%B2%D0%B0/%D0%93%D1%80%D0%B0%D1%86,+%D0%90%D0%B2%D1%81%D1%82%D1%80%D0%B8%D1%8F/%D0%9D%D1%96%D0%B2%D0%B8%D1%86%D0%B5,+%D0%A5%D0%BE%D1%80%D0%B2%D0%B0%D1%82%D0%B8%D1%8F/%D0%92%D0%B5%D0%BD%D0%B5%D1%86%D0%B8%D1%8F,+%D0%98%D1%82%D0%B0%D0%BB%D0%B8%D1%8F/%D0%A2%D0%B0%D1%80%D0%B8%D1%84%D0%B0,+%D0%98%D1%81%D0%BF%D0%B0%D0%BD%D0%B8%D1%8F/@40.4779137,4.2307939,5.26z/data=!4m79!4m78!1m10!1m1!1s0x472c64a32bfa355d:0xf14ad2a3d9b9e229!2m2!1d28.6586669!2d50.25465!3m4!1m2!1d20.9176217!2d50.0551705!3s0x473d83c6649caa7b:0x1fcee554f38dc479!1m5!1m1!1s0x4715b1a430a9c16f:0x400f7d1c69708c0!2m2!1d19.2968746!2d49.212679!1m5!1m1!1s0x476c89360aca6197:0x631f9b82fd884368!2m2!1d17.1077478!2d48.1485965!1m5!1m1!1s0x476e3587173065bb:0xfe8e8ad1d2dfdd9b!2m2!1d15.439504!2d47.070714!1m5!1m1!1s0x4763643854f2c763:0xd1a2ff912e5dc48b!2m2!1d14.5448533!2d45.1644434!1m35!1m1!1s0x477eb1daf1d63d89:0x7ba3c6f0bd92102f!2m2!1d12.3155151!2d45.4408474!3m4!1m2!1d17.0004967!2d40.5984243!3s0x13470bdbcec1ba9f:0x830e97bd1d6537c7!3m4!1m2!1d17.1308356!2d39.0669494!3s0x1340485eaae7e579:0x8be496935ac90db0!3m4!1m2!1d16.0616966!2d37.9252918!3s0x1314ec78f174adb5:0x2bc4fbc9ff540276!3m4!1m2!1d14.9988326!2d36.8375669!3s0x1311886fa85d94d7:0xe0f6df126a3ab7e7!3m4!1m2!1d13.714939!2d37.1973034!3s0x131087e9cc1c9379:0x9d698167f8fed664!3m4!1m2!1d12.4594496!2d37.7772536!3s0x131bc2605a54de95:0x1e3064240bc37aa1!1m5!1m1!1s0xd0c8ef7c23f1c63:0x2ce0f2832aa48963!2m2!1d-5.6044497!2d36.0143209!3e0?hl=ru
# Тарифа => Лиссабон => Порту, Португалия => Париж, Франция (2561 км)

if distance_km_sum >= 84.8:
    travel_city = "Житомир => Новоград"
if distance_km_sum >= 1724:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk"
    travel_next_city_distance_km = round(1987 - (distance_km_sum), 2)
    travel_next_city = "Венеция в Италии"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 1987:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция"
    travel_next_city_distance_km = round(2553 - (distance_km_sum), 2)
    travel_next_city = "Ницца во Франции"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 2553:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция => Ницца"
    travel_next_city_distance_km = round(3216 - (distance_km_sum), 2)
    travel_next_city = "Тарифа в Испания"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 3216:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция => Ницца => Барселона"
    travel_next_city_distance_km = round(4337 - (distance_km_sum), 2)
    travel_next_city = "Барселона"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 7391:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция => Апеннинский полуостров => Ницца => Барселона => Тарифа, Испания"
    travel_next_city_distance_km = round(8370 - (distance_km_sum), 2)
    travel_next_city = "Париж во Франции"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 8370:
    travel_city = "Житомир => Ровно => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция => Апеннинский полуостров => Ницца => Барселона => Тарифа, Испания => Порту, Португалия"
    travel_next_city_distance_km = round(12356 - (distance_km_sum), 2)
    travel_next_city = "Париж во Франции"
    travel_predict_next_city_days = math.ceil(travel_next_city_distance_km / distance_km_average)
if distance_km_sum >= 12356:
    travel_city = "Житомир => Львов => Краков => Dolny Kubin => Братислава => Грац (Австрия) => Njivice, Krk => Венеция => Апеннинский полуостров => Ницца => Барселона => Тарифа => Париж"


# Вычисление количества шагов до следующего города
travel_steps_next_city = round(travel_next_city_distance_km / STEP_ONE_DISTANCE)

# Вычисление окончания в слове "День" для прогнозиварония времени прибытья в следующий город.
if travel_predict_next_city_days == 1:
    travel_predict_word_ending_days = "день"
elif travel_predict_next_city_days < 5:
    travel_predict_word_ending_days = "дня"
else:
    travel_predict_word_ending_days = "дней"

############################################################
# Графики и гистограммы
############################################################

def steps_graph():
    # Построение графика по количеству шагов.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(STEPS, linewidth = 1, c=(0, 0.7, 1), label='Шагов в день')
    ax.plot(days_median_steps, linewidth = 1.3, c=(0.8, 0, 0.2), label='Медианная средняя')
    ax.plot(days_average_30_graph, linewidth = 1.3, c=(0.6, 0, 0.5), label='Среднее за 30 дней')
    ax.plot(days_average_180_graph, linewidth = 1.3, c=(0.2, 0.2, 1), label='Среднее за 180 дней')
    ax.plot(days_average_360_graph, linewidth = 1.3, c=(0, 0.8, 0.8), label='Среднее за 360 дней')
    ax.plot(days_average_steps, linewidth = 1.3, c=('black'), label='Среднее за все время')
    ax.legend()

    # Назначение заголовка диаграмы и меток осей.
    ax.set_title("График количества шагов", fontsize = 12)
    ax.set_xlabel("День", fontsize = 10)
    ax.set_ylabel("Количество шагов за один день", fontsize = 10)

    # Назначение размера шрифта делений на осях
    ax.tick_params(axis='both', labelsize = 10)
    ax.set_facecolor('seashell')

    plt.show()


def bar_days_week_average():
    # Гистограмма которая показывает статистику по шагам на протяжении недели.
    plt.style.use('seaborn-pastel')
    fig, ax = plt.subplots()

    x = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение")
    y_day_average = (day_monday_average, day_tuesday_average, day_wednesday_average, day_tuesday_average, day_friday_average, day_saturday_average, day_sunday_average)
    y_day_median = (day_monday_median, day_tuesday_median, day_wednesday_median, day_thursday_median, day_friday_median, day_saturday_median, day_sunday_median)
    y_day_max = (max(day_monday), max(day_tuesday), max(day_wednesday), max(day_thursday), max(day_friday), max(day_saturday), max(day_sunday))
    y_day_min = (min(day_monday), min(day_tuesday), min(day_wednesday), min(day_thursday), min(day_friday), min(day_saturday), min(day_sunday))

    ax.bar(x, y_day_max, color=(0.5, 0.5, 1), edgecolor='black', linewidth=1, label='Max')
    ax.bar(x, y_day_median, color=(0, 0.7, 0.3), edgecolor='black', linewidth=1, label='Median')
    ax.bar(x, y_day_average, color=(0.3, 0.9, 0.4), edgecolor='black', linewidth=1, label='Average')
    ax.bar(x, y_day_min, color=(0.9, 0.3, 0.5), edgecolor='black', linewidth=1, label='Min')

    ax.set_title("График количества шагов по дням недели", fontsize=12)
    ax.set_xlabel("Дни недели", fontsize=10)
    ax.set_ylabel("Количество шагов за один день", fontsize=10)

    ax.set_facecolor('seashell')
    plt.legend()

    plt.show()


def bar_hours_stat_steps():
    # Гистограма для отображения кол-ва шагов на протяжении дня.
    plt.style.use('seaborn-pastel')
    fig, ax = plt.subplots(figsize=(14,6))

    x_axis = ('00:00-00:59', '01:00-01:59', '02:00-02:59', '03:00-03:59', '04:00-04:59', '05:00-05.59', '06:00-06.59',
              '07:00-07.59', '08:00-08.59', '09:00-09.59', '10:00-10.59', '11:00-11.59', '12:00-12.59', '13:00-13.59',
              '14:00-14.59', '15:00-15.59', '16:00-16.59', '17:00-17.59', '18:00-18.59', '19:00-19.59', '20:00-20.59',
              '21:00-21.59', '22:00-2.59', '23:00-23.59', )
    y_hour_steps = (sum(hour_stat_steps['00:00-00:59']), sum(hour_stat_steps['01:00-01:59']), sum(hour_stat_steps['02:00-02:59']),
                    sum(hour_stat_steps['03:00-03:59']), sum(hour_stat_steps['04:00-04:59']), sum(hour_stat_steps['05:00-05:59']),
                    sum(hour_stat_steps['06:00-06:59']), sum(hour_stat_steps['07:00-07:59']), sum(hour_stat_steps['08:00-08:59']),
                    sum(hour_stat_steps['09:00-09:59']), sum(hour_stat_steps['10:00-10:59']), sum(hour_stat_steps['11:00-11:59']),
                    sum(hour_stat_steps['12:00-12:59']), sum(hour_stat_steps['13:00-13:59']), sum(hour_stat_steps['14:00-14:59']),
                    sum(hour_stat_steps['15:00-15:59']), sum(hour_stat_steps['16:00-16:59']), sum(hour_stat_steps['17:00-17:59']),
                    sum(hour_stat_steps['18:00-18:59']), sum(hour_stat_steps['19:00-19:59']), sum(hour_stat_steps['20:00-20:59']),
                    sum(hour_stat_steps['21:00-21:59']), sum(hour_stat_steps['22:00-22:59']), sum(hour_stat_steps['23:00-23:59']), )

    ax.bar(x_axis, y_hour_steps, color=(0.5, 0.5, 1), edgecolor='black', linewidth=1, label='Max')

    ax.set_title("График количества шагов по часам на протяжении дня", fontsize=12)
    ax.set_xlabel("Время дня", fontsize=10)
    ax.set_ylabel("Количество шагов за один час", fontsize=10)

    for label in (ax.get_xticklabels()):
        label.set_fontsize(5)

    ax.set_facecolor('seashell')
    plt.show()

############################################
# Вывод информции на экран
############################################
print("🏃 🚗")
print(Fore.CYAN + "===============================================" + Style.RESET_ALL + Fore.MAGENTA + "===" + Style.RESET_ALL)

print(f"Всего за {Fore.MAGENTA}{len(STEPS):,.0f}{Style.RESET_ALL} дня пройдено - {Fore.GREEN}{steps_sum:,.0f}{Style.RESET_ALL} шагов. (Вчера: + {Fore.LIGHTGREEN_EX}{(STEPS[-1]):,.0f}{Style.RESET_ALL}) ({challenge_average}{str(percentage_difference_round)} %{Style.RESET_ALL}) {challenge_row} :: (Min: {Fore.RED}{steps_min:,.0f}{Style.RESET_ALL} / Max: {Fore.GREEN}{steps_max:,.0f}{Style.RESET_ALL}).")

print(f"В среднем, в день: {Fore.LIGHTGREEN_EX}{steps_average:,.0f}{Style.RESET_ALL} шагов. (Запас: {stock_steps_to_10k_per_day:,.0f} шага).")
print((f"Средняя медианная: {Fore.LIGHTGREEN_EX}{statistics.median(STEPS):,.0f}{Style.RESET_ALL} шагов в день."))

print(f"\nОбщее расстояние: {Fore.LIGHTBLUE_EX}{distance_km_sum:,.0f}{Style.RESET_ALL} км (+ {str(distance_day_km)} км)")
print(f"В среднем: {Fore.LIGHTBLUE_EX}{str(distance_km_average)}{Style.RESET_ALL} км в день.")

print(f"\nСреднее кол-во шагов за последние: \n\t-- 30 дней: {Fore.GREEN}{steps_average_last_30_days:,.0f}{Style.RESET_ALL} шагов; "
      f"\n\t-- 90 дней: {Fore.GREEN}{steps_average_last_90_days:,.0f}{Style.RESET_ALL} шагов; "
      f"\n\t-- 180 дней: {Fore.GREEN}{steps_average_last_180_days:,.0f}{Style.RESET_ALL} шагов; "
      f"\n\t-- 360 дней: {Fore.GREEN}{steps_average_last_360_days:,.0f}{Style.RESET_ALL} шагов;")

print(f"\nМаршрут прошел по городам: {travel_city}")
print(f"До города {Fore.LIGHTGREEN_EX}{travel_next_city}{Style.RESET_ALL} осталось: {Fore.CYAN}{travel_next_city_distance_km:,.0f}{Style.RESET_ALL} км, или {Fore.GREEN}{travel_steps_next_city:,.0f}{Style.RESET_ALL} шага. Прогнозированное, прибытие через {Fore.CYAN}{travel_predict_next_city_days}{Style.RESET_ALL} {travel_predict_word_ending_days}.")

print(f"\nНа ходьбу затрачено: {Fore.CYAN}{kcal_sum:,.0f}{Style.RESET_ALL} kcal, (вчера {kcal_last_day} kcal).")
print(f"Эквивалент: {Fore.CYAN}{kcal_to_fat}{Style.RESET_ALL} кг жира, {Fore.CYAN}{kwt_sum}{Style.RESET_ALL} кВт, {Fore.CYAN}{petrol_economy_liter}{Style.RESET_ALL} л бензина, или {Fore.CYAN}{big_mac_used}{Style.RESET_ALL} Big Mac.")

print(f"\nЧелендж выполняется последние {Fore.CYAN}{challenge_last_days_go_on}{Style.RESET_ALL} дней. За вчера пройдено {challenge_last_day} 10к шагов.")
print(f"По статистике: {Fore.CYAN}{len(steps_more_10k):,.0f}{Style.RESET_ALL} из {Fore.CYAN}{len(STEPS):,.0f}{Style.RESET_ALL} дней ({Fore.CYAN}{(round(percent_steps_more_10k, 2))}{Style.RESET_ALL} %), за которые пройдено более 10к шагов, на протяжении дня.")

# Отображение среднего количества шагов в день в разные дни недели.
print(f"\n--- Статистика по среднему и медианному кол-ву шагов, в разные дни недели: ---")
for day, value in avarage_steps_days_of_week.items():
    print(f"\t- {day.title()} - Среднее значение: {Fore.CYAN}{value['average_day']:,.0f}{Style.RESET_ALL}; медианное: {Fore.GREEN}{value['median_day']:,.0f}{Style.RESET_ALL} :: Min: {Fore.RED}{value['min_day']:,.0f}{Style.RESET_ALL} / Max: {Fore.GREEN}{value['max_day']:,.0f}{Style.RESET_ALL}.")

# Отображения статистики по кол-ву шагов в конкретный час дня.
print(f"\n--- Статистика по кол-ву шагов по часам на протяжении дня: ---")
for day_time, value in hour_stat_steps.items():
    print(f"\t- {day_time} - Пройдено: {Fore.GREEN}{sum(value):,.0f}{Style.RESET_ALL} шагов. ({Fore.LIGHTBLUE_EX}{(sum(value) / hour_stat_steps_sum) * 100:,.2f}{Style.RESET_ALL} %)")


# Вывод построения графиков.
#steps_graph()              # Построение графика по количеству шагов.
#bar_days_week_average()    # Гистограмма которая показывает статистику по шагам на протяжении недели.
bar_hours_stat_steps()      # Гистограмма для отображения статистики по шагам в разные часы, на протяжении дня.


print(Fore.LIGHTCYAN_EX + "\n==============================================="+ Style.RESET_ALL)
print(f"Скрипт выполнен за: {time.time() - start_time:,.3f} секунды.")

