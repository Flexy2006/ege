a = 49**10+7**30-49
n = ""
while a > 0:
    n += str(a%7)
    a = a // 7
c = n[::-1]
c = list(map(int, str(c)))
print(c.count(6))#18