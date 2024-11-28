n = int(input())
three, five =0, 0
if n % 5 ==0:
    print(n // 5)
else:
    while n > 0:
        n -= 3
        three +=1
        if n% 5 == 0:
            five += n // 5
            print(three + five)
            break
        elif n == 1 or n == 2:#5에서 3을 빼고 난 나머지는 1 or 2이기때문
            print(-1)
            break
        elif n == 0:
            three = n // 3
            print(three)
            break