def solution(intStrs, k, s, l):
    answer = []
    #intStrs를 인덱스 범위로 순회
    for i in range(len(intStrs)):
        #intStrs의 i번째 문자열을 s부터 l까지 부분 문자열 추출 한 int형 변환 한 값이 k보다 작으면
        if int(intStrs[i][s:s+l]) > k:
            #answer에 그 값 저장
            answer.append(int(intStrs[i][s:s+l]))
    return answer