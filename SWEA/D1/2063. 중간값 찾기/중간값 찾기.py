N = int(input())
N_list = list(map(int, input().split()))
N_list.sort()
mid = N // 2
print(N_list[mid])
