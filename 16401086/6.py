q = 0
for i in range(1000,10000):
    a = i//1000
    b = (i - a*1000)//100
    c = (i - a*1000-b*100)//10
    d = i - a*1000-b*100-c*10
    if a % 2 == 1 and b % 2 == 1 and c % 2 == 1 and d % 2 == 1:
        if a + b < c + d:
            number = str(a+b)+str(c+d)
        else:
            number = str(c+d)+str(a+b)
        if number == "616":
            q += 1
print(q)#12
        