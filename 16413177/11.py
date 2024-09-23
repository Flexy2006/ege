x = "1"*82
while "11111" in x or "888" in x:
    if "11111" in x:
        x = x.replace("11111", "88", 1)
    elif "888" in x:
        x = x.replace("888", "8", 1)
print(x)#8811