def solution(my_str, n):
    answer = []
    #0부터 my_str길이까지 nstep만큼 인덱스 범위 ex(0 6 12 18)
    for i in range(0,len(my_str), n):
        #i번째 부터 i+n까지 범위까지 슬라이싱
        #ex) 0번부터 6번 , 6번부터 11번인덱스까지 , 12번부터 17번인덱스까지
        answer.append(my_str[i:i+n])
    return answer