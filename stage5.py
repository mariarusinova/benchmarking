from utilites import load, dump

import numpy as np
import scipy as sp

_in = load('исходные данные (ред).json')

регионы = list(_in.keys())
показатели = list(_in[регионы[0]].keys())

data = np.zeros([len(регионы), len(показатели)])

x = 0
for регион in регионы:
    y = 0
    for показатель in показатели:
        data[x,y] = _in[регион][показатель]
        y += 1
    x += 1

скос = sp.stats.skew(data, 0, 0)

rez = {}
i = 0
for показатель in показатели:
    rez.update({показатель:скос[i]})
    i += 1

dump(rez, 'скос.json')