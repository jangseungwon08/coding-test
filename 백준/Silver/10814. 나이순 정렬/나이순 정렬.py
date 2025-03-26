import sys
input = sys.stdin.readline
N = int(input())
N_list = []
for _ in range(N):
    x, y = input().split()
    N_list.append((int(x),y))
N_list.sort(key = lambda x:x[0])
for x,y in N_list:
    print(x,y)