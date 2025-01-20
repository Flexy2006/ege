from itertools import *
t = "12 15 16 21 25 29 34 36 38 43 46 47 51 52 57 61 63 64 74 75 83 89 92 98"
g = "АБ БА БВ ВБ ВГ ГВ АЖ ЖА ГК КГ ЖИ ИЖ ИК КИ АД ДА ЖД ДЖ ЕД ДЕ ЕГ ГЕ ЕК КЕ"

s = set(g.replace(' ',''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)