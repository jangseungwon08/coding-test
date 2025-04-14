import sys
input = sys.stdin.readline
N = int(input())
N_set = set()
for _ in range(N):
    a , b =input().split()
    if a == "ChongChong":
        N_set.add(a)
        N_set.add(b)
    elif b == "ChongChong":
        N_set.add(b)
        N_set.add(a)
    if a in N_set or b in N_set:
        N_set.add(a)
        N_set.add(b)
print(len(N_set))