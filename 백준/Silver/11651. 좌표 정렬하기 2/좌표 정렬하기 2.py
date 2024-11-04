N = int(input())
N_list = []
for _ in range(N):
    x, y = map(int, input().split())
    N_list.append((x, y))
N_list = sorted(N_list, key= lambda x: (x[1], x[0]))
for x, y in N_list:
    print(x, y)