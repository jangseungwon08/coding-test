def solution(arr):
    stk = []
    i = 0
    #i가 arr의 길이보다 작을때만 while문 동작
    while i < len(arr):
        #len(stk) 가 빈 배열일 때
        if len(stk) == 0:
            #stk에 arr[i]번째 value값 append
            stk.append(arr[i])
            #i에 1 더함
            i += 1
            #stk에 원소가 있고 arr[i] value값이 stk의 마지막 원소 값 보다 크면
        elif len(stk) > 0 and arr[i] > stk[-1]:
            #stk에 arr[i] value값 append
            stk.append(arr[i])
            #i에 1 더함
            i += 1
            #stk에 원소가 있고 stk마지막 원소가 arr[i] value값 보다 크거나 같으면
        elif len(stk)> 0 and stk[-1] >= arr[i]:
            #stk 마지막 원소를 stk에서 제거(pop)
            stk.pop()
    return stk