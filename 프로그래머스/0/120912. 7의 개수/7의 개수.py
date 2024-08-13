def solution(array):
    answer = 0
    #k의 개수 문제와 동일
    for i in array:
        answer += str(i).count("7")
    return answer