q = []
x = 1111111110-6+48
m = 0
for N in range(1, 1000):
    R = bin(N)[2:]
    if len(bin(N % 3)[2:]) < 2:
        R += bin(N % 3)[2:] + "0"
    else:
        R += bin(N % 3)[2:]
    R += str(int(R) % 5) + "0"*2
    q.append(int(R, 2))
while x < 1444444416:
    m += 1
    x += 48
    if x > 1444444416:
        break   
    m += 1
    x += 32
    if x > 1444444416:
        break
    m += 1
    x += 16
print(m)

    
