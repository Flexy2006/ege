#72559
from itertools import *
t="16 19 23 25 27 32 34 39 43 46 47 52 58 61 64 68 69 72 74 78 85 86 87 91 93 96"
g="АБ БА БВ ВБ АВ ВА АИ ИА ИК КИ ВК КВ АГ ГА ИЕ ЕИ ЖК КЖ ГД ДГ ДЖ ЖД ЖЕ ЕЖ ГЕ ЕГ"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)