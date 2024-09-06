def solution(my_string):
    '''
    answer = 0
    #my_string을 공백을 기준으로 나눈 문자열들을 리스트 형식으로 temp에 저장
    temp = my_string.split(' ')
    #처음 숫자temp[0]을 answer에 저장
    answer = int(temp[0])
    #for문 1 부터 temp길이까지 돌면서 2칸씩 점프(연산자만 찾는 for문)
    for i in range(1, len(temp), 2):
        #연산자 다음 숫자를 num변수에 저장 2칸씩 띄우고 1을 더하면 뒤에 숫자니까
        num = int(temp[i+1])
        #temp[i]의 값이 +면
        if temp[i] == "+":
            #answer의 초기화 한 값에 num저장
            answer += num
            #-면
        elif temp[i] == "-":
            #빼줌
            answer -= num
            
    return answer
    '''
solution = eval