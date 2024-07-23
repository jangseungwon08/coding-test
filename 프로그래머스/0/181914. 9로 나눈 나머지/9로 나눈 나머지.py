def solution(number):
    answer = 0
    #각 자리 숫자 합을 위한 변수
    plus = 0
    #number for문
    for i in number:
        #각 자리 i를 int로 형 변환 하여 plus변수에 저장
        plus += int(i)
    #for문에서 다 더한 plus값을 9로 나눈 나머지를 answer에 저장 후 리턴
    answer = plus % 9
    return answer