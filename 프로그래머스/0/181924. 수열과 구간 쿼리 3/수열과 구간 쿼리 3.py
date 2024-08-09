def solution(arr, queries):
    answer = []
    #쿼리의 range(len())인덱스 순회하면서
    for i in range(len(queries)):
        #2차원 배열이니까 queries[i]를 하면 원소값이 두개가 나와서 a , b로 두고
        a , b = queries[i]
        #arr[i]와 arr[j]의 값을 서로 바꾸니까 arr[a] 에 arr[b]를 대입하고, arr[b]에 arr[a]를          대입
        arr[a], arr[b] = arr[b], arr[a]
    return arr