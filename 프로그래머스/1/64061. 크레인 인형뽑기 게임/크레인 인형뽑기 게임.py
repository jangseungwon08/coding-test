def solution(board, moves):
    answer = 0
    answer_list = []
    for move in moves:
        for row in board:
            if row[move-1] != 0:
                answer_list.append(row[move-1])
                row[move - 1] = 0
                break
        i = 0
        while i < len(answer_list) - 1:
            if answer_list[i] == answer_list[i+1]:
                answer_list.pop(i)
                answer_list.pop(i)
                answer += 2
            else:
                i += 1
    return answer