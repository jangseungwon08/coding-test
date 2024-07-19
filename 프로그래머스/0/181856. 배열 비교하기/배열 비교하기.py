def solution(arr1, arr2):
    answer = 0
    #먼저 길이를 기준으로 구한다.
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer =-1
        #여기서는 arr1의 길이와 arr2의 길이가 같으면 배열의 합을 비교해서 구해야한다
    else:
        if sum(arr1)> sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1
        else:
            answer = 0
    return answer