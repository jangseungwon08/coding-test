def solution(a, d, included):
    answer = 0
    #included 인덱스 범위만큼 0부터 len(included)-1까지
    for i in range(len(included)):
        #등차수열 공식 an = a + (n-1)*d
        linear = a + (i*d)
        #included[i]번째 값이 True이면
        if included[i]:
            #answer에 등차수열 공식의 값linear 대입
            answer += linear
    return answer