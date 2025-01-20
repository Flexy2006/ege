a = 25 ** 5 + 5 ** 14 - 5
res = ''
while a != 0:
    res += str(a % 5)
    a //= 5
print(res.count('4'))