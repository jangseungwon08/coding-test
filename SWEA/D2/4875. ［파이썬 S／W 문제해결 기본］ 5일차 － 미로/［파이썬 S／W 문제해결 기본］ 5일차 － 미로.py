from collections import deque
T = int(input())
#상우하좌
dr = [-1,0,1,0]
dc = [0,1,0,-1]
for a in range(1,T+1):
    N = int(input())
    N_list = []
    q = deque()
    for _ in range(N):
        N_list.append(list(map(int,input())))
    for i in range(N):
        for j in range(N):
            if N_list[i][j] == 2:
                q.append([i,j])
    found_target = False
    while q:
        if found_target:
            break
        length = len(q)
        for _ in range(length):
            r,c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<= nr < N and 0<= nc < N:
                    if N_list[nr][nc] == 3:
                        print(f'#{a} 1') 
                        found_target = True
                        break
                    elif N_list[nr][nc] == 0:
                        N_list[nr][nc] = -1
                        q.append([nr,nc])
    if not found_target:
        print(f'#{a} 0')