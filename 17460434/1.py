from itertools import *
t = "15 16 26 27 29 35 37 38 48 49 51 53 58 61 62 67 72 73 76 83 84 85 92 94"
g = "АБ БА БВ ВБ АГ ГА АЕ ЕА ГЕ ЕГ ГД ДГ ВД ДВ ВК КВ ДК КД ЕЖ ЖЕ ЖИ ИЖ ИК КИ"

s = set(g.replace(' ',''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)