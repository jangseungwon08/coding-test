def solution(my_string, is_prefix):
    answer = 0
    temp = []
    #range(len())을 이용하여 인덱스 형식으로 접근할 수 있게 for문을 돌린다.
    for i in range(len(my_string)):
        #append함수를 사용하여 특정 인덱스까지의 문자열을 모두 temp에 저장해준다.
        temp.append(my_string[:i+1])
        #is_prefix의 문자열이 temp에 존재한다면 1을 리턴
        if is_prefix in temp:
            answer = 1
            #그렇지 않다면 0을 리턴
        else:
            answer = 0
    return answer