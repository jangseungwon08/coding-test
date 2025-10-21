from collections import deque
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    q = deque(score)
    for i in range(0, len(score), m):
        if len(score) - i < m:
            break
        tmp = [q.popleft() for _ in range(i, i+m)]
        answer += min(tmp) * len(tmp)
    return answer