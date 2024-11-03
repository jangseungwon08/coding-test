T = int(input())
for i in range(1,T+1):
    A, B, N = map(int,input().split())
    count = 0
    #입력받은 A와 B가 N보다 작거나 같을때만
    while A <= N and B <= N:
        #A가 B보다 크면
        if A > B:
            #B에 A를 더함
            B += A
        else:
            A += B
        count += 1
    print(count)