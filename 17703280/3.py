from itertools import *
t = '13 18 25 28 31 34 36 43 46 52 57 63 64 67 75 76 78 81 82 87'
g = 'DE ED EB BE DB BD AE EA AH HA HC CH CF FC FG GF HG GH BG GB'
s = set(g.replace(" ", ""))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)