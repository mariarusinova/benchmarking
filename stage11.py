import xlwt
from utilites import load

_in1 = load('jsondb/матрица структурных расстояний.json')
_in2 = load('jsondb/regions.json')

for region in _in2:
    code = _in2[region]['code']
    try:
        try:
            distances = _in1[region]
        except KeyError:
            try:
                distances = _in1[_in2[region]['emissname']]
            except KeyError:
                try:
                    if 'Москва' in region:
                        distances = _in1['г. Москва']
                    elif 'Петербург' in region:
                        distances = _in1['г. Санкт-Петербург']
                    elif 'Осетия' in region:
                        distances = _in1['Республика Северная Осетия-Алания']
                except KeyError:
                    pass
        assert distances
        wb = xlwt.Workbook()
        ws = wb.add_sheet(region[:20])
        ws.write(0,0,"N п/п")	
        ws.write(0,1,"Регион")
        ws.write(0,2,"Индекс")
        i = 1
        for k, v in distances.items():
            ws.write(i, 0, i)
            ws.write(i, 1, k)
            ws.write(i, 2, v)
            i += 1
        wb.save('xlsxdb/%s.xlsx' % code)
    except AssertionError:
        print(region, _in2[region]['emissname'])

