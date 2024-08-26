def solution(s, skip, index):
    answer = ''
    #소문자로만 이뤄진 알파벳 리스트
    temp_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #skip문자열 순회하면서
    for i in skip:
        #각 문자열 i가 temp_alpha에 있으면
        if i in temp_alpha:
            #i의 원소값에 해당하는 원소를 temp_alpha에서 제거
            temp_alpha.remove(i)
    #문자열 s 순회하면서
    for j in s:
        #temp_alpha의 인덱스 번호 + 건너 뛸 index번호가 temp_alpha의 길이보다 작을때
        if temp_alpha.index(j) + index < len(temp_alpha):
            #temp_index에 temp_alpha(j)의 인덱스번호 + index값을 더한 값을 저장
            temp_index = temp_alpha.index(j) + index
            #answer에 temp_alpha의 temp_index번째 인덱스 원소값을 저장
            answer += temp_alpha[temp_index]
            #temp_alpha의 길이보다 클 때
        else:
            #temp_index에 temp_alpha.index(j) + index한 값을 temp_alpha의 길이만큼 모듈러               연산을 해줌-> 리스트 인덱스 범위 초과하면 처음으로 돌아가게 함
            temp_index = (temp_alpha.index(j) + index) % len(temp_alpha)
            answer += temp_alpha[temp_index]
    return answer
