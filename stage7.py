from utilites import load, dump

import numpy as np
import scipy as sp

_in = load('трансформированные данные.json')

регионы = list(_in.keys())
показатели = list(_in[регионы[0]].keys())

data = np.zeros([len(показатели), len(регионы)])

x = 0
for регион in регионы:
    y = 0
    for показатель in показатели:
        data[y,x] = _in[регион][показатель]
        y += 1
    x += 1
    
rez = {}
i = 0
for показатель in показатели:
    rez.update(
        {показатель:
            {'avg':np.average(data[i]),
             'std':np.std(data[i])}
        }
    )
    i += 1

dump(rez, 'avg_std.json')