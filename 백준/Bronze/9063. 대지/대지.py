N = int(input())
N_list = []
for _ in range(N):
    N_list +=  list(map(int,input().split()))
print((max(N_list[::2]) - min(N_list[::2])) * (max(N_list[1::2])-min(N_list[1::2])))