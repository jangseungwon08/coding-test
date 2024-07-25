def solution(a, b):
    answer = 0
    #a 그리고 b가 홀수일때
    if a%2 and b%2:
        answer = (a**2) + (b**2)
        #a 또는 b가 홀수일때
    elif a%2 or b%2:
        answer = 2*(a+b)
        #둘 다 홀수가아닐때
    else:
        #abs->절대값
        answer = abs(a-b)
    return answer