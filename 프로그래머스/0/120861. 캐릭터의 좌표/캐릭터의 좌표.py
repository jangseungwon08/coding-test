def solution(keyinput, board):
    answer = [0, 0]
    max_x , max_y = (board[0]-1) // 2 , (board[1]-1) // 2
    min_x , min_y = -(board[0]-1) // 2 , -(board[1]-1) // 2
    for i in keyinput:
        if max_x == 0 and max_y == 0:
            return answer
        else:
            if i == "up" and max_y > answer[1]:
                answer[1] += 1
            elif i == "down" and min_y < answer[1]:
                answer[1] -= 1
            elif i == "right" and max_x > answer[0]:
                answer[0] += 1
            elif i == "left" and min_x < answer[0]:
                answer[0] -= 1
    return answer