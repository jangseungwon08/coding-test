def solution(n):
    #list 컴프리헨션
    #answer = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    #answer에 [0]*n을 0 1 2 행까지 구한다
    answer = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            #i의 값과 j의 값이 같으면
            if i == j:
                #answer[i][j]번째에 1을 저장
                answer[i][j] = 1
    return answer