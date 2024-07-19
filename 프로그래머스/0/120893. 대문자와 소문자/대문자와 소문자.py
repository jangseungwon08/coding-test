def solution(my_string):
    answer = ''
    #my_string의 for문을 돌면서
    for i in my_string:
        # my_stirng의 각 문자열이 대문자인지 조건문으로 사용
        if i.isupper() == True:#isupper는 대문자인지 소문자인지 구분하는 함수(리턴값 true,false)
            #만약 대문자면 소문자로 변환하여 answer에 대입
            answer += i.lower()
            #my_string의 문자열이 소문자면 (False)
        else:
            #answer에 대문자로 변환한 값을 대입
            answer += i.upper()
    return answer