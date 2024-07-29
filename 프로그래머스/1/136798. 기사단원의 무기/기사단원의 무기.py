def solution(number, limit, power):
    answer = 0
    #일단 각 숫자의 약수를 세기위해서 range함수를 사용하여 1부터 number까지의 숫자를 순회
    for i in range(1,number+1):
        #temp_count 0 으로 초기화
        temp_count = 0
        #1부터 i의 제곱근 +1까지 ex i가 4이면 1부터 2까지의 범위까지 
        for j in range(1,int(i**(1/2)) + 1):
            # i에 j를 나눈 나머지 값이 없으면 약수
            if i % j == 0:
                temp_count += 1
                #i에 j를 정수형 나누기 한 값이 j의 값과 같지 않으면 약수
                if i // j != j:
                    temp_count += 1
        #각 number의 약수를 구하고 temp_count가 limit보다 크면 answer에 power저장
        if temp_count > limit:
            answer += power
            #temp_count가 limit보다 작으면 answer에 temp_count저장
        else:
            answer += temp_count
    return answer
