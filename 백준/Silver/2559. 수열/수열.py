import sys
input = sys.stdin.readline
N ,K = map(int, input().split())
N_list = list(map(int, input().split()))
window = sum(N_list[:K])
answer = window
for i in range(K,N):
    window += N_list[i] - N_list[i-K]
    answer = max(answer,window)
print(answer)