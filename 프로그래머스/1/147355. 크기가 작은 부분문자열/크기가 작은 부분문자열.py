def solution(t, p):
    answer = 0
    #임시 리스트 생성
    temp = []
    # len(t)-len(p) +1을 해줌으로써 부분문자열의 인덱스 개수를 셀 수 있다.
    #따라서 7-3+1=5이다 0부터 4까지의 인덱스 -> 5개의 부분문자열 추출 가능
    for i in range(len(t)-len(p) +1):
        temp.append(t[i:i+len(p)]) #인덱스 i번째부터 i+len(p)-1번째까지 문자 추출
        
    for j in temp:
        #정수 값 비교를 위해서 int로 형 변환 후 비교해준다
        if int(j) <= int(p):
            answer += 1
    return answer