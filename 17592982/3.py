def f(x,y,flag):
    if x == y:
        return 1
    if x > y + 1:
        return 0
    else:
        if flag == 1:
            return f(x*2,y,flag-1)+f(x*3,y,flag-1)
        else:
            return f(x-1,y,flag+1)+f(x*2,y,flag)+f(x*3,y,flag)
print(f(3,15,0))