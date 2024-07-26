def solution(myString):
    #split함수를 사용하여 'x'를 기준으로 나눠준 리스트 값을 answer에 저장
    answer = myString.split('x')
    #answer을 돌면서
    for i in answer:
         #''이 answer안에 있으면
        if '' in answer:
            #''원소 제거
            answer.remove('')
        #마지막으로 오름차순 정렬
    answer.sort()
    return answer