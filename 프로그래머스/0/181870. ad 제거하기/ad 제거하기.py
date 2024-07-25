def solution(strArr):
    answer = []
    #strArr을 for문
    for i in strArr:
        #i의 문자열값에 'ad'가 없으면
        if 'ad' not in i:
            #answer배열에 i문자열을 append함(순서를 유지해야하기 때문)
            answer.append(i)
    return answer