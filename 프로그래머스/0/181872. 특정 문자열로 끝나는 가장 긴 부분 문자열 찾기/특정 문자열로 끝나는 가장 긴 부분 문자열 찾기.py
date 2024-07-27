def solution(myString, pat):
    answer = ''
    #myString을 인덱스 형식으로 순회
    for i in range(len(myString)):
        #myString[i]번째 원소값이 pat[-1]->마지막 문자와 같으면
        if myString[i] == pat[-1]:
            #answer에 myString의 처음부터 i+1=>i까지 answer에 저장
            #i+1까지 하는 이유는 슬라이싱 시 i-1번째 까지 접근하니까 i+1까지 해줌
            answer = myString[:i+1]
    return answer