def solution(arr):
    #이중 for문으로 2차원 배열을 다 돈다.
    for i in range(len(arr)):
        for j in range(len(arr)):
            #돌면서 i j  와 j i 의 value값이 하나라도 다르면 0 다 같으면 1을 리턴
            if arr[i][j] != arr[j][i]:
                return 0
    return 1