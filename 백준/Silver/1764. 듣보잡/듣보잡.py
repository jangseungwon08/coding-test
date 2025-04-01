import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
N_set = set()
total_list = []
#듣지못한사람
for _ in range(N):
    N_set.add(input().strip())
#보도 못한 사람
for _ in range(M):
    name = input().strip()
    if name in N_set:
        total_list.append(name)
total_list.sort()
print(len(total_list))
for i in total_list:
    print(i)