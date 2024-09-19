def s(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    return s(x + 1, y) + s(x + 2, y) + s(x + 5, y)
print(s(21, 30))#75