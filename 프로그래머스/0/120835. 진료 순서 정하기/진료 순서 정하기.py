def solution(emergency):
    answer = []
    #emergency를 내림차순 정렬 후 temp에 저장
    temp = sorted(emergency, reverse = True)
    #emergency배열을 순회하면서
    for i in emergency:
        #answer에 temp배열 원소 i 값의 인덱스위치에 +1해준 값을 append
        answer.append(temp.index(i)+1)
    return answer