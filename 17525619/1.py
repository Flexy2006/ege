from itertools import *
t = "12 14 16 21 23 24 25 27 32 35 37 41 42 46 47 52 53 61 64 67 72 73 74 76"
g = 'АБ БА БГ ГБ АГ ГА АВ ВА ВГ ГВ ВД ДВ ВЕ ЕВ ДЕ ЕД ЕК КЕ ДК КД ГК КГ ГД ДГ'
s = set(g.replace(' ', ''))
for p in permutations(s):
    nt = t
    for i,v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)