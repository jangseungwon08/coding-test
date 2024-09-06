def solution(my_string):
    answer = 0
    temp = my_string.split(' ')
    answer = int(temp[0])
    for i in range(1, len(temp), 2):
        num = int(temp[i+1])
        if temp[i] == "+":
            answer += num
        elif temp[i] == "-":
            answer -= num
    return answer