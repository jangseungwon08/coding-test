def solution(n):
    answer = 0
    #6조각으로 잘라줘서 6으로 설정
    n2 = 6
    #n 과 n2를 나눈 나머지가 0이 아닐때만(n2 % n 이 0이면 break로 루프빠져나감)
    while n2 % n != 0:
        #n2에 6 더함->한판 더 
        n2 += 6
    #루프 빠져나와서 n2정수 나누기 6을 한 값을 answer에 저장
    answer = n2 // 6
    return answer