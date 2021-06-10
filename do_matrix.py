import re
import numpy as np

from utilites import load, dump
from xlwt import Workbook

matrix = load('jsondb/матрица для экселя.json')

wb = Workbook()

ws = wb.add_sheet('1')

i = 1
for region in matrix:
    ws.write(0, i, region)
    ws.write(i, 0, region)
    i += 1
    
j = 1
for region_a in matrix:
    i = 1
    for region_b in matrix:
        ws.write(i, j, matrix[region_a][region_b])
        i += 1
    j += 1

wb.save('/tmp/out.xls')