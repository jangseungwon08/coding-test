def solution(arr):
    answer = []
    #일단 처음에는 arr[0]의 값 즉 1이 answer리스트가 비어있으니 들어간다.
    answer.append(arr[0])
    #for문을 1부터 arr길이만큼 돌면서
    for i in range(1,len(arr)):
        # arr의 i번째 인덱스값과 arr의 i-1 즉 i전의 인덱스 값이 다르면 answer에 append를
        #이용하여 arr의 i번째 인덱스값을 넣어준다.
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            #이렇게하면 arr의 원소들의 순서를 유지할 수 있다.
    return answer