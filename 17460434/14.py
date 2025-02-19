a = 36**8+6**20-12
res = ''
while a != 0:
    res += str(a % 6)
    a //= 6
print(res.count('5'))