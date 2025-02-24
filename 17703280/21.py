for x in "012345678":
    for y in "012345678":
        n = int(f"2{y}66{x}", 9) + int(f"{x}0{y}1", 12)
        if n % 170 == 0:
            print(n // 170)