def solution(absolutes, signs):
    answer = 0
    #signs길이와 absolutes길이가 같으니까 range(len())사용해서 인덱스로 접근
    for i in range(len(absolutes)):
        #signs[i]의 값이 true 일 때
        if signs[i]:
            #answer에 absolutes[i]을 누적으로 합 해준다.
            answer += absolutes[i]
        #signs[i]가 false일 때
        else:
            #-absolutes[i]를 누적으로 합 해준다.
            answer += -absolutes[i]
    return answer