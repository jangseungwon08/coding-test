N = int(input())
N_list = list()
for _ in range(N):
    N_list.append(list(map(int,input().split())))
count = [0 ,0]

def recursive(x,y, n):
    init_color = N_list[y][x]
    all = True
    for i in range(y,y+n):
        for j in range(x,x+n):
            if N_list[i][j] != init_color:
                all = False
                break
        if not all:
            break
        # 기저조건
    if all:
        count[init_color] += 1
        return
    else:
        # 4단계로 분할해서 정복
        half_n = n//2
        # 왼쪽 위 
        recursive(x,y,half_n)
        # 오른쪽 위
        recursive(x + half_n, y, half_n)
        #왼쪽 아래
        recursive(x,y + half_n, half_n)
        # 오른쪽 아래
        recursive(x + half_n, y +half_n , half_n)
recursive(0,0,N)
print(count[0])
print(count[1])