def f(x):
    if x == 1:
        return 1
    if x % 2 == 0:
        return x + f(x-1)
    if x > 1 and x % 2 == 1:
        return 2*f(x-2)
print(f(24))