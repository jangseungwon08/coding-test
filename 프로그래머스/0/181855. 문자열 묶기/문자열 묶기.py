def solution(strArr):
    answer = 0
    #문자열 마다 키 value값을 알기 위해서 임시 dic생성
    temp_dic = {}
    #strArr 순회하면서
    for i in strArr:
        #len(i)의 값이 dic.keys의 값에 있으면
        if len(i) in temp_dic.keys():
            #temp_dic의 len(i) key값의 value값 1 증가
            temp_dic[len(i)] += 1
            #len(i)의 값이 dic.keys값에 없으면 1로 설정
        else:
            temp_dic[len(i)] = 1
            #for문 순회 끝나고 temp_dic의 value값들 중에 max값을 answer에 저장
    answer = max(temp_dic.values())
    return answer