from itertools import *
t = '13 17 25 27 31 34 37 43 47 52 56 65 67 71 72 73 74 76'
g = 'AC CA AG GA AD DA CD DC GD DG BD DB DE ED BF FB EF FE'
s = set(g.replace(" ", ""))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)