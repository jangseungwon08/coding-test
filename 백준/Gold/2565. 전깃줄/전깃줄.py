N = int(input())
N_list = []
dp = [0] * (N+1)
for _ in range(N):
    a, b = map(int, input().split())
    N_list.append([a,b])
N_list = sorted(N_list, key=lambda x:x[0])
for i in range(len(N_list)):
    for j in range(i):
        if N_list[i][1] > N_list[j][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(N - (max(dp)+1))