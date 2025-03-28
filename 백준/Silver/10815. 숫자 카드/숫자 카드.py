import sys
input = sys.stdin.readline
N = int(input())
N_set = set(map(int, input().split()))
M = int(input())
M_set = list(map(int, input().split()))
res = []
for i in M_set:
    if i in N_set:
        res.append(1)
    else:
        res.append(0)
for i in res:
    print(i, end = ' ')