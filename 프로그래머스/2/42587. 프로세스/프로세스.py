from collections import deque
def solution(priorities, location):
    answer = 0
    candidate_que = deque([(i,p) for i,p in enumerate(priorities)])
    print(candidate_que)
    while candidate_que:
        current_process = candidate_que.popleft()
        if any(current_process[1] < other_process[1] for other_process in candidate_que):
            candidate_que.append(current_process)
        else:
            answer += 1
            if current_process[0] == location:
                return answer
    return answer