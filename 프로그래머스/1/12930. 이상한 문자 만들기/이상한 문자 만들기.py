def solution(s):
    res = []
    #단어를 기준으로 짝 홀수 인덱스를 판단해야되니까 공백을 기준으로 split한 결과를 temp에 대입
    temp = s.split(' ')
    #temp를 for문을 돌면서
    for j in temp:
        answer = ''
        #j의 단어 try hello world의 각 단어 길이만큼 첫번째 try는 0 1 2 의 인덱스 값을 가지고
        #hello는 0 1 2 3 4 의 인덱스 값을 가진다 이렇게 0번째 공백을 제거하고 단어별로 
        #인덱스를 접근해서 한다.
        for i in range(len(j)):
            #i의 인덱스값이 짝수면 대문자
            if i % 2 == 0:
                answer += j[i].upper()
            #홀수면 소문자에 대입한다.
            else:
                answer += j[i].lower()
            #하지만 answer의 값만으로는 공백이 제거되었기 때문에 다시 list형식의 res의 
            #list안에 answer를 하나대로 넣어준다. [try,hello,world]
        res.append(answer)
        #공백을 기준으로 join함수를 사용하여 리턴해준다.
    return ' '.join(res)
