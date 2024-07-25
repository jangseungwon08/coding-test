def solution(name, yearning, photo):
    answer = []
    dic = {}
    #일단 name과 yearning의 길이가 같고 같은 위치의 값을 찾아야되니까 dict형태로 바꿔준 값을 dic에 저장
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
        #photo의 행을 돌면서
    for j in photo:
        #각 행마다 count값을 찾아야되기 때문에
        count = 0
        #각 행의 열을 돌면서
        for k in j:
            #각 행의 열(문자열)이 dic에 존재하면
            if k in dic:
                #dic[k]->딕셔너리에서 key k 의 value값을 나타냄.
                
                count += dic[k]
        #각 행의 열을 다 검색한 count값을 answer에 append
        answer.append(count)
    return answer