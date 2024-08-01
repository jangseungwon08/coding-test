def solution(emergency):
    answer = []
    '''리스트 형식으로 솔루션
    #emergency를 내림차순 정렬 후 temp에 저장
    temp = sorted(emergency, reverse = True)
    #emergency배열을 순회하면서
    for i in emergency:
        #answer에 temp배열 원소 i 값의 인덱스위치에 +1해준 값을 append
        answer.append(temp.index(i)+1)
        '''
    temp = sorted(emergency, reverse = True)
    #딕서녀리 선언
    dic = {}
    #temp 의 인덱스 순회하면서
    for i in range(len(temp)):
        #temp[i]의 value값을 key로 인덱스+1값을 value로 해서 딕셔너리 생성
        dic[temp[i]] = i+1
        #emergency의 value값으로 순회
    for j in emergency:
        #dic[j]만약에 emergency에 76이라는 원소값이 있으면 dic[j]-> dic[76]키 값에 접근하여
        #키 값에 맞는 value값을 뽑아내서 answer에 append
        answer.append(dic[j])
    return answer