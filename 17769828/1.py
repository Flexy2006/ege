from itertools import *
t = '13 14 17 23 25 26 31 32 34 35 36 37 41 43 52 53 62 63 67 71 73 76'
g = 'CF FC DF FD DC CD DG GD GF FG GA AG FA AF AB BA BF FB FE EF BE EB'
s = set(g.replace(" ", ""))
for p in permutations(s):
    nt = t
    for i, v in enumerate(p):
        nt = nt.replace(str(i+1), v)
        if set(g.split()) == set(nt.split()):
            print(p)