from utilites import load, dump

_in = load('jsondb/секторная структура.json')

def stage_2(_in):
    rez = {}
    for reg in _in.keys():
        data = {}
        for _pok in _in[reg].keys():
            A = _in[reg][_pok]['ВРП'] #ВРП по основным видам экономической деятельности
            B = _in[reg][_pok]['ЧИСЛ'] #Среднегодовая численность занятых по основным видам экономической деятельности
            X = A / (B * 1000)  #Расчет производительности труда по основным видам экономической деятельности

            data.update({_pok:X})

        rez.update({reg:data})
    return rez

if __name__ == '__main__':
    _in = load('jsondb/секторная структура.json')
    _out = stage_2(_in)
    dump(_out, 'jsondb/Производительность труда.json')
