from xlrd import open_workbook,cellname
from pprint import pprint
from utilites import dump

wb = open_workbook('xlsxdb/data.xlsx')

ws = wb.sheet_by_name('исходные данные')

categories = []
for y in range(3):
    row = []
    for x in range(ws.ncols):
        row += [ws.cell(y, x).value.replace('\n', ' ').strip()]
    categories += [row]
    
rez = {}
subcat, cat = '', ''
for n in range(len(categories[2])):
    subsubcat = categories[2][n]
    if subsubcat:
        if categories[1][n]:
            subcat = categories[1][n]
        if categories[0][n]:
            cat = categories[0][n]
        rez.update({subsubcat:(subcat, cat)})

dump(rez,'jsondb/categories.json')

rez = {}
for row in range(3, 88):
    data = {}
    for col in range(1, ws.ncols):
        reg = ws.cell(row, 0).value.replace('\n', ' ').replace(' – ',' - ').strip()
        subsubcat = ws.cell(2, col).value.replace('\n', ' ').strip()
        v = ws.cell(row, col).value
        data.update({subsubcat:v})
    rez.update({reg:data})
        
dump(rez,'jsondb/исходные данные.json')


