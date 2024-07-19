def solution(my_string):
    answer = []
    #한칸 공백을 기준으로 문자열을 list형식으로 나눠서 저장해준다.
    my_string = my_string.split(' ')
    #나눠준 문자열을 for문을 돌면서 
    for i in my_string:
        #i의 값이 참인 값 즉 문자열이 존재하는 경우만 answer에 순서대로 추가해준다.
        if i:
            answer.append(i)
    return answer