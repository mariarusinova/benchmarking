from utilites import load, dump

import numpy as np
import scipy as sp

_in0 = load('jsondb/нормированные данные.json')
_in1 = load('jsondb/вес показателей.json')

регионы = list(_in0.keys())
показатели = list(_in0[регионы[0]].keys())
эталонный_регион = "Пермский край"

rez = {}
for регион in регионы:
    _sum = 0
    for показатель in показатели:
        try:
            вес = _in1[показатель]
            показатель_эт_региона = _in0[эталонный_регион][показатель]
            показатель_региона = _in0[регион][показатель]
            x = вес * ((показатель_эт_региона - показатель_региона) ** 2)
            _sum += x
        except KeyError:
            pass
    rez.update({регион: _sum})

dump(rez, 'jsondb/индекс структурного расстояния.json')