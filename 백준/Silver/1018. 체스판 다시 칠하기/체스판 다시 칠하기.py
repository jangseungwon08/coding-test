N, M = map(int, input().split())
board = list()
res = []
for _ in range(N):
    board.append(input())
# 0부터 N, M -7까지
for i in range(N-7):
    for j in range(M-7):
        draw_1 = 0
        draw_2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a + b) % 2 == 0:
                    #하나의 짝수일때 시작점이 W와 B인 것을 모두 구할 수 있다.
                    if board[a][b] != 'B':
                        draw_1 += 1
                    if board[a][b] != 'W':
                        draw_2 += 1
                else:
                    if board[a][b] != 'W':
                        draw_1 += 1
                    if board[a][b] != 'B':
                        draw_2 += 1
        res.append(min(draw_1,draw_2))
print(min(res))