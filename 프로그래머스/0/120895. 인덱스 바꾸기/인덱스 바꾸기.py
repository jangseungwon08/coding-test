def solution(my_string, num1, num2):
    answer = ''
    #list형식으로 바꿔준 다음
    my_string = list(my_string)
    #list의 인덱스 형식으로 my_string의 num1과 num2 num2와 num2을 교체해준다.
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    #문자열 형식으로 나타내기 위해서 join함수를 사용하여 answer에 대입한다
    answer = ''.join(my_string)
    return answer