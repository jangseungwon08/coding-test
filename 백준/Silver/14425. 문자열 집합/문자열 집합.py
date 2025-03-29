import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
N_set = set()
M_list = []
res = 0
for _ in range(N):
    N_set.add(input())
for _ in range(M):
    M_list.append(input())
for i in M_list:
    if i in N_set:
        res += 1
print(res)