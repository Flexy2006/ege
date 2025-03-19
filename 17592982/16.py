a = open('1004.txt')
b = [int(i) for i in a]
x = 0
y = 0
mini = min(b)
maxi = max(b)
for j in range(0,len(b)-1):
    if (b[j] % 7 == mini % 7 and b[j+1] % 7 != mini % 7) or (b[j+1] % 7 == mini % 7 and b[j] % 7 != mini % 7) or (b[j] % 7 == mini % 7 and b[j+1] % 7 == mini % 7): 
        if (b[j] % 3 == maxi % 3 and b[j+1] % 3 != maxi % 3) or (b[j+1] % 3 == maxi % 3 and b[j] % 3 != maxi % 3) or (b[j] % 3 == maxi % 3 and b[j+1] % 3 == maxi % 3):
            x += 1
            y = max(y,b[j]+b[j+1])
print(x,y)