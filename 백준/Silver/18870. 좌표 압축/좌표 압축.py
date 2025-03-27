import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
N_list2 = sorted(set(N_list))

dic = {N_list2[i]: i for i in range(len(N_list2))}


for i in N_list:
    print(dic[i], end = ' ')