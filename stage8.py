from utilites import load, dump

import numpy as np
import scipy as sp

_in1 = load('jsondb/трансформированные данные.json')
_in2 = load('jsondb/avg_std.json')

регионы = list(_in1.keys())
показатели = list(_in1[регионы[0]].keys())

data = np.zeros([len(показатели), len(регионы)])

rez = {}
for регион in регионы:
    poka = {}
    for показатель in показатели:
        try:
            показатель.index('%')
        except ValueError:
            x = (_in1[регион][показатель] - _in2[показатель]['avg']) / _in2[показатель]['std']
            poka.update({показатель: x})
    rez.update({регион: poka})

dump(rez, 'jsondb/нормированные данные.json')