def solution(s):
    answer = ''
    #s를 사전 순으로 정렬해서 리스트로 바꿈
    s = sorted(s)
    #s를 순회하면서
    for i in s:
        #s의 각 원소값 i의 count값이 1 일때 
        if s.count(i) == 1:
            #answer에 count가 1인 i값을 넣음
            answer += i
            #answer 리턴
    return answer