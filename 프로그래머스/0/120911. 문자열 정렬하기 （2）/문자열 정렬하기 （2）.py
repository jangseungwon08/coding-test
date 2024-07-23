def solution(my_string):
    answer = ''
    #문자열을 모두 소문자로 바꾸고 list형식으로 형 변환을 한 값을 my_string1에 저장
    my_string1 = list(my_string.lower())
    #list형식인 my_string1을 sort함수를 사용하여 오름차순 정렬
    my_string1.sort()
    #join함수를 사용하여 ''을 기준으로 my_string1을 합침
    answer = ''.join(my_string1)
    return answer