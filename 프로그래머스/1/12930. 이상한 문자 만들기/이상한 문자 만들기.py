def solution(s):
    res = []
    temp = s.split(' ')
    for j in temp:
        answer = ''
        for i in range(len(j)):
            if i % 2 == 0:
                answer += j[i].upper()
            else:
                answer += j[i].lower()
        res.append(answer)
    return ' '.join(res)