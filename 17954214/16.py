def f(x):
    if x == 0:
        return 0
    if x > 0 and x % 3 == 2:
        return f(x-1) + 1
    if x > 0 and x % 3 < 2:
        return f((x - (x%3)) / 3)

print(f(6))