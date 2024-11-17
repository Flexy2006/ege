from itertools import *

def f1(x, y, z, w):
        return ((x <= (z <= w)) and (z <= (y != w)))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tab = [(a1, 0, 0, 0), (a2, a3, 0, 0), (a4, a5, 0, a6)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)#zyxw