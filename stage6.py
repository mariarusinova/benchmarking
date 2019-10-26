from utilites import load, dump

import numpy as np
import scipy as sp

_in = load('исходные данные (ред).json')
скос0 = load('скос.json')

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


for i_показатель in range(len(показатели)):
    скос = скос0[показатели[i_показатель]]
    if abs(скос) > 0.5:
        скосы = []
        for n in [2,3,4]:
            скос_i = sp.stats.skew(data[i_показатель] ** (1/n), 0, 0)
            скосы += [(скос_i, n)]
        
        n = min(скосы)[1]
        data[i_показатель] = data[i_показатель] ** (1/n)
        
скос = sp.stats.skew(data, 1, 0)

rez = {}
i = 0
for показатель in показатели:
    rez.update({показатель:скос[i]})
    i += 1

dump(rez, 'скос new.json')

rez = {}
x = 0
for регион in регионы:
    y = 0
    pok = {}
    for показатель in показатели:
        pok.update({показатель:data[y,x]})
        y += 1
    rez.update({регион:pok})
    x += 1

dump(rez, 'трансформированные данные.json')

