N = int(input())
N_list = list()
for _ in range(N):
    N_list.append(list(map(int,input().split())))

def recursive(pool_list,size):
    if size == 1:
        return pool_list[0][0]
    half = size // 2
    next_pooling = [[0 for _ in range(half)] for _ in range(half)]
    
    for i in range(0,size,2):
        for j in range(0,size, 2):
            pool = [
                pool_list[i][j],
                pool_list[i][j+1],
                pool_list[i+1][j],
                pool_list[i+1][j+1]
            ]
            pool.sort()
            second_large = pool[-2]
            next_pooling[i//2][j//2] = second_large
    return recursive(next_pooling, half)
res = recursive(N_list, N)
print(res)