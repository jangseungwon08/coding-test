def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    for i in range(0, len(score), m):
        if i + m > len(score):
            break
        answer += score[i+m-1] * m
    return answer