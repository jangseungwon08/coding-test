def solution(num_list):
    answer = 0
    #num_list for문 돌리면서
    for i in num_list:
        count = 0
        #i가 1이 아닐때만
        while i != 1:
            #1인지 검사 하는 조건문
            if i != 1:
                #1이 아니고 홀수면
                if i % 2:
                    #i-1 에 2를 나눈 값을 i에 다시 업데이트
                    i = (i -1) / 2
                    #count 1증가
                    count += 1
                    #짝수면
                elif i % 2 == 0:
                    #i에 2를 나눈 값을 없데이트 한 후
                    i = i /2
                    #count 1 증가
                    count += 1
                #i가 1이면 나눠줄 값이 없으니 count를 초기화 한 값 대입
            else:
                anwer += count
        #while문 탈출하고 for문 가장 마지막에 answer에 count값 누적 업데이트
        answer += count
    return answer