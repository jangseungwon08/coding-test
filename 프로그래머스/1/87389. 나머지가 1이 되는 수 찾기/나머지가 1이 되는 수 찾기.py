def solution(n):
    answer = 0
    s =[]
    for i in range(1, n+1):
        if n % i == 1:
            s.append(i)
            answer = min(s)
    return answer