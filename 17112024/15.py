import sys
sys.setrecursionlimit(1000000000)
def f(n):
    if n < 15:
        return n
    if n >= 15:
        return f(n%15)*f(n//15)
q = 0
for i in range(1, 3**40):
    if f(i) == 7560:
        q += 1
print(q)