T= int(input())
for tc in range(1,T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    ans_list = []
    for i in range(0,len(N_list)-1):
        for j in range(i+1,len(N_list)):
            if int(N_list[j]*0.75) == N_list[i]:
                ans_list.append(N_list[i])
                N_list.pop(j)
                break
    print('#'+str(tc), end= ' ')
    for n in ans_list:
        print(n, end= ' ')
    print()