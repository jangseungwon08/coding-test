def solution(my_string, indices):
    answer = ''
    #리스트 형식으로 문자열을 하나씩 원소를 나눔
    temp = list(my_string)
    #indices배열을 순회
    for i in indices:
        #temp[i]번째 value값을 ''로 변경
        temp[i] = ''
    #for문 순회 후 join함수를 사용하여 temp를 answer에 join
    answer = ''.join(temp)
    return answer