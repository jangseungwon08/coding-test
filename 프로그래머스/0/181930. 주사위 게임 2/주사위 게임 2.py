def solution(a, b, c):
    answer = 0
    #a와 b와 c의 값이 같을 때
    if a ==b==c:
        answer = (a+b+c) * ((a**2) + (b**2) + (c**2)) * ((a**3) + (b**3) + (c**3))
    #a와 b 또는 a와 c 또는 b와 c가 같을 때
    elif a == b or a==c or b==c:
        answer = (a+b+c) * ((a**2) + (b**2) + (c**2))
        #위의 두개의 조건문을 만족하지 못할 때
    else:
        answer = a+b+c
    return answer