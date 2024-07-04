def solution(s):
    answer = ''
    #리스트 형식으로 담아줄 m을 구한다.
    m = []
    #s를 list형식으로 변환 후 for문 돌림
    for i in list(s):
        # 리스트 형식m에 list(s)의 각 원소 값들을 차레대로 넣어준다.
        m.append(i)
        #reverse = True를 선언하여 m을 내림차순으로 배치한다.
        m.sort(reverse = True)
        #그 후 answer에 join함수를 사용하여 str형식으로 변형하여준다.
        answer = ''.join(m)
    return answer