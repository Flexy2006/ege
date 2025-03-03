a = 36**7+6**19-18
res = ''
while a != 0:
    res += str(a % 6)
    a //= 6
print(res.count('0'))