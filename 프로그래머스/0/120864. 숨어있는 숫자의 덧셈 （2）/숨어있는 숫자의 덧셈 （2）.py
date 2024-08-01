def solution(my_string):
    answer = 0
    temp_str = ''
    #my_string인덱스 범위 순회하면서
    for i in range(len(my_string)):
        #my_string[i]가 숫자일때
        if my_string[i].isdigit():
            #temp_str에 my_string[i]값을 추가
            temp_str += my_string[i]
            #i+1 최대길이이거나 my_string[i+1]의 값이 숫자가 아니면
            if i+1 == len(my_string) or my_string[i+1].isdigit() != True:
                #temp_str에 저장된 값을 int로 바꿔서 answer에 누적 저장
                answer += int(temp_str)
                #새로운 temp_str을 위해서 초기화
                temp_str = ''
    return answer