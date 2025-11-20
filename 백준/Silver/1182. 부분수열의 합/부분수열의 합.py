from itertools import combinations as c
total = 0
N, S = map(int, input().split())
N_list = list(map(int, input().split()))
for i in range(1,N+1):
    for iter in c(N_list, i):
        if sum(iter) == S:
            total += 1
print(total)