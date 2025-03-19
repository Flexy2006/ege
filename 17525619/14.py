for x in range(15):
    for y in range(15):
        p = int(f'90{x}4{y}',15)+int(f'91{x}{y}2', 16)
        if p % 56 == 0:
            print(p//56)