import squarify 

from xlrd import open_workbook
from PIL import Image

import matplotlib.pyplot as plt
import numpy as np

wb = open_workbook('xlsxdb/treecharts.src.xls')
ws = wb.sheets()[0]

industries = [ ws.cell(0,i).value.strip() for i in range(13) ]
regions = [ ws.cell(i, 13).value.strip() for i in range(1, 86) ]

ind_colors = {}

for ind in industries:
    c = tuple(np.array(Image.open('icons/%s.png' % ind).getpixel((0,0))) / 255)
    ind_colors.update({ind:c})
    
j = 1
for reg in regions:
    labels = []
    sizes  = []
    colors = []
    i = 0
    for ind in industries:
        colors += [ind_colors[ind]]
        sizes  += [1/1000000 if ws.cell(j, i).value == 0 else ws.cell(j, i).value]
        i += 1
    labels = [ "%s %%" % round(x * 100) for x in sizes ]
    
    j += 1
    plt.figure(figsize=(16,9), dpi=75)
    squarify.plot(sizes=sizes, label=labels, color=colors, text_kwargs={'fontsize':18})
    plt.title(reg)
    plt.axis('off')
    plt.savefig("/tmp/%s.png" % reg)
    plt.close()