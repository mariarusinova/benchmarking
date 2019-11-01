from utilites import load, dump

_in = load('jsondb/секторная структура.json')

rez = {}
for reg in _in.keys():
    data = {}
    for _pok in _in[reg].keys():
        A = _in[reg][_pok]['ВРП']
        B = _in[reg][_pok]['ЧИСЛ']
        X = A / (B * 1000)
        
        data.update({_pok:X})

    rez.update({reg:data})

dump(rez, 'jsondb/Производительность труда.json')
