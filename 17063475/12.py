def prost(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
mini = 1000000
for x in range(100):
    for y in range(100):
        s = "0" + "1"* x + "2"* y
        if len(s) > 44:
            while ('01' in s) or ('02' in s):
                s = s.replace("02", "1110", 1)
                s = s.replace("01", "220", 1)
            if prost(s.count("1") + s.count("2") * 2):
                mini = min(mini, x + 2*y)
print(mini)