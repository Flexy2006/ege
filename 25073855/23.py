def f(x, y):
    if x == y:
        return 1
    if x<y:
        return 0
    return f(x - 1, y) + f(x - 6, y) + f(x // 2, y)
print(f(34,29)*f(29,19)*f(19,6)-(f(34,29)*f(29,24)*f(24,19)*f(19,6)))