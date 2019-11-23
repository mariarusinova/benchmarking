from utilites import load, dump

def stage_3(_in1, _in2, _in3):
    for reg in _in2.keys():
        x = _in1[reg]
        _in2[reg]["Количество людей с высшим образованием из числа занятых и безработных (тыс.человек)"] = x
        for k in _in3[reg].keys():
            _in2[reg][k] = _in3[reg][k]
    return _in2

if __name__ == '__main__':
    _in1 = load('jsondb/Количество людей с высшим образованием из числа занятых и безработных.json')
    _in2 = load('jsondb/исходные данные.json')
    _in3 = load('jsondb/Производительность труда.json')
    _out = stage_3(_in1, _in2, _in3)  
    dump(_out, 'jsondb/исходные данные (ред).json')
