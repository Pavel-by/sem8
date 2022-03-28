from tkinter import ROUND
import numpy as np
from math import *
import matplotlib.pyplot as plt

ROUND_ACC = 5

def m_round(a):
    return round(a, ROUND_ACC)


def m_np_round(a):
    return np.round(a, ROUND_ACC)


def make_spaced(_data):
    _n = len(_data)
    _k = 1 + 3.322 * log10(_n)
    _max = max(_data)
    _min = min(_data)
    _h = (_max - _min) / _k
    print("Интервальный ряд: k={} (формула Спенсера), h={}={} (шаг)".format(_k, _h, round(_h)))
    _h = round(_h)
    _from, _upto = _min, _min + _h
    _spaces = []
    _abs_freqs = []
    _rel_freqs = []
    _space_count = 0
    for i in _data:
        if i >= _upto:
            _spaces.append([_from, _upto])
            _abs_freqs.append(_space_count)
            _rel_freqs.append(_space_count / _n)
            _from = _upto
            _upto = _from + _h
            _space_count = 1
        else:
            _space_count += 1

    _spaces.append([_from, _upto])
    _abs_freqs.append(_space_count)
    _rel_freqs.append(_space_count / _n)
    return np.array(_spaces), np.array(_abs_freqs), np.array(_rel_freqs), _h


source_dataset = np.genfromtxt('dataset.csv', delimiter=',')
source_len = len(source_dataset)
data = source_dataset[:,0].astype(int)

print("Исходный ряд:\n", data)

data = np.sort(data)
ranked_data = np.array(data)
print("Ранжированный ряд:\n", ranked_data)

uniq, abs_freqs = np.unique(data, return_counts=True)
abs_freqs_table = np.array([tuple([uniq[i], abs_freqs[i]]) for i in range(len(uniq))], dtype='i, i')
print("Вариационный ряд - абсолютные частоты:\n", abs_freqs_table)

rel_freqs = (abs_freqs / source_len).astype(float)
rel_freqs_table = np.array([tuple([uniq[i], rel_freqs[i]]) for i in range(len(uniq))], dtype='i, f')
print("Вариационный ряд - относительные частоты:\n", rel_freqs_table)

spaces, spaces_abs_freq, spaces_rel_freq, h = make_spaced(data)
print("Интервальный ряд:\n{}\t{}\t{}".format("Интервал", "Абс. частоты", "Отн. частоты"))
for i in range(len(spaces)):
    print("[{}, {})\t{}\t\t{}".format(spaces[i][0], spaces[i][1], spaces_abs_freq[i], m_round(spaces_rel_freq[i])))

spaces_median = np.median(spaces, axis=1)
spaces_median_str = [str(i) for i in spaces_median]

plt.plot(spaces_median, spaces_abs_freq)
plt.title("Полигон для абсолютной частоты")
plt.xlabel("Средние значения")
plt.ylabel("Частоты")
plt.grid()
plt.show()

plt.plot(spaces_median, spaces_rel_freq)
plt.title("Полигон для относительной частоты")
plt.xlabel("Средние значения")
plt.ylabel("Частоты")
plt.grid()
plt.show()

plt.bar(spaces_median_str, spaces_abs_freq, width=0.7)
plt.title("Гистограмма для абсолютной частоты")
plt.xlabel("Средние значения")
plt.ylabel("Частоты")
plt.show()

plt.bar(spaces_median_str, spaces_rel_freq)
plt.title("Гистограмма для относительной частоты")
plt.xlabel("Средние значения")
plt.ylabel("Частоты")
plt.show()

space_width = spaces_median[1] - spaces_median[0]
spaces_median_t = np.array([spaces_median[0] - space_width, *spaces_median, spaces_median[-1] + space_width])

spaces_distrib = [0, 0]
t = 0
for i in spaces_abs_freq:
    t += i
    spaces_distrib.append(t)

plt.step(spaces_median_t, spaces_distrib)
plt.title("Эмпирическая ф.р. для абсолютной частоты")
plt.xlabel("Средние значения")
plt.ylabel("Абсолютная частота")
plt.xticks(spaces_median_t)
plt.grid()
plt.show()

spaces_distrib = [0, 0]
t = 0
for i in spaces_abs_freq:
    t += i / np.sum(spaces_abs_freq)
    spaces_distrib.append(t)

plt.step(spaces_median_t, spaces_distrib)
plt.title("Эмпирическая ф.р. для относительной частоты")
plt.xlabel("Средние значения")
plt.ylabel("Относительная частота")
plt.xticks(spaces_median_t)
plt.grid()
plt.show()