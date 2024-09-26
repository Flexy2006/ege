def f(x):
    if x<=2:
        return 1
    if x>2:
        return f(x - 2)*x
print(f(7))#105