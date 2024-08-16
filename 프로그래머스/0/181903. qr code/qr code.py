def solution(q, r, code):
    answer = ''
    #문자열 code를 인덱스 형식으로 순회
    for i in range(len(code)):
        #i번째 인덱스를 q로 나눈 나머지가 r일때
        if i % q == r:
            #code문자열의 i번째 인덱스의 value값을 answer에 누적
            answer += code[i]
    return answer