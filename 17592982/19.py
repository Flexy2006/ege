import math
import sys
sys.setrecursionlimit(10**8)
q = 0
def f(x):
    if x == 1:
        return 1
    if x == 2:
        return 2
    if x > 2 and x % 2 == 0:
        return math.trunc((4*x - f(x - 3)) / 8)
    if x > 2 and x % 2 != 0:
        return math.trunc((4*x - f(x-1) + f(x-2)) / 8)
print(f(52)-f(38))