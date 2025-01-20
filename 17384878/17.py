a = open("1001.txt")
x = 0
y = 0
q = []
b = [int(i) for i in a]
for j in range(len(b)-1):
    if ((b[j]*b[j+1]) % 15 == 0) and ((b[j]+b[j+1]) % 7 == 0):
        x += 1
        y = max(y, b[j]+b[j+1])
print(x,y)
        
