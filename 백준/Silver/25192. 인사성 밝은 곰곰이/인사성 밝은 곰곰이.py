import sys
input = sys.stdin.readline
N = int(input())
N_set = set()
count = 0
for _ in range(N):
    i = input().strip()
    if i == "ENTER":
        count += len(N_set)
        N_set.clear()
    else:
        N_set.add(i)
count += len(N_set)
print(count)