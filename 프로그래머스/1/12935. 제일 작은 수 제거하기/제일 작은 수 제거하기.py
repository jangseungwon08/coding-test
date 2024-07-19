def solution(arr):
    answer = []
    #가장 작은수를 제거하기 위해서 sort함수와 reverse = True를 사용하여                            arr을 내림차순으로 정렬한다.
    #arr.sort(reverse = True)
    #그리고 pop함수를 사용하여 가장 마지막 원소를 리턴하고 제거한다.
    arr.remove(min(arr))
    #arr배열에 원소값이 존재할 경우
    if arr:
        #answer에 가장 작은 값을 제거한 배열을 리턴하고
        answer = arr
        #arr배열이 빈 배열일 경우 -1을 리스트로 채워 answer에 리턴해준다.
    else:
        answer = [-1]
    return answer