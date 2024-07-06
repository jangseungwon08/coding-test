def solution(left, right):
    answer = 0
    #left 부터 right+1까지 수를 계산해서 i에 대입
    for i in range(left, right+1):
        mea = 0
        #소인수 분해를 하기위해서 1부터 i+1까지의 수를 반복
        for j in range(1, i+1):
            #i 나머지 연산 j의 값이 0이면
            if i % j == 0:
                #약수 개수 +1
                mea += 1
                #아니면 그대로
            else:
                mea += 0
            #약수의 개수가 짝수면 그 약수의 수를 최종값에 더해준다.
        if mea % 2 == 0:
            answer += i
            #홀수면 빼준다.
        else:
            answer -= i
    return answer
