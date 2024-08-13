def solution(arr):
    answer = []
    #2의 인덱스를 담기 위한 임시 리스트
    temp = []
    #arr을 인덱스 형식으로 순회
    for i in range(len(arr)):
        #arr[i]번째 value값이 2면
        if arr[i] == 2:
            #temp리스트에 i번째 인덱스 값 저장
            temp.append(i)
    #for문 순회 완료시 temp의 길이가 0이면
    if len(temp) == 0:
        #2가 없다는 뜻이니까 answer에 -1 append
        answer.append(-1)
    #temp의 길이가 0이 아니면
    else:    
        #answer에 arr배열에 temp최저값 부터 temp최대값 +1 까지 슬라이싱 한 배열을 저장
        answer = arr[min(temp):max(temp)+1]
    return answer
