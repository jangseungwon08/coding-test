def solution(my_string, is_suffix):
    answer = 0
    temp = []
    #접두사인지 확인하기와 같은 문제
    for i in range(len(my_string)):
        temp.append(my_string[i:])
        if is_suffix in temp:
            answer = 1
        else:
            answer = 0
    return answer