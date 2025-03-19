import sys
sys.setrecursionlimit(10**8)
q = 0
def f(x):
    if x < 7:
        return 7
    if x >= 7:
        return 2*x+f(x-1)
print(f(2024)-f(2022))