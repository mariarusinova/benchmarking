from utilites import load, dump

_in1 = load('Количество людей с высшим образованием из числа занятых и безработных.json')
_in2 = load('исходные данные.json')
_in3 = load('Производительность труда.json')

for reg in _in2.keys():
    x = _in1[reg]
    _in2[reg]["Количество людей с высшим образованием из числа занятых и безработных (тыс.человек)"] = x
    for k in _in3[reg].keys():
        _in2[reg][k] = _in3[reg][k]
        
dump(_in2, 'исходные данные (ред).json')