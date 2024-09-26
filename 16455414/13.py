x = "8"*99+"1"
while "133" in x or "881" in x:
    if '133' in x:
        x = x.replace("133", "81", 1)
    else:
        x = x.replace("881", "13", 1)
print(x)#813