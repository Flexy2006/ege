#72559
from itertools import *
t="12 14 15 19 21 26 34 35 37 39 41 43 48 51 53 56 62 65 73 78 84 87 91 93"
g="АБ БА БВ ВБ АГ ГА ВЕ ЕВ ГВ ВГ ГД ДГ ДЕ ЕД ГЖ ЖГ ЖЕ ЕЖ ЕК КЕ ЖИ ИЖ ИК КИ"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)