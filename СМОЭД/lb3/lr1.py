from tkinter import ROUND
import numpy as np
from math import *

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

data = np.sort(data)
ranked_data = np.array(data)

uniq, abs_freqs = np.unique(data, return_counts=True)
abs_freqs_table = np.array([tuple([uniq[i], abs_freqs[i]]) for i in range(len(uniq))], dtype='i, i')

rel_freqs = (abs_freqs / source_len).astype(float)
rel_freqs_table = np.array([tuple([uniq[i], rel_freqs[i]]) for i in range(len(uniq))], dtype='i, f')

spaces, spaces_abs_freq, spaces_rel_freq, h = make_spaced(data)