def solution(s):
    answer = 0
    x = s[0]
    not_x = ""
    for i in range(1,len(s)):
        if len(x) == 0:
            x += s[i]
        elif s[i] not in x:
            not_x += s[i]
        else:
            x += s[i]
        if len(x) == len(not_x):
            answer += 1
            x , not_x = "", ""
    if x:
        answer += 1
    elif not_x:
        answer += 1
    return answer