def solution(order):
    answer = 0
    #각 숫자가 있는 것을 확인하기 위해서 list(str())형식으로 29423처럼 여러 숫자가 있는 것도 
    # 하나하나 셀 수 있게 하기 위해 list(str()) 형식으로 변환하여 for문을 돌린다.
    for i in list(str(order)):
        #"3"이 i안에 있으면 answer1 증가 
        if "3" in i:
            answer += 1
        elif "6" in i:
            answer += 1
        elif "9" in i:
            answer += 1
    return answer