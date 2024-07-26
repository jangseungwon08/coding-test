def solution(arr, flag):
    answer = []
    #flag를 index형식으로 접근 flag == arr
    for i in range(len(flag)):
        #flag[i]의 값이 True면
        if flag[i]:
            #[arr[i]]의 값을 갖는 리스트 요소를 arr[i]*2의 값만큼 곱해서 반복하여 answer에 저장
            answer += [arr[i]]* arr[i]*2
                #false이면
        else:
            '''
            #arr[i]범위만큼 answer배열 마지막 원소값 제거
            for k in range(arr[i]):
                answer.pop()
                '''
            answer = answer[:-arr[i]]
    return answer