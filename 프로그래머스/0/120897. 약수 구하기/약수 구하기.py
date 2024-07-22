def solution(n):
    answer = []
    #1부터 n+1(n)까지 for문 돌리면서
    for i in range(1, n+1):
        #n값을 i에 나눈 나머지가 0이면 answer배열에 차례대로 추가해준다.
        if n % i == 0:
            answer.append(i)
    return answer