def solution(myString, pat):
    answer = 0
    #myString을 인덱스 형식으로 순회
    for i in range(len(myString)):
        #myString[i:len(pat)+i:] 의 값이 pat과 같으면
        # i = 0 1 2 3 4 5
        #myString[0:2:] myString[1:3] myString[2:4] myString[3:5]형식으로 접근
        if myString[i:len(pat)+i:] == pat:
            #answer에 1증가
            answer += 1
    return answer
