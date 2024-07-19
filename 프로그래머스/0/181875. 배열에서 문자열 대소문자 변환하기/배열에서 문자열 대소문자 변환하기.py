def solution(strArr):
    answer = []
    #strArr리스트의 range(len())을 사용하여 인덱스로 접근 가능하게 한다.
    for i in range(len(strArr)):
        #i 번째 인덱스 즉 짝수일때는
        if i % 2 == 0:
            #answer배열에 strArr을 str로 형 변환 해준 뒤 소문자로 바꿔준 값을 append함수를                 사용하여 추가해준다. strArr[i]는 strArr의 i번째 인덱스의 값을 나타낸다. 
            answer.append(str(strArr[i].lower()))
            #i 번째 인덱스가 홀수일때는
        else:
            #answer배열에 대문자로 바꿔준 값을 append함수를 사용하여 추가해준다.
            answer.append(str(strArr[i].upper()))
            
    return answer