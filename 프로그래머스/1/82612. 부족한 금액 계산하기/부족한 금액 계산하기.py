def solution(price, money, count):
    answer = 0
    n = 0
    for i in range(1,count+1):
        n += i*price
        if money >= n:
            answer = 0
        else:
            answer = n - money
    return answer