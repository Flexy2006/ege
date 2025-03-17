for x in range(13):
    p = int(f'4C{x}4',15)+int(f'{x}62A',13)
    if p % 121 == 0:
        print(p//121)