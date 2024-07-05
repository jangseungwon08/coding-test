def solution(price, money, count):
    answer = 0
    #중간 놀이공원 n번째 이용을 위해 이용료를 받기 위한 이용금액의 총액
    n = 0
    #count를 4면 1 2 3 4 로 사용하니까 1부터 count+1까지 범위 맞춰줌
    for i in range(1,count+1):
        # n에 i*price의 값들을 for문을 돌면서 더해준 값을 변수 n에 대입
        n += i*price
        #money 값이 n보다 크면 0을 반환하고
        if money >= n:
            answer = 0
        #money 값이 n보다 작으면 모자른 값을 반환해야되니까 놀이기구 이용의 총액 - 현재 가지고있는 
        #돈 money를 빼줘서 answer에 대입
        else:
            answer = n - money
    return answer
