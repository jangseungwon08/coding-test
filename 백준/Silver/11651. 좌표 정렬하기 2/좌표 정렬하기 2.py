import sys
input = sys.stdin.readline
N = int(input())
N_list = []
for _ in range(N):
    x, y = map(int , input().split())
    N_list.append((x,y))
N_list.sort(key = lambda y:(y[1], y[0]))
for x,y in N_list:
    print(x, y)