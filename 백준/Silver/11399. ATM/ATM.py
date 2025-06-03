N = int(input())
N_list = list(map(int,input().split()))
N_list.sort()
ans = 0
for i in range(N):
    temp = 0
    for j in range(i+1):
        temp += N_list[j]
    ans += temp
print(ans)