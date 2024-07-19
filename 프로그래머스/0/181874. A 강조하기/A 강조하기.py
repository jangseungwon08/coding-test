def solution(myString):
    answer = ''
    #myString을 전체 소문자로 변환해준다.
    myString = myString.lower()
    #myString을 for문을 돌린 뒤 
    for i in myString:
        #a의 아스키 코드값이 97이다. 따라서 ord(i) == 97이면
        if ord(i) == 97:
            #a를 A로 바꿔준다.
            answer += i.upper()
            #a가 아니면 그냥 answer값에 더해준다.
        else:
            answer += i
        
    return answer