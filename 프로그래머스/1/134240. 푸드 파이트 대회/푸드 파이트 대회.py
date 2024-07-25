def solution(food):
    answer = ''
    #1부터 len(food)-1 까지
    for i in range(1,len(food)):
        #food i번째 인덱스value값이 2이상이면 
        if food[i] >= 2:
            #str(i)를 food[i] //2 의 값만큼 반복
            answer += str(i)*(food[i] // 2)
    #중간에 0이 들어가야되니까 0 추가
    answer += str(0)
    #역순으로 range(len(food)-1)은 food의 길이가 예시에서 4니까 인덱스로 접근하려면 3부터 시작해야된다. 따라서 len(food)-1을 해줘서 3을 만들어준다. 1까지 -1만큼 감소시킨다.
    for j in range(len(food)-1,0,-1):
        if food[j] >= 2:
            answer += str(j)*(food[j] // 2)
    return answer