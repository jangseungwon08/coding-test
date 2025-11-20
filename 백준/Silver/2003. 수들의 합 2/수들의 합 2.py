N, M = map(int, input().split())
N_list = list(map(int, input().split()))
total = 0
interval_sum = 0
end = 0
for i in range(N):
    while interval_sum < M and end < N:
        interval_sum += N_list[end]
        end += 1
    if interval_sum == M:
        total += 1
    interval_sum -= N_list[i]
print(total)