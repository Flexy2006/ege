def f(n):
    if n < 3:
        return n
    if n >= 3 and n % 2 == 1:
        a = (7 * n + f(n - 1) - f(n - 2)) / 5
        return int(a)
    if n >= 3 and n % 2 == 0:
        b = (3 * n + f(n - 3)) / 3
        return int(b)
print(f(35))#49