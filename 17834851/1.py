from itertools import *
t = "12 14 15 16 17 21 24 26 35 41 42 51 53 56 57 61 62 65 71 75"
g = "АБ БА БВ ВБ ВЖ ЖВ БЖ ЖБ БЕ ЕБ ЕЖ ЖЕ ГЖ ЖГ ГД ДГ ДЖ ЖД ЕД ДЕ"

s = set(g.replace(' ',''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)