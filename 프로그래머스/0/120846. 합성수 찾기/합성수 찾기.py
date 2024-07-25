def solution(n):
    answer = 0
    #for문 반복
    for i in range(1,n+1):
        count = 0
        #각 i의 값 마다 약수를 구하기 위해서 j반복
        for j in range(1, i+1):
            #j가 i의 약수일 때
            if i % j == 0:
                #count 1 증가
                count += 1
        #count를 찾는 for문을 다 돌고 나서
        #count의 값이 3이상이면
        if count >= 3:
            #answer 1 증가
            answer += 1
                
    return answer