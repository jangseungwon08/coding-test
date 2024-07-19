def solution(myString, pat):
    answer = 0
    temp_str = ''
    #myString을 for문을 돌린다.
    for i in myString:
        #i의 값이 A이면 B로 바꿔주고
        if i == 'A':
            temp_str += 'B'
            #B이면 A로 바꿔준다.
        else:
            #그 값들을 temp_str에 대입해준다.
            temp_str += 'A'
            #pat의 문자열이 temp_str에 있으면
    if pat in temp_str:
        #1 반환
        answer = 1
        #그렇지 않으면 0 반환
    else:
        answer = 0
    return answer