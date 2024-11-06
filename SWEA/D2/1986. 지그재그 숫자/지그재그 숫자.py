T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sum = 0
    for i in range(1,N+1):
        if i % 2 == 1:
            sum += i
        elif i % 2 == 0:
            sum -= i
    print("#"+str(tc), sum)