import sys
sys.setrecursionlimit(10**8)
q = 0
def f(x):
    if x == 1:
        return 1
    if x > 1:
        return x*f(x-1)
print(f(2023)/f(2020))