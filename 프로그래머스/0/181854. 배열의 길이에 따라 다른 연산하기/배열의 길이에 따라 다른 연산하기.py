def solution(arr, n):
    answer = []
    
    for i in range(len(arr)):
        #arr길이 홀수면
        if len(arr) % 2:
            #짝수 인덱스의 위치이면
            if i % 2 == 0:
                #n값 더해준 것을 append시켜준다.
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
        #arr길이 짝수면
        else:
            #홀수 인덱스의 위치이면
            if i % 2:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    return answer