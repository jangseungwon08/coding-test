T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    N_list = list(input().split())
    M_list = list(input().split())
    Q = int(input())
    ans = ''
    for i in range(Q):
        Y = int(input())
        N_mod = (Y % N) - 1
        M_mod = (Y % M) - 1
        ans += N_list[N_mod] + M_list[M_mod] + ' '
    print('#' + str(tc), ans)