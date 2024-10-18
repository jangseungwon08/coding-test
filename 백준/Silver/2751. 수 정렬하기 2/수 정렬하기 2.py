import sys
N = int(sys.stdin.readline().strip())
N_list = []
for _ in range(N):
    N_list.append(int(sys.stdin.readline().strip()))
N_list.sort()
for i in N_list:
    print(i)