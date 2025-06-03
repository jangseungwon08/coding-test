N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()
ans_list = list()
temp = 0
for i in range(N):
    temp += N_list[i]
    ans_list.append(temp)
print(sum(ans_list))