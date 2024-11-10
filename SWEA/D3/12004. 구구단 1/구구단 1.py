T = int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = []
    ans_list = []
    for i in range(1,10):
        if N % i == 0:
            N_list.append(i)
    for j in range(len(N_list)):
        for k in range(len(N_list)):
            if N_list[j] * N_list[k] == N:
                ans_list.append(N)
    if len(ans_list) > 0:
        print('#'+str(tc), 'Yes')
    else:
        print('#'+str(tc), 'No')