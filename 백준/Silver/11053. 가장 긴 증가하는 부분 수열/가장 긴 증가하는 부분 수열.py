N = int(input())
N_list = list(map(int, input().split()))
dp = [0] * (N+1)
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if N_list[j] < N_list[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))