a, b = map(int, input().split())
if (b - 45) < 0:
    if a == 0:
        b = 60 + (b - 45)
        print(23 , b)
    else:
        b = 60 + (b-45)
        print(a-1, b)
else:
    print(a, b-45)