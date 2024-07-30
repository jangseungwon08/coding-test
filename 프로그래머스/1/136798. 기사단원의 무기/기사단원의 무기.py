def solution(number, limit, power):
    answer = 0
    #일단 각 숫자의 약수를 세기위해서 range함수를 사용하여 1부터 number까지의 숫자를 순회
    for i in range(1,number+1):
        #temp_count 0 으로 초기화
        temp_count = 0
        #제곱근 위 아래의 약수 개수가 같다는 공식을 이용(i의 제곱근이 정수 라는 제한)
        #1부터 i의 제곱근 +1까지 ex i가 4이면 1부터 2까지의 범위까지 
        for j in range(1,int(i**(1/2)) + 1):
            # i에 j를 나눈 나머지 값이 없으면 약수
            if i % j == 0:
                temp_count += 1
                #i의 약수 개수 중복 약수를 취급하기 위해서 만약에 i가 36 j가 6이면 36//6 = j                    이므로 중복 약수이다.
                if i // j != j:
                    temp_count += 1
        #각 number의 약수를 구하고 temp_count가 limit보다 크면 answer에 power저장
        if temp_count > limit:
            answer += power
            #temp_count가 limit보다 작으면 answer에 temp_count저장
        else:
            answer += temp_count
    return answer