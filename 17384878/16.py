def f(x):
    if x == 0:
        return 0
    if x % 2 == 0:
        return f(x/2)
    if x % 2 == 1:
        return 1 + f(x-1)
print(f(12))