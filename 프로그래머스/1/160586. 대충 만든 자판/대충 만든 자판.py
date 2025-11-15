def solution(keymap, targets):
    answer = []
    for target in targets:
        temp = 0
        for i in target:
            key_candidate = []
            for key in keymap:
                if i in key:
                    key_candidate.append(key.index(i))
            if not key_candidate:
                temp = -1
                break
            else:
                temp += min(key_candidate) + 1
        answer.append(temp)
    return answer