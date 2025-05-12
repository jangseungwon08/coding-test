import sys
input = sys.stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))
for i in range(1,N):
    N_list[i] += N_list[i-1]
for _ in range(M):
    start, end = map(int ,input().split())
    if start == 1:
        ans = N_list[end-1]
        print(ans)
    else:
        ans = N_list[end-1] - N_list[start-2]
        print(ans)