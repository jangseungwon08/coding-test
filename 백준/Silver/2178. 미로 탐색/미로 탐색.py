from collections import deque
N ,M = map(int, input().split())
miro = []
#상우하좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
q = deque()
for i in range(N):
    miro.append(list(map(int, input())))
q.append([0,0])
while q:
    r,c = q.popleft()
    for i in range(4):
        dx = dr[i] + r
        dy = dc[i] + c
        if 0<= dx < N and 0 <= dy < M and miro[dx][dy] == 1:
            q.append([dx,dy])
            miro[dx][dy] = miro[r][c] + 1
print(miro[-1][-1])