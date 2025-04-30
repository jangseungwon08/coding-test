def solution(n):
    answer = 0
    s = bin(n)[2:]
    one_len = ""
    for i in s:
        if i == "1":
            one_len += i
    while True:
        n += 1
        s = bin(n)[2:]
        compet = ""
        for i in s:
            if i == "1":
                compet += i
        if len(compet) == len(one_len):
            answer = n
            break
    return answer