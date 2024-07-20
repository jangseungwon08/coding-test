def solution(str_list, ex):
    answer = ''
    #str_list의 각 원소문자열을 알기위해서 for문 돌림
    for i in str_list:
        #ex가 각 원소 문자열 i번째 value값에 없으면
        if ex not in i:
            #answer에 i를 추가해준다.
            answer += i
    return answer