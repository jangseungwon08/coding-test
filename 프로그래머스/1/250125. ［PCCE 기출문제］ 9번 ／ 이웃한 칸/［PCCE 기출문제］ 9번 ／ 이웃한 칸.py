def solution(board, h, w):
    #같은색 색칠된 칸의 개수 저장할 변수
    count = 0
    #보드 길이 저장할 변수
    n = len(board)
    #기준이 되는 지점에서 h축으로 +1 -1 w축으로 +1 -1로 정해서 4개의 dh, dw 리스트 형식으로 저장
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    #0부터 3까지 범위 순회
    for i in range(0,4):
        #기준 h에 대해서 dh[i]의 원소값을 더해주고 h_check에 저장 (w도 똑같이 한다)
        h_check , w_check = h + dh[i], w + dw[i]
        # h_check의 값이 0이상 n 미만 이고 w_check도 0 이상 n 미만이면(정해진 범위 초과 하지 않으면)
        if 0 <= h_check < n and 0 <= w_check < n:
            #board[h][w]의 색상 값 과 board[h_check][w_check]의 원소값 즉 같은색상이면
            if board[h][w] == board[h_check][w_check]:
                #count +1
                count += 1
    return count