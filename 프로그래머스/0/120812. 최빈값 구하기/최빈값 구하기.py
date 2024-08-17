def solution(array):
    answer = 0
    #딕셔너리 형태 임시 저장
    temp_dic = {}
    #key 임시 저장
    keys = []
    #array 순회하면서
    for i in array:
        #i의 값이 temp_dic안에 있으면
        if i in temp_dic:
            # 1 누적 증가
            temp_dic[i] += 1
            #없으면
        else:
            #1로 만들어줌
            temp_dic[i] = 1
    #가장 큰 value 값은 temp_dic의 values중에 max값이 가장 큰 값이다
    max_value = max(temp_dic.values())
    #temp_dic을 key값과 value값을 동시에 가져오면서
    for key, value in temp_dic.items():
        #해당 value 값이 최대 빈도수 값과 같으면
        if value == max_value:
            #keys배열에 key값을 append해준다
            keys.append(key)
            #keys값의 길이가 1 이상 즉 최빈값이 여러개면
    if len(keys) > 1:
        #-1 리턴
        return -1
    #그렇지 않으면
    else:
        #keys배열 첫번째 인덱스 리턴
        return keys[0]