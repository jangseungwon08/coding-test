import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int,input().strip().split()))
N_dict = {}
M = int(input())
M_list = list(map(int,input().strip().split()))
for i in N_list:
    if i in N_dict:
        N_dict[i] += 1
    else:
        N_dict[i] = 1
for i in M_list:
    if i in N_dict:
        print(N_dict[i], end = ' ')
    else:
        print(0, end = ' ')