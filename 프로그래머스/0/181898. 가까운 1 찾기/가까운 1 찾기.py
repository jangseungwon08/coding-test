def solution(arr, idx):
    #arr범위만큼 for문을 돌린 뒤
    for i in range(len(arr)):
        #i가 idx보다 크거나 같으면서 value값이 1인 것을 찾으면 그 인덱스 값을 리턴
        if i >= idx and arr[i]:
            return i
        #for문 안에 else문을 사용하면 안된다. 왜냐하면 else문을 사용할 시에는 정답값을 찾아도
        #for문을 계속 돌면서 정답값이 -1로 업데이트 될 수 있기 때문에
        #for문을 다 돌았는데 못찾았으면 -1리턴
    return -1