def solution(participant, completion):
    answer = ''
    part_dict = {}
    for k, v  in enumerate(participant):
        part_dict[v] = part_dict.get(v, 0) + 1
    for i in completion:
        part_dict[i] -= 1
        if part_dict[i] == 0:
            del part_dict[i]
    for i in part_dict.keys():
        answer += i
    return answer