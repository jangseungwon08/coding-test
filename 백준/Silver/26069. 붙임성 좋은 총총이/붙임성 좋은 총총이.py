import sys
input = sys.stdin.readline
N = int(input())
N_set = {"ChongChong"}
for _ in range(N):
    a , b =input().split()
    if a in N_set or b in N_set:
        N_set.add(a)
        N_set.add(b)
print(len(N_set))