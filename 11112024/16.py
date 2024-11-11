import sys
sys.setrecursionlimit(10000)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) + n - 2
print(f(2023) - f(2021))