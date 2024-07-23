def solution(binomial):
    answer = 0
    #한 칸씩 띄어쓰기가 되어있어서 공백을 기준으로 세 칸으로 나눈다.
    a, op, b = binomial.split(' ')
    # op가 +일때는 int로 형 변환 한 뒤 a와 b를 연산한다
    if op == "+":
        answer = int(a) + int(b)
    elif op == "-":
        answer = int(a) - int(b)
    elif op == "*":
        answer = int(a) * int(b)
    return answer