from itertools import *
t = '13 16 24 25 26 27 31 37 42 45 47 52 54 56 61 62 65 72 73 74'
g = 'AE EA EG GE AG GA DE ED AD DA BG GB AB BA DC CD CF FC FB BF'
s = set(g.replace(' ', ''))
for p in permutations(s):
    nt = t
    for i,v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(*p)