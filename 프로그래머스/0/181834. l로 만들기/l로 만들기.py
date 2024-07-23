def solution(myString):
    answer = ''
    #myString for문을 돌면서
    for i in myString:
        #ascii코드를 이용하여 문자 l보다 작은 문자들이 있을경우에 'l'을 저장
        if ord('l') > ord(i):
            answer += 'l'
            # l보다 클 경우에는 원래의 문자들을 저장
        else:
            answer += i
    return answer