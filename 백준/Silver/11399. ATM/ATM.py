N = int(input())
N_list = list(map(int,input().split()))
N_list2 = sorted(N_list)
ans = 0
for i in range(N):
    temp = 0
    for j in range(i+1):
        temp += N_list2[j]
    ans += temp
print(ans)