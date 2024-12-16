def f(x):
    a = 0
    if x < 3:
        return 1
    if x > 2:
        for i in range(1, x):
            a += f(i)
        return a
print(f(18))