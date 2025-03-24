from itertools import *
t = "12 14 18 21 23 32 36 38 41 47 56 57 58 63 65 68 74 75 81 83 85 86"
g = "АБ БА АГ ГА БГ ГБ БД ДБ ГД ДГ АВ ВА ЕВ ВЕ ЕГ ГЕ ДК КД КЛ ЛК ЕЛ ЛЕ"

s = set(g.replace(' ', ''))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(*p)