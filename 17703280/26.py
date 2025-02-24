import sys
sys.setrecursionlimit(10**8)
def f(x):
    if x == 1:
        return x
    if x > 1:
        return x - 1 + f(x-1)
print(f(2024) - f(2022))