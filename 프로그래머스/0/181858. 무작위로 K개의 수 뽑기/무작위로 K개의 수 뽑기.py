def solution(arr, k):
    answer = []
    #arr에서 조건에 맞는 원소값들만 출력하기 위해 temp_arr 초기화
    temp_arr = []
    #arr을 순회하면서
    for i in arr:
        #k가 len(tempa_arr) 보다 크고 i가 temp_arr에 없으면
        if k > len(temp_arr) and i not in temp_arr:
            #temp_arr에 i추가
            temp_arr.append(i)
            #temp_arr의 길이가 k값과 같으면
    if len(temp_arr) == k:
        #answer에 temp_arr 저장
        answer = temp_arr
        #k가 temp_arr보다 길면
    elif k > len(temp_arr):
        # k가 temp_arr의 길이가 같지 않을때만 true
        while k != len(temp_arr):
            #temp_arr에 -1추가
            temp_arr.append(-1)
        #while문 다 끝난 후 temp_arr을 answer에 저장
        answer = temp_arr
    return answer