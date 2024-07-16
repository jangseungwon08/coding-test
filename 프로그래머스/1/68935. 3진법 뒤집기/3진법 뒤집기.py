def solution(n):
    answer = 0
    while n !=0:
        #temp_arr.append(n % 3) 
        # (0*3 + 0) + (0*3 + 0) + (0*3 + 2) + 1이 된다.
        answer = answer*3 + (n%3)
        #n값을 갱신 시키기 위해서 정수형 나누기를 해준다.
        n = n // 3
    return answer
