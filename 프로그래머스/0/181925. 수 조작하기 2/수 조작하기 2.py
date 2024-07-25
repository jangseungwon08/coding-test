def solution(numLog):
    answer = ''
    #numLog를 1부터 끝까지 
    for i in range(1,len(numLog)):
        #numLog[i]의 값이 이전 값에 1이 더해졌으면
        if numLog[i] == numLog[i-1] + 1:
            #answer에 'w' 저장
            answer += 'w'
            #i번째 value값이 i-1번째 value값에 -1 값이랑 같으면
        elif numLog[i] == numLog[i-1] - 1:
            answer += 's'
        elif numLog[i] == numLog[i-1] + 10:
            answer += 'd'
        elif numLog[i] == numLog[i-1] - 10:
            answer += 'a'
    return answer