def solution(s, n):
    answer = ''
    for i in s:
            #공백일때는 공백만 answer에 저장
        if i == ' ':
            answer += i
        elif (ord(i) + n) > ord('Z') and i.isupper():
                answer += chr(ord(i) -26 + n)
        elif (ord(i) + n) > ord('z') and i.islower(): 
                answer += chr(ord(i) -26 + n)
        else:
            answer += chr(ord(i) + n)
    return answer