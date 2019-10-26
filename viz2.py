from utilites import load, dump

эталонный_регион = "Пермский край"

dists = load('индекс структурного расстояния.json')

graph = "<table>\n"
for регионA in dists.keys():
    for регионB in dists.keys():
    if регион != эталонный_регион:
        _len = round(dists[регион]*10)
        _lab = round(dists[регион]*10)
        graph += '\t"%s" -> "%s" [len=%s _minlen=%s label=%s]\n' % (эталонный_регион, регион, _len, _len, _lab)

graph += "</table>\n"
    
open('/tmp/test', 'w').write(graph)