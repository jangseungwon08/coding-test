def solution(x1, x2, x3, x4):
    #(x1 v x2) ^ (x3 v x4)였으니까 논리연산자도 괄호를 이용하여 문제를 해결가능 하다
    if (x1 or x2) and (x3 or x4):
        return True
    else:
        return False
