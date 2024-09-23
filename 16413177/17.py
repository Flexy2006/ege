def f(x):
    if x<3:
        return 1
    if x>2:
        q = 0
        for i in range(x):
            q += f(i)
        return q
print(f(18))#98304