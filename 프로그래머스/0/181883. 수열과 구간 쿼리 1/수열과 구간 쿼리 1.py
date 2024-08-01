def solution(arr, queries):
    #0 1 2  쿼리 2차배열 순회
    for i in range(len(queries)):
        # 0 1 , 1 2 , 2 3
        #queries[i]를 시작점 끝점으로 나눈다
        s, e = queries[i]
        #j를 s부터 e+1(e)까지 범위를 둬서
        for j in range(s, e+1):
            #arr[j]값에 1을 더해준다
            arr[j] += 1
    return arr