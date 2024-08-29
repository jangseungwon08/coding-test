def solution(arr, queries):
    answer = []
    #queries순회하면서 s e k 를 추출
    for s, e, k in queries:
        #2차원 배열 안에서 하나의 쿼리가 끝나면 다시 초기화
        temp_arr = []
        #s e+1까지 순회하면서
        for i in range(s, e+1):
            #arr[i]가 k보다 크면
            if arr[i] > k:
                #temp_arr에 arr[i]값 저장
                temp_arr.append(arr[i])
        #for문 다 끝나고 temp_arr이 존재하면
        if temp_arr:
            #answer에 temp_arr최솟값 append
            answer.append(min(temp_arr))
            #temp_arr이 비어있으면 k보다 큰 값이 없다는 뜻이니
        else:
            #answer에 -1 append
            answer.append(-1)
    return answer