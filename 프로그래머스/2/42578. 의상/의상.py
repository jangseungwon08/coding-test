def solution(clothes):
    answer = 0
    #clothes에 있는 각 행의 1번째 인덱스 값과 개수를 정하기 위해 clothes_dict 선언
    clothes_dict = {}
    #clothes순회하면서
    for i in clothes:
        #clothes_dict i번째 1번째 인덱스를 key값으로 하고 clothes_dict.get을                이용하여 i번째 1번째 인덱스의 개수를 0으로 두고 그 key값이 나올 때 마다 1씩             추가해줌
        clothes_dict[i[1]] = clothes_dict.get(i[1], 0 ) + 1
    #for문 다 순회 후 clothes_dict의 종류가 2개 이상이면
    if len(clothes_dict) > 1:
        #answer를 1로 둔다. (0에 곱하면 0이 되기 때문)
        answer = 1
        #clothes_dict을 value값을 기준으로 순회하면서
        for i in clothes_dict.values():
            #i의 값에 1을 더해준 값을 answer에 누적 저장
            answer *= (i+1)
        #for문 순회 후 1을 빼줌
        answer -= 1
    #clothes의 종류가 한개일때는
    else:
        #clothes_dict에 있는 values들을 모두 들고와서 list로 변경 후 0번째 인덱스의            value값을 answer에 저장
        answer = list(clothes_dict.values())[0]
    return answer