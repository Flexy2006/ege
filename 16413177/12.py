x = "7"*85
while "333" in x or "777" in x:
    if '333' in x:
        x = x.replace("333", "7", 1)
    else:
        x = x.replace("777", "3", 1)
print(x)#377