from xlrd import open_workbook,cellname
from utilites import load, dump

wb = open_workbook('xlsxdb/data.xlsx')

ws = wb.sheet_by_name('Расчет кол-ва людей с ВО')

rez = {}
for row in range(1,86):
    reg = ws.cell(row, 0).value.replace('\n', ' ').strip()
    data = {}
    for col in range(1, 5):
        cat = ws.cell(0, col).value.replace('\n', ' ').strip()
        v = ws.cell(row, col).value
        data.update({cat:v})
    rez.update({reg:data})

dump(rez,'jsondb/количество людей с ВО.json')
