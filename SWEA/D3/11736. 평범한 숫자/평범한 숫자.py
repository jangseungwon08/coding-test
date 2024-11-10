T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    count = 0
    for i in range(2,N):
        if (N_list[i-2] < N_list[i-1] < N_list[i]) or (N_list[i-2] > N_list[i-1] > N_list[i]):
            count += 1
    print('#'+str(tc), count)