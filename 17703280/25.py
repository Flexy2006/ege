import sys
sys.setrecursionlimit(10**8)
def f(x):
    if x < 3:
        return x
    if x >= 3:
        return (x - 1)*f(x-2)
print((f(2024) - f(2022)) // f(2020))