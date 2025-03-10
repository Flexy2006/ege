from itertools import *

def f(x, y, z, w):
        return ((not(x) or z) == (y and not(w)))<=(z and y)


for a1, a2, a3,a4,a5 in product([0, 1], repeat=5):
    tab = [(a1,1,1,1),(a2,a3,1,1),(a3,a4,1,a5)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0,0,0]:
                 print(*p)