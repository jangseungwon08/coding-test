def solution(board, k):
    answer = 0
    #일단 행 부터 구하기 위해서 board의 인덱스 형식으로 for문 접근
    for i in range(len(board)):
        #그 후 열을 구하기 위해 board[i]번째 행의 열을 구한다.
        for j in range(len(board[i])):
            if k >= i + j:
                #answer에 board[i][j]값 누적해서 더해줌
                answer += board[i][j]
    return answer