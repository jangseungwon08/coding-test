def solution(t, p):
    answer = 0
    #임시 리스트 생성
    temp = []
    #예시 1번기준) 0부터 3까지의 범위를 한다.
    for i in range(len(t)-len(p) +1):
        temp.append(t[i:i+len(p)]) #인덱스 i번째부터 i+len(p)-1번째까지
        
    for j in temp:
        #정수 값 비교를 위해서 int로 형 변환 후 비교해준다
        if int(j) <= int(p):
            answer += 1
    return answer