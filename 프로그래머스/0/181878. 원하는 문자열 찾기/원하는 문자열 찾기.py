def solution(myString, pat):
    answer = 0
    #대소문자를 구분하지 않는다고 했으니 myString과 pat을 모두 소문자로 바꿔준 뒤
    myString = myString.lower()
    pat = pat.lower()
    #myString문자열에서 pat이 있으면
    if pat in myString:
        #answer에 1을 대입하고
        answer = 1
        #그렇지 않으면 0을 대입한다.
    else:
        answer = 0
    return answer