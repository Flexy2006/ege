from sys import *
setrecursionlimit(1000000)
def f(x):
    if x < 10:
        return x
    if x >= 10:
        return f(x % 10) + f(x // 10)
b = 0
for i in range(2**63):
    if f(i) == 159:
        b += 1
print(b)