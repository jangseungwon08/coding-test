def solution(participant, completion):
    answer = ''
    completion_dict = dict()
    for i in participant:
        if i in completion_dict:
            completion_dict[i] += 1
        else:
            completion_dict[i] = 1
    for j in completion:
        if j in completion_dict:
            completion_dict[j] -= 1
    for k,v in completion_dict.items():
        if v > 0:
            answer = k
            break
    return answer