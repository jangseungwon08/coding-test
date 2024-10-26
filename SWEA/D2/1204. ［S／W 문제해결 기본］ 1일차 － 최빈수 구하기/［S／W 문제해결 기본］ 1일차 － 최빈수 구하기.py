T = int(input())
for i in range(1,T+1):
    N = int(input())
    N_list = list(map(int,input().split()))
    count = dict()
    ans_list = []
    answer = 0
    for j in N_list:
        if j not in count:
            count[j] = N_list.count(j)
    max_value = max(count.values())
    for k,v in count.items():
        if v == max_value:
            ans_list.append(k)
    if len(ans_list)>1:
        print('#'+str(i),max(ans_list))
    else:
        print('#'+str(i),ans_list[0])