from itertools import *
t = '12 18 21 24 26 27 35 39 42 49 53 57 62 68 69 72 75 79 81 86 93 94 96 97'
g = 'АБ БА БВ ВБ АГ ГА ГВ ВГ ГД ДГ ДЕ ЕД ЕВ ВЕ ГЖ ЖГ ЖЕ ЕЖ ЕК КЕ ЖИ ИЖ ИК КИ'
s = set(g.replace(" ", ""))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)