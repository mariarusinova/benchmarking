from xlrd import open_workbook,cellname
from utilites import load, dump

wb = open_workbook('data.xlsx')

ws = wb.sheet_by_name('Расчет производительности')

rez = {}
for row in range(3,88):
    reg = ws.cell(row, 0).value.replace('\n', ' ').strip()
    data = {}
    for col in range(1, 14):
        key1 = ws.cell(2, col).value.replace('\n', ' ').strip()
        v1 = ws.cell(row, col).value
        v2 = ws.cell(row, col+14).value
        data.update({key1:{'ЧИСЛ':v1, 'ВРП':v2}})
    rez.update({reg:data})

dump(rez,'секторная структура.json')

#        cat = ws.cell(0, col).value.replace('\n', ' ').strip()
#        v = ws.cell(row, col).value
#        data.update({cat:v})
#    rez.update({reg:data})

#
