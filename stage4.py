from utilites import load, dump

def stage_4(_categories):
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
    return M

if __name__ == '__main__':
    _categories = load('jsondb/categories.json')
    M = stage_4(_categories)
    dump(M,'jsondb/вес показателей.json')
