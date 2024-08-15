def solution(arr, queries):
    answer = []
    for i in queries:
        #쿼리의 각 원소값 s e k값으로 나눈다.
        s, e, k = i[0], i[1], i[2]
        #s부터 e+1까지의 순회
        for j in range(s, e+1):
            #j의 값 자체가 k의 배수이면 (배수는 어떤 숫자가 다른 숫자로 나누어 떨어지는 것을 뜻함)
            #arr[j]번째 원소값에 1을 더한다
            if j % k == 0:
                arr[j] += 1
    return arr