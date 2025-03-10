def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x * 2, y)

print((f(3,14)*f(14,62)) - (f(3,14)*f(14,59)*f(59,62)))