def solution(balls, share):
    #balls 팩토리얼 구하기 위해서 1로 초기화
    balls_fac = 1
    #share 팩토리얼 구하기 위해 1로 초기화
    share_fac = 1
    #ball-share값 팩토리얼 구하기 위해 1로 초기화
    balls_share_fac = 1
    #1부터 balls값 까지 for문
    for i in range(1,balls+1):
        #i값 다 곱함
        balls_fac *= i
    for j in range(1,share+1):
        share_fac *= j
    for k in range(1, (balls-share)+1):
        balls_share_fac *= k
        #balls_fac 에 balls-share의 팩토리얼 값 * share의 팩토리얼 값을 먼저 곱한 뒤 나눠줌
    return balls_fac // (balls_share_fac * share_fac)