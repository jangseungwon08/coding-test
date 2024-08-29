def solution(sides):
    answer = 0
    #가장 긴 변이 sides에 있는 경우 , 나머지 한 변이 가장 긴 변인 경우
    maximum = max(sides)
    minimum = min(sides)
    #가장 긴 변이 sides에 있는경우
    #가장 긴 변이 두 변의 길이보다 작아야된다. 그렇기 때문에 가장 긴 변이 sides에 있는 경우는          maximum에서 minimum을 뺀 값에서 1을 더해줘야된다. 그렇게 되면 최소한 다른 두 변을 더했을        때는 가장 긴 변 보다 크게 된다.
    for _ in range(maximum- minimum+1, maximum+1):
        answer += 1
    #가장 긴 변이 다른 한 변인 경우
    for _ in range(maximum+1, maximum+minimum):
        answer += 1
    return answer