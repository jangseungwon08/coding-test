#바구니 개수 N개 공을 넣으려는 횟수 M번
N, M = map(int, input().split())
N_list = [0 for i in range(N)]
for _ in range(M):
    i, j ,k = map(int, input().split())
    for index in range(i, j+1):
        N_list[index-1] = k
for i in range(N):
    print(N_list[i], end = ' ')