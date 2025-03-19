import sys
sys.setrecursionlimit(10**8)
q = 0
def f(x):
    if x < 9:
        return x
    if x >= 9:
        return f(x%9)+f(x//9)
for i in range(4*(6**20),5*(6**20)):
    if f(i) == 121:
        q += 1
print(q)