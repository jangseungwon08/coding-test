def solution(order):
    answer = 0
    #아메리카노 리스트
    americano_list = ["iceamericano", "americanoice", "hotamericano", "americanohot", "americano", "anything"]
    #카페라떼 리스트
    cafelatte_list = ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    #order리스트 순회하면서
    for i in order:
        #문자열 i가 아메리카노 리스트에 존재하면
        if i in americano_list:
            #answer에 4500 누적
            answer += 4500
            #문자열 i가 cafelatte_list에 존재하면
        elif i in cafelatte_list:
            #answer에 5000 누적
            answer += 5000
    return answer