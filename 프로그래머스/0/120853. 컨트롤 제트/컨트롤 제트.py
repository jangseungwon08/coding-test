def solution(s):
    answer = 0
    #문자열이 공백 기준으로 되어있어서 공백을기준으로 나눔
    s = s.split(' ')
    #s를 인덱스 형식으로 순회
    for i in range(len(s)):
        #lstrip('-')를 사용하여 왼쪽 문자 '-'를 모두 제거하고 숫자인지 판별한다.
        if s[i].lstrip('-').isdigit():
            #숫자로 판별되면 s[i]번째 value값을 answer에 누적 합
            answer += int(s[i])
            #z로 판별되면
        else:
            #s[i-1]번째 value값을 answer에 누적 차
            answer -= int(s[i-1])
    return answer