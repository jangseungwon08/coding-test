def solution(data, ext, val_ext, sort_by):
    answer = []
    #sort_by되기 전 ext와 val_ext의 조건을 만족하는 부분을 저장하기 위한 temp
    temp = []
    #data에서 인덱스를 알기위해서 data_name리스트 
    data_name = ["code", "date", "maximum", "remain"]
    #data순회
    for i in data:
        # data_name에서 ext의 원소값을 가지는 인덱스값을 i의 인덱스값에 저장 한 값이 val_ext보다 작으면
        if val_ext > i[data_name.index(ext)]:
            #temp리스트에 i append
            temp.append(i)
            #sorted함수 사용하여 temp를 정렬하는데 key값으로는 data_name에서 sort_by의 value값을 가지는 값을 사용하여 그 값을 기준으로 하여 오름차순 정렬
    answer = sorted(temp, key = lambda x:x[data_name.index(sort_by)])
    return answer