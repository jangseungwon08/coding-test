###완전탐색###
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    count = 0
    #원점을 중심으로 해야되니까 -N부터 N+1(N)까지
    for x in range(-N, N+1):
        #y축도 원점을 중심으로 -N부터 N+1(N)까지
        for y in range(-N, N+1):
            #문제에 주어진 대로 x**2 + y**2 <= N**2인 격자점
            if ((x**2) + (y**2)) <= N**2:
                #일 경우에만 count +1
                count += 1
    #x와 y 둘 다 돌면 count값 출력
    print('#'+str(tc), count)