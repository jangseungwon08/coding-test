def solution(arr, flag):
    answer = []
    #flag를 index형식으로 접근 flag == arr
    for i in range(len(flag)):
        #flag[i]의 값이 True면
        if flag[i]:
            #arr[i]*2범위만큼 arr[i]의 value값을 answer배열에 append
            for j in range(arr[i]*2):
                answer.append(arr[i])
                #false이면
        else:
            #arr[i]범위만큼 answer배열 마지막 원소값 제거
            for k in range(arr[i]):
                answer.pop()
    return answer