from itertools import *

def f1(x, y, z, w):
        return ((w <= y) <= x) or not(z)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tab = [(a1, a2, 1, a3), (a4, 0, a5, a6), (a7, 1, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f1(**dict(zip(p, r))) for r in tab] == [0, 0, 0]:
                print(p)#zyxw