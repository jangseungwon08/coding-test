N = int(input())
dp = [0] * (N+1)
N_list = [0]
for _ in range(N):
    N_list.append(int(input()))
dp[1] = N_list[1]
if N > 1:
    dp[2] = N_list[1] + N_list[2]
for i in range(3,N+1):
    dp[i] = max(dp[i-1], dp[i-2] + N_list[i] , N_list[i-1] + N_list[i] + dp[i-3])
print(max(dp))