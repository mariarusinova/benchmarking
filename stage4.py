from utilites import load, dump

_categories = load('jsondb/categories.json')

критерии = set([ _categories[k][1] for k in _categories.keys() ])

число_критериев = len(критерии)

rez = {}
for критерий in критерии:
    rez.update({критерий:0})

for показатель in _categories.keys():
    критерий_показателя = _categories[показатель][1]
    фактор_показателя = _categories[показатель][0]
    
    rez[критерий_показателя] += 1

M = {}
for показатель in _categories.keys():
    критерий_показателя = _categories[показатель][1]
    число_показателей = rez[критерий_показателя]
    m = 1/число_критериев/число_показателей
    M.update({показатель:m})

dump(M,'jsondb/вес показателей.json')