def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        temp_count = 0
        for j in range(1,int(i**(1/2)) + 1):
            if i % j == 0:
                temp_count += 1
                if i // j != j:
                    temp_count += 1
        if temp_count > limit:
            answer += power
        else:
            answer += temp_count
    return answer