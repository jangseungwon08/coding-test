def solution(n, m, section):
    num = 1
    a = section[0]
    for i in section:
        if i >= a + m:
            num += 1
            a = i
    return num