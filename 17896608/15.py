def f(x):
    if x < 3:
        return 1
    if x > 2 and x % 2 == 1:
        return f(x-1)+3*f(x-2)
    if x > 2 and x % 2 == 0:
        return sum(f(i) for i in range(1,x))
print(f(28))

    