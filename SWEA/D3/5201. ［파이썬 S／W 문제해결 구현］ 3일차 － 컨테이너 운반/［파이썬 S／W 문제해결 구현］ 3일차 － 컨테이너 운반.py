T = int(input())
for tc in range(1,T+1):
    N ,M = map(int, input().split())
    w_list = list(map(int,input().split()))
    t_list = list(map(int,input().split()))
    w_list.sort(reverse = True)
    ans = 0
    for i in range(len(w_list)):
        for j in range(len(t_list)):
            if t_list[j] >= w_list[i]:
                ans += w_list[i]
                t_list.pop(j)
                break
    print('#' + str(tc), ans)