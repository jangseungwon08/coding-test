#arr의 각 원소중 값이 50보다 크고 짝수라면 2로 나눔, 50보다 작고 홀수라면 2를 곱하고 1을 더함
def solution(arr):
    answer = 0
    #원하는 값을 얻기위해서 무한반복 사용
    while True:
        #temp_arr배열에 arr.copy()를사용하여 얕은 복사를 해서 원본을 유지한 채로 복사한다.
        #arr의 업데이트 이전 배열을 복사
        temp_arr = arr.copy()
        #arr을 인덱스 형식으로 순회
        for i in range(len(arr)):
            #arr[i]의 값이 50이상 그리고 짝수면
            if arr[i] >= 50 and arr[i] % 2 ==0:
                #arr[i]값에 2를 나눠서 업데이트
                arr[i] = arr[i] // 2
                #50이하고 홀수이면
            elif 50 > arr[i] and arr[i] % 2:
                #2곱하고 1더한값을 업데이트
                arr[i] = (arr[i]*2) + 1
        #arr 전체 순회를 다 하면 1번 반복 뜻이니까 1 누적
        answer += 1
        #현재 arr리스트 값과 이전 temp_arr의 값이 같으면
        if arr == temp_arr:
            #arr이 한번 더 업데이트 됐다는 뜻이므로 1 감소
            #감소 후 while문 탈출
            break
    return answer -1