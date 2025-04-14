import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
if len(N_list) == 1:
    print(N_list[0]**2)
else:
    print(max(N_list) * min(N_list))