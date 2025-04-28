def solution(s):
    answer = []
    zero = []
    count = 0
    while len(s) > 1:
        temp = ""
        count += 1
        for i in s:
            if i == "1":
                temp += i
            else:
                zero.append(i)
        s = bin(len(temp))[2:]
    answer.append(count)
    answer.append(len(zero))
    return answer