#72559
from itertools import *
t="15 17 18 24 27 28 34 35 37 42 43 47 51 53 56 65 68 71 72 73 74 81 82 86"
g="АБ БА АГ ГА БГ ГБ АЕ ЕА ГЕ ЕГ ЕЖ ЖЕ ДЖ ЖД ВД ДВ БВ ВБ ЖИ ИЖ ВИ ИВ ГД ДГ"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)