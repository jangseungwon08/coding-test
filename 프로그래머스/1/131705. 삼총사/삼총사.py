def solution(number):
    answer = 0
    #number의 인덱스로 접근
    for i in range(len(number)):
        #i보다 1큰 수를 len(number)길이까지 j 반복문
        for j in range(i+1, len(number)):
            #j 보다 1큰 수를 len(number)길이까지 k 반복문
            for k in range(j+1, len(number)):
                # i j k 번째 value값의 합이 0일때만 answer 1 증가
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer