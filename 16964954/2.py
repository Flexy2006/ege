#72559
from itertools import *
t="16 17 25 26 27 34 35 36 43 45 52 53 54 61 62 63 71 72"
g="АБ БА АВ ВА БВ ВБ ВД ДВ БГ ГБ ГД ДГ ГЕ ЕГ ЕЗ ЗЕ ДЗ ЗД"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)