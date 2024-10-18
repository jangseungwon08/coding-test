N, K = map(int,input().split())
N_list = list(map(int,input().split()))
N_list.sort(reverse = True)
print(N_list[K-1])