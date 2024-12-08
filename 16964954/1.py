#72559
from itertools import *
t="14 15 17 24 26 35 36 37 41 42 51 53 56 62 63 65 71 73"
g="AB BA BD DB GD DG FD DF FG GF FE EF EC CE CA AC CG GC"

s=set(g.replace(' ',''))
for p in permutations(s):
    nt=t
    for i,v in enumerate(p):
        nt=nt.replace(str(i+1),v)
    if set(g.split())==set(nt.split()):
        print (p)